#
######################################
# ECR Parameters
######################################
#
# publish to s3
echo "*** INFO: publishing to s3"
aws --profile ${profile} --region ${s3CloudFormationArtifactsRegion} \
    s3 cp --recursive \
    --include "*.yaml" \
    ecr s3://${s3CloudFormationArtifactsName}/ecr

## set parameters
echo "*** INFO: set stack parameters"
stackParameters="\
    ParameterKey=ecrBuildContainerName,ParameterValue=${buildContainerName} \
"

# get existing stack info
echo "*** INFO: find stack"
stackName=${deployment}-ecr-main
stackExists=$(aws --profile ${profile} --region ${region} \
    cloudformation describe-stacks \
    --stack-name ${stackName} \
    --query "Stacks[?StackName==\`${stackName}\`]" \
    --output text)
stackTemplateUrl=${s3CloudFormationArtifactsUrl}/ecr/ecr.yaml

if [[ -z "${stackExists}" ]]; then
    echo "Creating ${stackName} now ..."
    aws --profile ${profile} --region ${region} \
        cloudformation create-stack \
        --stack-name ${stackName} \
        --template-url ${stackTemplateUrl} \
        --parameters ${stackParameters} \
        --capabilities CAPABILITY_NAMED_IAM
else
    echo "stackExists ${stackName} updating now ..."
    aws --profile ${profile} --region ${region} \
        cloudformation update-stack \
        --stack-name ${stackName} \
        --template-url ${stackTemplateUrl} \
        --parameters ${stackParameters} \
        --capabilities CAPABILITY_NAMED_IAM
fi

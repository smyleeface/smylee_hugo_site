#
######################################
# Cognito
######################################
#
#
## publish to s3
echo "*** INFO: publishing to s3"
aws --profile ${profile} --region ${s3CloudFormationArtifactsRegion} \
    s3 cp --recursive \
    --exclude "*" \
    --include "*.yaml" \
    --acl public-read \
    cognito s3://${s3CloudFormationArtifactsName}/cognito

## set parameters
echo "*** INFO: set stack parameters"
stackParameters="\
    ParameterKey=CloudformationS3BucketUrl,ParameterValue=${s3CloudFormationArtifactsUrl} \
    ParameterKey=ExternalId,ParameterValue=${UUID}
"

# set configuration values
echo "*** INFO: find stack"
stackName=${deployment}-cognito-main
stackExists=$(aws --profile ${profile} --region ${region} \
    cloudformation describe-stacks \
    --stack-name ${stackName} \
    --query "Stacks[?StackName==\`${stackName}\`]" \
    --output text)
stackTemplateUrl=${s3CloudFormationArtifactsUrl}/cognito/main.yaml

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

#
######################################
# S3 Parameters
######################################
#


# publish to s3
aws --profile ${profile} --region ${s3CloudFormationArtifactsRegion} \
    s3 cp --recursive \
    --include "*.yaml" \
    s3 s3://${s3CloudFormationArtifactsName}/s3

## set parameters
stackParameters="\
    ParameterKey=s3CodePipelineArtifactsBucketName,ParameterValue=${s3CodePipelineArtifactsBucketName} \
    ParameterKey=s3CodePipelineTriggerBucketName,ParameterValue=${s3CodePipelineTriggerBucketName} \
    ParameterKey=s3SiteDomainStagingBucketName,ParameterValue=${s3SiteDomainStagingBucketName} \
    ParameterKey=s3SiteDomainProductionBucketName,ParameterValue=${s3SiteDomainProductionBucketName} \
    ParameterKey=s3SiteAssetBucketName,ParameterValue=${s3SiteAssetBucketName} \
    ParameterKey=s3PublicBucketName,ParameterValue=${s3PublicBucketName} \
"

# get existing stack info
stackName=${deployment}-s3-main
stackExists=$(aws --profile ${profile} --region ${region} \
    cloudformation describe-stacks \
    --stack-name ${stackName} \
    --query "Stacks[?StackName==\`${stackName}\`]" \
    --output text)

if [[ -z "${stackExists}" ]]; then
    echo "Creating ${stackName} now ..."
    stackTemplateUrl=${s3CloudFormationArtifactsUrl}/${service}/s3-create.yaml
    aws --profile ${profile} --region ${region} \
        cloudformation create-stack \
        --stack-name ${stackName} \
        --template-url ${stackTemplateUrl} \
        --parameters ${stackParameters} \
        --capabilities CAPABILITY_NAMED_IAM
else
    echo "stackExists ${stackName} updating now ..."
    stackTemplateUrl=${s3CloudFormationArtifactsUrl}/${service}/s3-update.yaml &&
    aws --profile ${profile} --region ${region} \
        cloudformation update-stack \
        --stack-name ${stackName} \
        --template-url ${stackTemplateUrl} \
        --parameters ${stackParameters} \
        --capabilities CAPABILITY_NAMED_IAM
fi

#
######################################
# CodeBuild and CodePipeline
######################################
#
## publish to s3
echo "*** INFO: publishing to s3"
aws --profile ${profile} --region ${s3CloudFormationArtifactsRegion} \
    s3 cp --recursive \
    --exclude "*" \
    --include "*.yaml" \
    --acl public-read \
    codebuild s3://${s3CloudFormationArtifactsName}/codebuild

echo "*** INFO: publishing to s3"
aws --profile ${profile} --region ${s3CloudFormationArtifactsRegion} \
    s3 cp --recursive \
    --exclude "*" \
    --include "*.yaml" \
    --acl public-read \
    codepipeline s3://${s3CloudFormationArtifactsName}/codepipeline


echo "*** INFO: parameter store"
githubAccessTokenName="/${deployment}/hugosite/codepipeline/github/personal-access-token"
aws --profile ${profile} --region ${region} \
    ssm put-parameter \
    --name ${githubAccessTokenName} \
    --description "The GitHub Personal Access token location or value. This should already exist in SSM Parameter Store under the key '${githubAccessTokenName}'" \
    --value ${githubAccessToken} \
    --type String

## set parameters
echo "*** INFO: set stack parameters"
stackParameters="\
    ParameterKey=Deployment,ParameterValue=${deployment} \
    ParameterKey=CloudformationS3BucketUrl,ParameterValue=${s3CloudFormationArtifactsUrl} \
    ParameterKey=CodeBuildGitHubUrl,ParameterValue=${githubRepoUrl} \
    ParameterKey=CodePipelineS3Bucket,ParameterValue=${s3CodePipelineArtifactsBucketName} \
    ParameterKey=CodePipelineGitHubOwner,ParameterValue=${githubOwner} \
    ParameterKey=CodePipelineGitHubRepo,ParameterValue=${githubRepo} \
    ParameterKey=CodePipelineGitHubBranch,ParameterValue=${githubBranch} \
    ParameterKey=CodeBuildS3StagingName,ParameterValue=${s3SiteDomainStagingBucketName} \
    ParameterKey=CodeBuildS3ProductionName,ParameterValue=${s3SiteDomainProductionBucketName} \
    ParameterKey=CodeBuildHugoSiteBuildContainer,ParameterValue=${buildContainerUrl}
    ParameterKey=CodePipelineGitHubToken,ParameterValue=${githubAccessTokenName}
"

# set configuration values
echo "*** INFO: find stack"
stackName=${deployment}-codebuild-codepipeline-main
stackExists=$(aws --profile ${profile} --region ${region} \
    cloudformation describe-stacks \
    --stack-name ${stackName} \
    --query "Stacks[?StackName==\`${stackName}\`]" \
    --output text)
stackTemplateUrl=${s3CloudFormationArtifactsUrl}/codebuild/main.yaml

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

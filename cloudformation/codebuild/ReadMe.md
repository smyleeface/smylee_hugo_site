CodeBuild and CodePipeline
==========================

Executing upon repository update, CodePipeline will trigger a workflow to update the Website.

### Before Running CloudFormation Template
[CodePipeline uses both GitHub OAuth tokens and personal access tokens](https://docs.aws.amazon.com/codepipeline/latest/userguide/GitHub-authentication.html)
* Give GitHub access to your CodePipeline and CodeBuild.
    * The easiest way to do this is via the console by beginning the process of creating a pipeline and connect the GitHub account. It will prompt for authorization, and after allowing, it will not prompt again until you revoke access. Cancel the creation of the CodePipeline.
    * Follow the same process for CodeBuild.
* Generate a [GitHub personal access token](https://github.com/settings/tokens) for use by CodePipelie.
  > NOTE: Personal access tokens are only needed because CloudFormation is creating the pipeline. This is also required when using CLI or SDK.
* Store your GitHub personal access token as `String` parameter called `/hugosite/codepipeline/github/personal-access-token` in the region you are planning to deploy. 
  > NOTE: Ideally this would be a SecureString, but [SecureString is currently not supported in CloudFormation (20180429)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types-unsupported).

### Resources
* [CodePipeline Action Type Constraints for Artifacts](https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#w204aac37b9b9c15b3)
* [Action Configuration Properties for Provider Types](https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#w204aac37b9b9c21b3)
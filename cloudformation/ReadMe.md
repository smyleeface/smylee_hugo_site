CloudFormation Templates
========================

Set of CloudFormation templates used to build smylee.com. As services are finalized, they are converted to CloudFormation templates.
Ongoing project.

## Before Running CloudFormation Templates
* Run `s3-cloudformation-artifacts.yaml` CloudFormation template. This will create a bucket where main stacks can reference the CloudFormation files.
* [CodeBuild Running CloudFormation Template](codebuild/ReadMe.md#before-running)
* Run the deploy for the ECR service to create the docker images for CodeBuild/CodePipeline 
    * `ecr`
    * `ecr_publish`
    
## Deploy CloudFormation

* Copy deploy.sh.dist to `deploy.sh`
* Edit `deploy.sh` and fill in the env var section on the top
* From the `cloudformation` directory run 
    ```sh
    bash deploy.sh <SERVICE_NAME>
    ```
    replacing `<SERVICE_NAME>` for one of commands the below
    
## Services

1. S3
    * COMMAND: `s3`
    * S3 buckets for the project.
    * First thing to run. Pretty much every service relies on S3.
1. ECR
    * COMMAND: `ecr`
    * Creates the repository that holds the images used to build the site.
1. Container Image
    * COMMAND: `ecr_publish`
    * Dependent On: `ECR`
    * Creates and publishes the images used to build the site.
1. [CodeBuild and CodePipeline](codebuild/ReadMe.md)
    * COMMAND: `codebuild`
    * Dependent On: `ECR` & `Container Image`
    * Executing upon repository update, CodePipeline will trigger a workflow to update the Website.
    * The CodePipeline will include CodeBuild Artifacts.
1. [Cognito](cognito/ReadMe.md)
    * COMMAND: `cognito`
    * Generates user pool and identity pool for future use of site management system and/or viewing of private posts.

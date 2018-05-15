Cognito User and Identity Pools
===============================

This CloudFormation will create a Cognito User Pool, Federated Identity, and register the Cognito User Pool witll the Federated Identity. The Federated Identity only allows authenticated users.

1. Create an S3 bucket or use an existing S3 bucket that CloudFormation has access to.
1. Upload all the files in the `cloudformation` directory to the S3 bucket.
1. Copy the S3 template URL to the file `cognito-main.yaml`
1. Create a new CloudFormation stack and `Specify an Amazon S3 template URL` to the S3 bucket `cognito-main.yaml` is located.

    OR

    `Upload a template to Amazon S3` and choose `cognito-main.yaml` from your local system.

1. Fill the parameters:
    1. Stack name: any name you want
    2. CloudformationS3BucketUrl: the URL to the S3 bucket and path the CloudFormation files are uploaded
    1. ExternalId: used in policy conditions when giving permissions to cognito. 
        > See [How to Use an External ID When Granting Access to Your AWS Resources to a Third Party](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html) for more information.
1. Follow the rest of the prompts, leaving values at default, to complete the setup of the CloudFormation stack. 
1. To find values needed for the application, see the CloudFormation `Outputs` in the different stacks created after the templates are finished running.
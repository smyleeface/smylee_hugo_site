+++
title = "Magic Night Project - Part 2: Slack Slash Commands for GitHub Pull Request Actions"
date = "2016-06-07T17:30:47-07:00"
toc = true
draft = false
categories = ["Step-by-Step Guides"]
tags = ["AWS", "Lambda", "API Gateway", "GitHub", "Slack", "Magic Night", "IAM", "Encryption Keys", "AWS CLI"]
+++

## Description
When a custom Slack command is triggered, the corresponding command will change the state of a GitHub pull request.  A magic night project provided by [AWS User Group Hosted by MindTouch](http://www.meetup.com/AWS-UG-San-Diego/events/230499687/).

## Tools used in this project
* Slack: smylee.Slack.com
* GitHub: GitHub.com/smyleeface/shiny-palm-tree
* Amazon API Gateway, Lambda, IAM > Roles, Encryption Keys
* AWS CLI

## Prerequisites
* [GitHub Pull Request Alert on Slack (Magic Night Project - Part 1)](/post/2016/06/07_magicnight_pt1/)
* The AWS CLI installed with a user and valid API key with an authorized user to run the kms command before continuing.<br>See http://docs.aws.amazon.com/cli/latest/userguide/installing.html for details.

## Lambda Function
1. Create a new Lambda Function; skip selecting blueprint.
	* Name the function, and choose Python 2.7.
	* [Download](/files/20160607-magicnight/lambda_smylee_slack_github_action.py) and copy/paste the code into the textarea.
	* Replace GITHUB_OWNER. You will replace the other two keys, ENCRYPTED_EXPECTED_TOKEN and GITHUB_TOKEN later.
	* Use the Lambda_basic_execution Role, or the Role created in part 1.
	* Leave the rest of the setting default. You can choose your own VPC, but I'm choosing "No VPC" in this configuration.
	* Review and Create. We're not quite ready to run this yet.<br><br>
![Lambda Slack to GitHub](/images/20160607-magicnight/lambda_slack_to_github.png "Lambda Slack to GitHub")

## API Gateway
1. Create the API Gateway or use the API Gateway from the part 1.
2. Add a new resource from the root of the API. Choose Lambda Function > us-west-2 > smylee_github_slack_action, save. After saving, a permissions prompt will popup choose OK.<br><br>
<img src="/images/20160607-magicnight/api_gateway_slack_to_github_setup.png" class="imginitial" alt="API Gateway Slack to GitHub Settings" title="API Gateway Slack to GitHub Settings">
2. Add a new Method > POST.<br><br>
![API Gateway Method POST](/images/20160607-magicnight/api_gateway_method_post.png "API Gateway Method POST")

3. In Integration Request:
  * Body Mapping Templates > When there are no templates defined (recommended)
  4. Add mapping template > application/x-www-form-urlencoded > Checkmark.<br><br>
![Mapping Template FORM](/images/20160607-magicnight/body_mapping_1.png "Mapping Template FORM")

  4. Add mapping template > application/json > Checkmark.<br><br>
<img src="/images/20160607-magicnight/body_mapping_2.png" class="imginitial" alt="Mapping Template JSON" title="Mapping Template JSON">

  4. Add { "body": $input.json("$") } > Save to both mapping templates.<br><br>
![Generate Template](/images/20160607-magicnight/body_mapping_3.png "Generate Template")

6. Deploy API.<br><br>
![Deploy API](/images/20160607-magicnight/deploy_api.png "Deploy API")

10. Once the API is created, within Stages from the left side, drill down to the resource and click the method.<br><br>
<img src="/images/20160607-magicnight/api_gateway_post_url2.png" class="imginitial" alt="Deploy URL" title="Deploy URL">

11. This will display an "Invoke URL", copy this URL and we'll use it in the Slack Slash Command Setup section.<br><br>
![Invoke URL](/images/20160607-magicnight/api_gateway_invoke_url2.png "Invoke URL")

## Slack Slash Command Setup
3. From settings choose "Add an app or integration".<br><br>
<img src="/images/20160607-magicnight/add-app-integration.png" class="imginitial" alt="Add an app or integration" title="Add an app or integration">

4. In the textbox, type and choose "Slash Commands"<br><br>
![Slash Commands](/images/20160607-magicnight/slash-command.png "Slash Commands")

5. If this is the first slash command created, click on "install", otherwise "configure".
	* Enter the command that will trigger the API Gateway.<br><br>
	* Paste the Invoke URL from the API Gateway into the URL field for the Slack command.
	* Copy the Token.
	* Complete and save the form.<br><br>
![Create Slash Commands](/images/20160607-magicnight/create_slash_command.png "Create Slash Commands")

8. You will use the Slack token to create the encryption blob.

## KMS Keys
1. Choose the region from the filter that matches the Lambda function previously setup.
2. Create a new key and enter an alias.<br><br>
![Create Key Alias](/images/20160607-magicnight/key_alias.png "Create Key Alias")

3. Do not add any users to Define Key Administrative Permissions, unless there is a user that you want to be able to manage this key.
4. In Define Key Usage Permissions, find the role used in your Lambda function above.
5. Review policy and Finish.
6. Copy the ARN for the Encryption Key account just created.<br><br>
![Key Summary](/images/20160607-magicnight/key_summary.png "Key Summary")

## Add KMS Decrypt Policy to Role
1. In IAM, go to Roles, and edit the role created for the Lambda function.
2. From Permissions > Inline Policy > Create Role Policy > Custom Policy > Select
8. Enter the policy name.
8. [Download](/files/20160607-magicnight/role_policy.txt) and copy/paste the policy, replacing < your KMS key ARN > with the one copied in the KMS Keys section.
10. Validate and Apply Policy<br><br>
![Role Policy](/images/20160607-magicnight/key_policy.png "Role Policy")

## Create the base-64 encoded, encrypted Slack command token
1. In the command line where aws cli is installed, enter:<br> `aws kms encrypt --key-id alias/< ENCRYPTION KEY ALIAS > --plaintext "< SLACK TOKEN >" --region us-west-2`
2. Copy the CiphertextBlob in the output from the command line and place into the Lambda function replacing < CIPHERTEXT_BLOB ><br><br>
![CiphertextBlob](/images/20160607-magicnight/kms_key_blob.png "CiphertextBlob")

## GitHub Token
1. Under your profile > Settings > Personal access tokens > Generate new token.<br><br>
![Generate new token](/images/20160607-magicnight/github_personal_token.png "Generate new token")

2. Name the token, and choose the repo checkbox. Generate token.<br><br>
![Configure Token](/images/20160607-magicnight/new_personal_token.png "Configure Token")

3. Copy the token and paste it into the < GITHUB_TOKEN > in the Lambda function.<br><br>
![GitHub Token](/images/20160607-magicnight/personal_key.png "GitHub Token")

## Setup your Repo
1. In your repo, create a new file, name the file, add some text, and create a new branch, and propose new file to save.<br><br>
![Create new file in repo](/images/20160607-magicnight/github_create_new_file.png "Create new file in repo")

2. Click the Create a pull request button.<br><br>
![Create pull request](/images/20160607-magicnight/github_pull_request.png "Create pull request")

3. If you have your Slack open, you should've received a message in the channel.<br><br>
<img src="/images/20160607-magicnight/slack_pull_request_message_1.png" class="imginitial" alt="Recieve Slack Message" title="Recieve Slack Message">

## Testing
5. [Download](/files/20160607-magicnight/sample_input.txt) sample payload. (Note: This sample data may throw an error as it is a payload from my setup. You may be able to find your payload in CloudWatch.)
1. Test the Lambda function (see [part 1](/post/2016/06/07_magicnight_pt1/) for how to test). You could try the Slack command first to check CloudWatch to get the real payload for testing.
1. Test the api function, deploy if any changes were made. (see [part 1](/post/2016/06/07_magicnight_pt1/) for how to test). You could try the Slack command first to check CloudWatch to get the real payload for testing.
1. Test the Slack command.<br>
`/github close < repo-name > < pull-request number>`<br>
`/github open < repo-name > < pull-request number>`<br>
`/github merge < repo-name > < pull-request number>`<br><br>
![Command Response](/images/20160607-magicnight/open_close_message.png "Command Response")

1. You should receive two messages for each request. One from the return of the function which runs the GitHub command and second one is a message of the pull request status which is triggered from the setup of part 1 of this guide.
2. Invalid commands will return with an invalid message.<br><br>
<img src="/images/20160607-magicnight/not_valid.png" class="imginitial" alt="Invalid Command" title="Invalid Command">

## AWS Costs for creating this project
* AWS provides a lot of services for free for the first 12 months of sign up and beyond. More information can be found on AWS pricing pages.
* Cost should be less than $1 to create this project.
* [Lambda pricing cost](https://aws.amazon.com/lambda/pricing/) - Doesn't start to charge until you've made 1 million requests and gone over 400,000 GB-Seconds (each billed separately.)
* [API Gateway pricing cost](https://aws.amazon.com/api-gateway/pricing/) - Different for some regions, but all regions are billed per million calls received, plus the cost of data transfer out, in gigabytes. Plus you only pay for what you use.
* [Key Encryption](https://aws.amazon.com/kms/pricing/) - $1/month for a key and first 20,000 request/month free, and cost per use after.

## Footnotes
* You can skip using encryption key for this exercise by commenting out lines 13-14 & 27-29 in lambda_smylee_slack_github_action.py.


## Resources
* [https://developer.GitHub.com/v3/pulls/#merge-a-pull-request-merge-button](https://developer.GitHub.com/v3/pulls/#merge-a-pull-request-merge-button)
* [https://developer.GitHub.com/v3/pulls/#update-a-pull-request](https://developer.GitHub.com/v3/pulls/#update-a-pull-request)
* [http://stackoverflow.com/questions/4511598/how-to-make-http-delete-method-using-urllib2](http://stackoverflow.com/questions/4511598/how-to-make-http-delete-method-using-urllib2)
* Lambda > New function using blueprint Slack-echo-command-python
* [GitHub Pull Request Event API Information](https://developer.GitHub.com/v3/activity/events/types/#pullrequestevent)
* [Emoji Cheat Sheet](http://www.emoji-cheat-sheet.com)

+++
title = "Magic Night Project - Part 1: GitHub Pull Request Alert on Slack"
date = "2016-06-07T17:20:47-07:00"
toc = true
draft = false
categories = ["Step-by-Step Guides"]
tags = ["AWS", "Lambda", "API Gateway", "GitHub", "Slack", "Magic Night"]
+++

## Description
When a GitHub pull request is made, it will trigger an alert on Slack. A magic night project provided by [AWS User Group Hosted by MindTouch](http://www.meetup.com/AWS-UG-San-Diego/events/230499687/).

## Tools used in this project
* Slack: smylee.slack.com
* GitHub: github.com/smyleeface/shiny-palm-tree
* Amazon API Gateway & Lambda

## Slack Setup
1. Setup a Slack team if you don't have one to use.
2. Create a new channel (or skip this step to use an existing channel that the messages will appear.)<br><br>
![Create a Slack Channel](/images/20160607-magicnight/create-a-channel.png "Create a Slack Channel")

3. From settings choose "Add an app or integration".<br><br>
<img src="/images/20160607-magicnight/add-app-integration.png" class="imginitial" alt="Add an app or integration" title="Add an app or integration">

4. In the textbox, type and choose "Incoming Webhooks"<br><br>
![Incoming Webhooks](/images/20160607-magicnight/incoming-webhooks.png "Incoming Webhooks")

5. If this is the first Webhook created, click on "install", otherwise "configure".
6. Configure a new Webhook into the desired channel.<br><br>
![Configure a new Webhook](/images/20160607-magicnight/add-webhook-to-channel.png "Configure a new Webhook")

7. Complete and save the form. Note the Webhook URL for use later.<br><br>
![Webhook form](/images/20160607-magicnight/webhook-integration-settings.png "Webhook form")


## AWS Lambda Setup
1. Make sure you note the region you are using.<br><br>
<img src="/images/20160607-magicnight/lambda_region.png" class="imginitial" alt="Lambda Region" title="Lambda Region">

1. Create a new Lambda Function; skip selecting a blueprint.
2. Configure the Lambda function:
  * Name the function.
  * Choose "Python 2.7" as the Runtime.
  * [Download](/files/20160607-magicnight/lambda_smylee_github_slack_alert.py) and copy/paste the code into the textarea.
  * In the code, replace <ADD SLACK WEBHOOK URL HERE> to the Webhook I mentioned in the Slack setup.<br><br>
![Replace Code](/images/20160607-magicnight/lambda_smylee_github_slack_alert_code.png "Replace Code")

  * (optional) Choose a different emoji from the [emjoi cheet sheet](http://www.emoji-cheat-sheet.com) or change the username message in the code.
  * Use the default Handler (lambda_function.lambda_handler).
  * Create a new role with *Basic Execution Role.
    * This will open a new window/tab; use the default IAM Role and Create a new Role Policy.<br><br>
![Lambda default IAM Role](/images/20160607-magicnight/lambda_github_slack_iam_role.png "Lambda default IAM Role")

  * Leave the rest of the settings default. You can choose your own VPC, but I'm choosing "No VPC" in this configuration.
  * Review and Create.<br><br>
![Review and Create Lambda](/images/20160607-magicnight/lambda_function_review.png "Review and Create Lambda")

10. Test the function. On first test, Lambda will prompt for inputs. You can copy/paste the (VERY LONG) sample payload for the Pull Request Event from: https://developer.github.com/v3/activity/events/types/#pullrequestevent<br><br>
![Lambda will prompt for inputs](/images/20160607-magicnight/lambda_test_input_screen.png "Lambda will prompt for inputs")

11. Save and test! If you have your Slack open, you should've received a message in the channel where you setup the incoming Webhook. If you used the sample payload data, it will look something like this:<br><br>
<img src="/images/20160607-magicnight/api_gateway_slack_test_sample.png" class="imginitial" alt="Test button Slack response" title="Test button Slack response">

12. Now your Lambda function is ready to go, let's connect to an API Gateway!

## AWS API Gateway Setup
1. Setup a New API Gateway or use an existing Gateway if you have one setup.
2. Create a new Resource. Enter a name and use the default for the resource path.
3. Click on the new Resource and create a new Method > Post
4. Choose Lambda Function > us-west-2 > smylee_github_slack_alert, save. After saving, a permissions prompt will popup choose OK.<br><br>
<img src="/images/20160607-magicnight/api_lambda_setup.png" class="imginitial" alt="API Gateway Lambda Setup" title="API Gateway Lambda Setup">

5. Click on the method function just created and four boxes will appear on the right side, click the Test Icon.<br><br>
![Test API Gateway](/images/20160607-magicnight/api_gateway_method_execution_screen.png "Test API Gateway")

6. In the Request Body textarea, paste the same payload used for the pull request event. (https://developer.github.com/v3/activity/events/types/#pullrequestevent)<br><br>
<img src="/images/20160607-magicnight/awi_gateway_test_request_body.png" class="imginitial" alt="Request Body textarea" title="Request Body textarea">

7. Click the Test button and if you have your Slack open, you should've recived a message in the channel you setup the incoming Webhook!<br><br>
<img src="/images/20160607-magicnight/api_gateway_slack_test_sample.png" class="imginitial" alt="Test button Slack response" title="Test button Slack response">

8. Now deploy the API from Actions > Deploy API.<br><br>
<img src="/images/20160607-magicnight/api_gateway_deploy_api.png" class="imginitial" alt="Deploy API" title="Deploy API">

9. In Deployment Stage, Choose [New Stage], in the stage name enter "prod" (this will be part of the API url.)<br><br>
![Deploy API Setup](/images/20160607-magicnight/api_gateway_deploy_setup.png "Deploy API Setup")

10. Once the API is created, within Stages from the left side, drill down to the resource and click the method.<br><br>
<img src="/images/20160607-magicnight/api_gateway_post_url.png" class="imginitial" alt="Deploy URL" title="Deploy URL">

11. This will display an "Invoke URL", copy this URL and we'll use it in the GitHub Setup section.<br><br>
![Invoke URL](/images/20160607-magicnight/api_gateway_invoke_url.png "Invoke URL")

## GitHub Setup
1. Create a new repository, add some files.
2. In the settings for the repository, go to Webhooks & Services > Add Webhook.<br><br>
![Add Webhook](/images/20160607-magicnight/github-webhooks.png "Add Webhook")

3. In the Payload URL, enter the URL from the API Gateway we just deployed.<br>Under "Which events would you like to trigger this webhook?", choose: Let me select individual events. > Pull request<br><br>
![GitHub Webhook](/images/20160607-magicnight/github_webhook_api_gateway.png "GitHub Webhook")

5. Save webhook.

## Try it out!
1. In your repo, create a new file, name the file, add some text, and create a new branch, and propose new file to save.<br><br>
![Create new file in repo](/images/20160607-magicnight/github_create_new_file.png "Create new file in repo")

2. Click the Create a pull request button.<br><br>
![Create pull request](/images/20160607-magicnight/github_pull_request.png "Create pull request")

3. If you have your Slack open, you should've received a message in the channel!<br><br>
<img src="/images/20160607-magicnight/slack_pull_request_message_1.png" class="imginitial" alt="Receive Slack Message" title="Receive Slack Message">

4. Try closing, opening, and merging the pull request from GitHub and you should receive messages for each action (merge will report closed).<br><br>
<img src="/images/20160607-magicnight/slack_open_close_message.png" class="imginitial" alt="Close,Open,Merge Repo" title="Close,Open,Merge Repo">


## Footnotes
* Now anytime a pull request is made on this repo it will alert you on Slack.
* If you want to customize the message, make the change in the slack_message inside the Lambda function.
* Troubleshooting note: Check your CloudWatch Logs /aws/lambda/< lambda function name > for messages that were logged.<br><br>
![CloudWatch Logs](/images/20160607-magicnight/cloudwatch_logs2.png "CloudWatch Logs")


## AWS Costs for creating this project
* AWS provides a lot of services for free for the first 12 months of sign up and beyond. More information can be found on AWS pricing pages.
* Cost should be less than $0.10 to create this project.
* [Lambda pricing cost](https://aws.amazon.com/lambda/pricing/) - Doesn't start to charge until you've made 1 million requests and gone over 400,000 GB-Seconds (each billed separately.)
* [API Gateway pricing cost](https://aws.amazon.com/api-gateway/pricing/) - Different for some regions, but all regions are billed per million calls received, plus the cost of data transfer out, in gigabytes. Plus you only pay for what you use.

## Resources
* [GitHub Pull Request Event API Information](https://developer.github.com/v3/activity/events/types/#pullrequestevent)
* [Emoji Cheat Sheet](http://www.emoji-cheat-sheet.com)

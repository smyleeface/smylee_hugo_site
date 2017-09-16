+++
title = "Basic Cognito"
date = "2016-06-17T21:00:00-07:00"
toc = true
draft = false
categories = ["Step-by-Step Guides"]
tags = ["AWS", "Cognito"]
+++

## Description
[AWS Coginto](https://aws.amazon.com/cognito/) is a user mangement tool for web and mobile applications. This project is a basic setup to get familiar with Cognito and the interface. It is meant to run for testing on localhost (or even file://) as passwords are sent in plaintext.
Shoutout to Robert for help in getting me started and sharing his html code.

## Tools Used in this Project
* Amazon Coginto
* My Github Project - [smylee_basic_cognito](https://github.com/smyleeface/smylee_basic_cognito)

## Coginto Setup
Note: Cognito is still in beta and at times the setup form can be a little flakey. Some values won't save even though it seems like it would. I will try to write this to minimize those distractions.

### Create a User Pool
1. Choose your region. Coginto is only avaliable in eu-west-1 (Ireland), ap-northeast-1 (Tokyo), and us-east-1 (N. Virginia).
1. Create a User Pool.
2. Enter a Name, then choose "Step through settings"
![Enter Name](/images/20160617-basiccognito/pool_name.png "Enter Name")

3. Choose email, name, phone, preferred username. Add a custom attribute of string, name "city".
BUT WAIT! This is one of the pages with a bug. When you try to continue (next step), it will not do anything. To "fix" this, mark the checkbox for preferred name > alias, uncheck, then go to next step.
![Attributes](/images/20160617-basiccognito/attributes.png "Attributes")

4. Password strength is completely up to you. Next step.
![Policies](/images/20160617-basiccognito/policies.png "Policies")

5. Leave MFA off, and mark the checkbox Phone Number. Change the text in the textboxes if desired. Next step.
According to the [docs](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools-settings.html?icmpid=docs_cognito_console#user-pool-settings-email-phone-verification) "If a user signs up with both a phone number and an email address, and both are selected for verification, the code is sent via SMS to the phone."
Texting charges to your phone will apply depending on your plan. Keep unchecked if desired.
![Verifications](/images/20160617-basiccognito/verifications.png "Verifications")

6. Add an app, enter a name, and uncheck Generate Client Secret. Create App. Copy App Client ID, you will need it later. Next Step.
![Which apps](/images/20160617-basiccognito/which_apps.png "Which apps")

7. Skip the triggers sections. Next step.
8. Your User Pool is created! Copy the Pool ID, you will need it later.
![Created Success](/images/20160617-basiccognito/created_success.png "Created Success")


### Create Federated Identities
1. Create new identity pool.
2. Add Identity pool name. Enable access to unauthenticated identities.
2. Add Authenitcation Providers > Coginto. Paste the User Pool ID and App Client ID copied from earlier.
2. Create Pool.<br>
![Create Identity pool](/images/20160617-basiccognito/create_new_identity_pool.png "Create Identity pool")

3. The IAM users page will appear. Keep the default settings and Allow.
4. Edit the newly created Identity Pool, and copy the Identity Pool Id for later.
![Edit Identity pool](/images/20160617-basiccognito/edit_identity_pool.png "Edit Identity pool")


## EDIT THE INDEX
1. Download or clone the data from: https://github.com/smyleeface/smylee_basic_cognito
2. Edit the index.html file and replace with your settings and copied data from earlier.
 * REGION
 * IDENTITY_POOL_ID
 * USER_POOL_ID
 * CLIENT_ID
3. Open the index.html file in a browser.

## TRY IT!
1. Create a new user.<br>
<img src="/images/20160617-basiccognito/create_new_user.png" class="imginitial" alt="Create a new user" title="Create a new user">

2. Verify user with code from email or text.<br>
<img src="/images/20160617-basiccognito/verify_user.png" class="imginitial" alt="Verify user" title="Verify user">

3. Login as user.<br>
<img src="/images/20160617-basiccognito/login_user.png" class="imginitial" alt="Login as user" title="Login as user">

4. Logout as user.<br>
<img src="/images/20160617-basiccognito/logout_user.png" class="imginitial" alt="Logout User" title="Logout User">

4. View user in Cognito.<br>
![Coginto User List](/images/20160617-basiccognito/user_list.png "Coginto User List")

## Extend
* Try adding a delete or other use cases to this. Lots of examples on the [AWS Coginto Identity JS Github](https://github.com/aws/amazon-cognito-identity-js#usage)

## Footnotes
* Phone number verification is only setup for US numbers in this sample code.

## AWS Costs for creating this project
* AWS provides a lot of services for free for the first 12 months of sign up and beyond. More information can be found on AWS pricing pages.
* Should be no cost to create this project, but if you did go over limits, should cost no more than $2.
* [AWS Cognito](https://aws.amazon.com/cognito/pricing/) - You pay based on your monthly active users (MAUs). This means if a user is inactive for the entire month, they will not be charged towards your count of MAUs. First 50,000 MAUs are free.
* [AWS SNS](https://aws.amazon.com/sns/pricing/) - Each month, Amazon SNS customers receive 1,000,000 Amazon SNS Requests, 100,000 HTTP notifications, 1,000 email notifications and 100 SMS notifications for free. [Per monthly calculator](http://calculator.s3.amazonaws.com/index.html)

## Resources
* [AWS Coginto Identity JS Github](https://github.com/aws/amazon-cognito-identity-js#usage)
* Robert's Brain ;) ... and files
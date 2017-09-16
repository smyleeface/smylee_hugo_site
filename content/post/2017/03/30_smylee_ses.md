+++
title = "Receiving smylee.com emails using AWS SES"
date = "2017-03-19T17:00:00-08:00"
toc = false
draft = false
categories = ["AWS"]
tags = ["Email", "AWS", "SES Rules", "S3", "SNS", "KMS"]
thumbnail = "/images/2017/03/smylee_com_ses_workflows_sm.png"
+++

I setup email receiving for patty at smylee.com using Amazon SES.

During this project I learned that in order to decrypt messaging using SES built-in encryption, you must decrypt using an `Encryption Client` available only in AWS SDK for Java and Ruby.
http://docs.aws.amazon.com/kms/latest/developerguide/services-ses.html#services-ses-decrypt

Because of this restriction, in this code, during the s3 event message to sqs phase, the lambda function encrypts the file at rest and removes the original.

## Email
- SES (RECEIVING) -> Send message to S3
- S3 -> Writes email file to raw directory in S3
- Lambda -> Encrypt the raw file, place into encrypted directory, deletes the original raw email file, and then sends a message to SQS.
- SQS -> Receives message and waits for something to poll it.

## Process Email in Message Queue
- CloudWatch Rule -> Triggers lambda function on schedule.
- Lambda -> Will poll the queue for any messages waiting to be processed. It will then decrypt the email in the encrypted directory, change the reply-to email and send the original email (minus the original sender) to the email specified in the lambda function.
- SES -> Send the email message
- Email appears in the email provided in the lambda function.

## Diagram

<img src="/images/2017/03/smylee_com_ses_workflows.png" alt="SES workflow for smylee.com" title="SES workflow for smylee.com">

## Steps

More information and steps to set this up can be found at: https://github.com/smyleeface/smylee_com_ses

## Miscellaneous
I also added an alarm if the SQS gets too large in a short period of time, it will trigger a CloudWatch alarm.
<img src="/images/2017/03/sqs_alarm_for_emails.png" alt="SQS Alarm for number of messages received" title="SQS Alarm for number of messages received">

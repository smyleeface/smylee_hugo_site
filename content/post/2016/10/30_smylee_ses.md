+++
date = "2016-10-15T17:00:00-08:00"
draft = false
title = "smylee.com emails using AWS"
categories = ["Step-by-Step Guides", "AWS"]
tags = ["Email", "AWS", "Route53", "Lambda", "IAM", "SES", "S3", "SQS", "KMS", "CloudWatch"]
toc = false
image = "201610/ses_smylee_com_workflow.png"
+++

AWS has the ability to receive emails for your domain, however, you must complete the processing after it is received.

After many hours of testing, I finally have patty(at)smylee(dot)com working and forwarding to my real email.

More information and setup can be found at:
https://github.com/smyleeface/smylee_com_ses

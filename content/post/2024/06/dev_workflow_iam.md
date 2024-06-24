+++

title = "Dev Workflow IAM"
description = "Setting up a simple username check so only authorized users can trigger the pipeline."
date = "2024-06-22T15:00:00-08:00"
toc = false
draft = false
mermaid = false
categories = ["Dev Workflow"]
tags = ["AWS", "Lambda"]
thumbnail = "https://cdn.smylee.com/images/2024/06/dev_workflow_iam_image_0.png"
+++


## IAM Access in S3

Using this as a guide:

* **DynamoDB**: Best for dynamic data with frequent updates and complex queries.
* **S3**: Best for simple storage needs, infrequent updates, and potentially larger data sets.
* **Secrets Manager**: Best for small, sensitive data that does not change frequently.

I decided to keep it simple and put the user list in a file on S3, the same S3 bucket that the lambda stores the GitHub events in.
Since my current use case of users is...me, it will not be updated frequently.

I created a simple text file and added it to the deploy script to upload it to the S3 bucket.

I had to add read permissions for the Lambda Function dispatcher.

It was pretty quick to integrate and can be switched out easily for other storage needs.

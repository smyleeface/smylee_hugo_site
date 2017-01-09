#!/bin/sh
echo "
[default]
aws_access_key_id = $ACCESS_KEY
aws_secret_access_key = $SECRET_KEY" >~/.aws/credentials
aws s3 rm s3://smylee.com.updates --recursive --region us-west-2

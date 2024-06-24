+++

title = "Lambda Debug Tips"
description = "Setting logging levels in Lambda functions without changing the code."
date = "2024-06-22T14:00:00-08:00"
toc = false
draft = false
mermaid = false
categories = ["Dev Tips", "AWS"]
tags = ["AWS", "Lambda", "Debug"]
thumbnail = "https://cdn.smylee.com/images/2024/06/lambda_debug_tips_image_0.png"
+++


## CloudWatch Logs from Lambda

In python, you can create your own logger. When using this logger it will print it to the CloudWatch logs defined in the lambda function.

However, you can set the logging level so it only print out certain logs as configured.

```python
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("hello world")
```

This will print "hello world" to the CloudWatch logs.

```python
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("hello world")
    logger.debug(event)
```

If I were to add the `logger.debug(event)` line, it will not print out the event to the CloudWatch logs because the logging level is set to `INFO`.

But we don't always want to change the code to change the logging level. We can set the logging level to an environment variable and provide a default to `INFO` level.

```python
logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGGING_LEVEL", logging.INFO))

def lambda_handler(event, context):
    logger.info("hello world")
    logger.debug(event)
```

Now the debug logs will only appear if the `LOGGING_LEVEL` environment variable is set to `DEBUG`.

In the Lambda Function configuration, you can set the `LOGGING_LEVEL` environment variable to `DEBUG` to see the debug logs.

![Lambda Environment Variable](https://cdn.smylee.com/images/2024/06/lambda_logging_level.png)

Remove the environment variable to go back to seeing only the `INFO` logs.

The logging level can be set to `DEBUG` or `ERROR` or `CRITICAL` or `WARNING` or `INFO`.

It is case-sensitive so make sure to use all caps.

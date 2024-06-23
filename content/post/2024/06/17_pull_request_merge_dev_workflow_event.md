+++

title = "Pull Request Merge Workflow Event"
description = "Setting up infrastructure to trigger a lambda function when a pull request is merged."
date = "2024-06-17T14:00:00-08:00"
toc = false
draft = false
mermaid = true
categories = ["Dev Workflow"]
tags = ["AWS", "Dev Workflow"]
thumbnail = "https://cdn.smylee.com/images/2024/06/17_pull_request_merge_dev_workflow_event_image_0.png"
+++


Hugo is [supported for deploy](https://gohugo.io/hosting-and-deployment/) on many platforms where this setup is not necessary.

But this is an application I can learn, understand how things work, and customize my own; and it's fun!

## Planning

In this phase, I'm going to plan and build out the CI/CD pipeline for when a pull request is merged to main it triggers a CodePipeline from a lambda function.

First, we'll add the pull reqeust merged event API to the Dev Workflow pipeline. Eventually, we'll update this to trigger CodePipeline.

1. GitHub event triggered (PR-merged)
1. Lambda Dispatcher
1. SNS Pull Request -- merged
1. Lambda Pull Request -- merged (Hello world logs)

Once that is complete, we'll break down these steps and get those working.

* :black_square_button: Setup CodeBuild
* :black_square_button: Setup CodePipeline
* :black_square_button: Setup Lambda Pull Request -- merged to trigger CodePipeline

## Working backwards

Since the foundation infrastructure is already in place, let's work backwards to implement the pull request merged function.

I'll be working from the [smylee-dev-workflows repo at this point in time](https://github.com/smyleeface/smylee-dev-workflows/tree/1f881175fbe2ef637e2f39f88120cfde59c3a81d).

### Lambda Pull Request -- merged

Fist I'll create the files that will be needed for the lambda function. It will simply log the event that triggers the lambda function.

![File structure of Pull Request Merged](images/2024/06/file_structure_prmerged.png)

```python
import logging
import os

logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGGING_LEVEL", logging.DEBUG))


def lambda_handler(event, context):
    logger.debug(event)

    return "done"
```

### Infrastructure to run Lambda Pull Request -- merged

Then I update the [infrastructure code](https://github.com/smyleeface/smylee-dev-workflows/blob/d98510881a663b3a951a27993f8f1be54c9ba125/infrastructure/function_pull_request_merged.py) to include the new lambda function and SNS topic.

Then I [updated the dispatcher](https://github.com/smyleeface/smylee-dev-workflows/blob/d3b8728ddfddbf4a89caf195aac2bca9ac97f637/functions/dispatcher/dev_workflow/dispatcher/dispatch_event.py) to look for this new event and sent a message to the Pull Request Merged SNS topic.

{{< mermaid >}}
flowchart TD
    A[GitHub]-->|/github_dispatcher endpoint|B[API Gateway]
    B-->|triggers|C[Lambda Dispatcher]
    C-->|sends message to|D[SNS PR Merged]
    D-->|triggers|E[Lambda PR Merged]
{{< /mermaid >}}

> :point_up: [Checkout this post on how to set up mermaid diagrams on hugo](https://navendu.me/posts/adding-diagrams-to-your-hugo-blog-with-mermaid/)!

So now the dispatcher knows how to send a message if it's pull request merge.

Next we'll set up Code Build to trigger and then do the hugo site updates when the PR is merged to main.

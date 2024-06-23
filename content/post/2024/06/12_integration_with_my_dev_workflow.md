+++
title = "s-MY-lee Dev Workflow Integration"
description = "Integrating my custom development workflow with my hugo_site repo"
date = "2024-06-12T13:00:00-08:00"
toc = false
draft = false
categories = ["Website", "Dev Workflow"]
tags = ["Website", "AWS", "Hugo", "Dev Workflow"]
thumbnail = "https://cdn.smylee.com/images/2024/06/dev_workflow_integration.png"
+++

For practice and fun, I created my own [custom development workflow](https://github.com/smyleeface/smylee-dev-workflows).

I had written one a while back, but it was not maintained and the infrastructure I used was too slow, so I'm slowly porting it to a different language and infrastructure.

So in the first port, of course is to scope creep and integrate some "AI" ooooo. ;)

## Flow

Currently, the GitHub app sends the PR open request to an API Gateway hooked up to a lambda function.

This lambda function verifies the payload signature and sends the request to the PR-open lambda function SNS topic.

The PR-open lambda function triggers, gets the commit messages from the PR on GitHub, and sends it to Bedrock for a summary.

It then subsequently posts the summary to the open PR on GitHub. 

![Smylee Dev Workflows Diagram](https://raw.githubusercontent.com/smyleeface/smylee-dev-workflows/wip/diagram.png)

I'll go into that project in another post.

## Adding the repo

Any repo in my account that has this GitHub app installed will trigger this process on an open PR.

So let's add the hugo_site repo and see what our latest summary will entail.

![AI Summary in a Pull Request Description](https://cdn.smylee.com/images/2024/06/ai-summary-pr-open.png)

If you notice the summary doesn't include the last 3 commits, and this is probably due to me truncating the commit list of characters to 200 because I don't want to pay too much for AI queries.

I should add it to remove the "chores" or the labels in the commit message.

To not have this automatic, it could be change into a comment command, which I might implement at another time.

But this is great because I don't have to write any descriptions and have a starting point if I want to modify.

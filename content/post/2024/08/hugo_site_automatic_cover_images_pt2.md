+++
title = "Hugo Website - Automatic Image Generator (Part 2)"
description = "Added a local CLI to run the same image generation process on my local machine."
date = "2024-08-01T14:00:00-08:00"
toc = false
draft = false
mermaid = true
categories = [ "Image Generator", "Website",]
tags = [ "AWS", "Hugo", "AI",]
thumbnail = "https://cdn.smylee.com/images/2024/08/hugo_site_automatic_cover_images_pt2_image_0_20240801182138.png"
+++


I'm a little ahead of myself as I have already added a command line to slack to show me the images,
but I did not like how I architected it, so I'm going to re-do it.

I didn't want to block myself and I want to run locally as much as possible, so I [refactored a bit](https://github.com/smyleeface/smylee_hugo_site_automations/pull/1) to
re-use the same code locally. I know it's a large pull request... :eyes:

This exercise was a good way to abstract the local needs (i.e. user GitHub token) vs the cloud needs (i.e. GitHub App Key).

I can also update the file with the image path from the command line as well. I used python package [click](https://click.palletsprojects.com/en/8.1.x/) to make the CLI.

These are building blocks that I can use in my Slack command, with the same codebase I run locally.

Additionally, it gives me a way to run and test the base application without having to deploy it to the cloud.

I can continue to add features and have multiple ways to run the application.
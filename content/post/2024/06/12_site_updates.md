+++
title = "How to do site updates"
description = "Notes about current workflow for updating this site."
date = "2024-06-12T12:00:00-08:00"
toc = false
draft = false
categories = ["Website"]
tags = ["Website", "AWS", "Hugo", "Bash"]
thumbnail = "https://cdn.smylee.com/images/2024/06/web_site_updates.png"
+++

## Manual deployment

For now I'm doing manual deployments of this site to understand the flow.

First I deleted the contents from the S3 bucket.

I tried using the `hugo deploy` command and it worked great!

In order to use it you have to [add configurations](https://gohugo.io/hosting-and-deployment/hugo-deploy/#advanced-configuration) to the `hugo.toml` file.

Some of these values are going to require some templating since I couldn't get environment variables to take and I don't want to hardcode those values. I will leave it uncommitted for now. 

Once deployed, I needed to clear the caches before I saw the changes.

While looking for something else, I found that adding the `cloudFrontDistributionID` to the hugo config will invalidate the caches for you whe using `hugo deploy`. 

## Image handling

I do not want to commit the images to the repo.

I have a cdn that will point to the images in a separate s3 bucket because I want the ability to wipe this site in the S3 bucket without having to re-upload all the images.

In the past I hard-coded the cdn URL, but it made local development weird because the images had to be uploaded first.

I could put in a condition in the theme and hardcode the url to the CDN, but the images on the post themselves would not reflect this, only the thumbnail.

I now realize that the easiest way to do this is to path rewrite on a Webserver. Which I'll consider for another time.

## Build script

This is the little build/deploy script I'm currently using locally to sync changes to the s3 bucket.

```bash
#!/bin/bash

hugo

# Sync the images to the S3 bucket
IMAGE_SYNC_COMMAND="aws s3 sync public/images s3://domain.com.assets/images"
$IMAGE_SYNC_COMMAND --exclude '/**/.DS_Store' --dryrun

read -p "Do you want proceed with IMAGE SYNC? (Y/y to continue): " user_input
if [[ "$user_input" == "Y" || "$user_input" == "y" ]]; then
    echo "Proceeding..."
    $IMAGE_SYNC_COMMAND --exclude '/**/.DS_Store'
fi

# Deploy the site
hugo deploy --dryRun
read -p "Do you want proceed with DEPLOY? (Y/y to continue): " user_input
if [[ "$user_input" == "Y" || "$user_input" == "y" ]]; then
    echo "Proceeding..."
    hugo deploy
fi
``` 

## Next Steps

I'd like to automate this a bit and not push changes directly to the live site, but from a pull request merge.

I could do this with a GitHub action, but for demonstration purposes, in this project I will continue using CodePipeline and CodeBuild.
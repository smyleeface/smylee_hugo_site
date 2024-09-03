+++
title = "I lost count"
date = "2024-06-12T11:00:00-08:00"
toc = false
draft = false
categories = ["Website"]
tags = ["Website", "AWS", "Hugo"]
thumbnail = "http://cdn.smylee.com/images/2024/06/i_lost_count.png"
+++
 
It's been over 5 years since I've done anything on this site. I've lost count of how many times I've started and stopped. But it was fun to go back and look at the posts.

## Site Resurrection

I didn't decommission too much of infrastructure, so it was easy to get the site back up and running.

First I re-activated the CDN and saw the images pop up on the Wayback Machine.

I tried to run the hugo site as-is locally.

It threw a bunch of errors due to my hugo config version being of `0.62`, and I had version `0.127` installed.

The theme I forked wasn't maintained and I didn't feel like debugging it, so I switched to a [new theme](https://github.com/CaiJimmy/hugo-theme-stack) that was well documented and simple to set up out the box.

After a few tweaks and it was alive again and ready to upload.

I deleted the `public` directory, ran `hugo` to generate the site files, and uploaded the files to the smylee.com s3 bucket.

The Cloudfront distribution was still active, so the site was live immediately.

![Website screenshot of smylee.com](https://cdn.smylee.com/images/2024/06/its_alive.png)

## New Learnings

I found there's (always been?) a [`hugo deploy`](https://gohugo.io/hosting-and-deployment/hugo-deploy/#deploy) command that does the same things as the `aws s3 cp public s3://bucket-name/ --recursive` command, however, it seems like it only deploys what is changed? There are also `confirm` and `dryRun` flags. Definitely will try these out!

Image handling needs to be reconfigured again for local development support. It was set up odd last time because I wanted the images to be served from a different domain.

In the past, I ended up using absolute URLs for images in the markdown files. I plan on revisiting this to take advantage of [hugo's image processing](https://gohugo.io/content-management/image-processing/).


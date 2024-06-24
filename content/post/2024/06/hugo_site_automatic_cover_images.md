+++

title = "Hugo Website - Automatic Image Generator"
description = "Generate cover images for new posts in a pull request. The images are automatically uploaded and the post is updated with the link."
date = "2024-06-23T14:00:00-08:00"
toc = false
draft = false
mermaid = true
categories = ["Image Generator", "Website"]
tags = ["AWS", "Dev Workflow", "Hugo", "CodeBuild"]
thumbnail = "https://cdn.smylee.com/images/2024/06/hugo_site_automatic_cover_images_image_0.png"
+++


When it comes to making cover images for my posts, I usually use an image that is already in the post or don't use one at all.

I don't really like to spend the time with images. I thought it would be fun to let AI generate an image for me, upload to the CDN, and automatically commit the changes to the pull request for review.

This is the workflow of the image generator:

![Image Generator Workflow](/images/2024/06/hugo_site_automatic_cover_image_generator.png)

I didn't really log my steps during development on this one, but one new thing I tried that my friend showed me recently, was using ChatGPT to generate the code.

I incrementally added features, and it was a fun way to develop.

![ChatGPT Writing Code](/images/2024/06/chatgpt_writing_code.png)

Code organization got a bit messy as I added more features, I tried to clean it up a bit.

Future plans include:

* generating more than one image and letting the user choose which image to use
* automatically updating the post with the date and time, so I don't have to remember
* automatically updating the categories (with pre-defined list) and tags (with a limit)
* automatically generate a description based on the post content (with a length limit)

I'm excited to finally use the image generation for something other than just testing. :smile:

I still don't have the auto deploy setup yet, but I'll get there.

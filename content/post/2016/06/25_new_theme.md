+++
title = "New Theme"
date = "2016-06-25T17:00:00-09:00"
toc = false
draft = false
categories = ["Site Update"]
tags = ["Hugo", "Lambda"]
image = "covers/newtheme.png"
+++

I finally got around to playing with Hugo Themes and making my own. I'm not a front-end developer and I wanted something very simple that didn't take too much time to make.

Used bootstrap and updated the colors and that's about it. I also updated the logo to change the blue eyes to brown, but I don't think the CDN has picked up the changes yet.

I have yet to make images for the posts, they will just stay the defaults for right now.

I did have a couple issues with updating the theme.

* When I pushed it up, the sidebar was not rendering. I updated Hugo to version .16 from .15 in Lambda and it worked fine after that.<br>(guess I should check the version, Robert :p).
* Found an <a href="https://github.com/spf13/hugo/issues/2198" target="_blank" rel="nofollow">issue with the new emoji feature and colons in the content</a> that was already reported but not yet fixed in the release version. Won't be using those for now.

I did have other issues, but they weren't as time consuming as those. When I was trying to get the emoji to work, I learned a new feature of Hugo, <a href="https://gohugo.io/extras/shortcodes/" target="_blank" rel="nofollow">shortcodes</a>.

There are some other things I want to add:

* category and tag when you hover over a post on the main page
* category and tag in the footer
* next/prev post from a page

But for now... I will get back to learning more AWS things. :)

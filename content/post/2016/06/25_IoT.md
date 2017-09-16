+++
title = "Internet of Things - Programmable Amazon Dash Button"
date = "2016-06-25T17:00:00-07:00"
toc = false
draft = false
categories = ["Tinkering"]
tags = ["AWS", "Lambda", "SNS", "Dash Button", "IoT"]
image = "covers/awsiotdash.png"
+++

I was curious about the programmable [Amazon IoT Dash Button](https://aws.amazon.com/iot/button/) and pre-ordered two buttons, thinking I might program one to give to my dad.

A few weeks ago it came in (three months earlier than expected) and went through their [tutorial](http://docs.aws.amazon.com/iot/latest/developerguide/iot-gs.html), which sends an email with a different subject based on how you clicked the button (single, double, long).

*It looks like they've updated that tutorial since, and will send you a text instead of an email.

<img src="/images/20160625-iot/emails.png">

Upon searching what you can do with this button, I found a [night light switch project](https://news.ycombinator.com/item?id=11688145) that sounded pretty cool, but upon continued reading, also learned that it will only last approximately 1000 clicks! That is very little for a development + use. [The battery is welded in](https://mpetroff.net/2015/05/amazon-dash-button-teardown/) and cannot be easily replaced. I was disappointed that was the case and for the price as well.

In the email I received, I notice it was sending the voltage reading, which went down with every click.

<img src="/images/20160625-iot/single.png">
<img src="/images/20160625-iot/double.png">
<img src="/images/20160625-iot/long.png">

The pre-programmed dash buttons that Amazon sells, the 1000 clicks isn't an issue because it will take a long time to reach. So I need to be sure what I decide to use this for will not require many clicks in a short period of time.

There are other ways to play with IoT. I have a [Wio Link](https://smile.amazon.com/WiFi-802-11-Development-Tools-Deluxe/dp/B01EJPCBTE/ref=sr_1_1?ie=UTF8&qid=1466918241&sr=8-1&keywords=wio+link) coming next week which will be a new tinkering project to mess with.

Until then, the button will sit around until I find something that will work with the 1000 click limit.

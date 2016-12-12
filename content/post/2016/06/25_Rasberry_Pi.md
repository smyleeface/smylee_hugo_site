+++
date = "2016-06-25T17:00:00-08:00"
draft = false
title = "Raspbuuuury Pi"
categories = ["Tinkering"]
tags = ["Raspberry Pi 3"]
toc = false
+++

I recently acquired a Raspberry Pi and brought it over to test it out with my dad.

It's very neat in that each SD card holds an image for what function you want. The card that mine came with had Raspbain installed. I was able to connect to the Internet and use their Web browser no problem!

We decided to install KODI to see what that's about. I used a <a href="//www.wirelesshack.org/how-to-install-kodi-on-a-raspberry-pi-3.html" target="_blank" rel="nofollow">guide to install KODI</a>, but was using a MAC and skipped some of the steps. Additionally, I skipped installing an image writer and went command line to write the image.

Some issues I did come across

* I downloaded the "Update File" instead of the "DiskImage". Yeah.
* One tutorial told me to use "bs=4M" in the command line, which would return the error `invalid number '4M'`. I tried 1M also and ended up working using `bs=1m`.
* I used the wrong disk name, out disk name was /dev/disk4 (for /dev/disk4s1) but should be mounted with /dev/rdisk4

Following some of these <a href="//www.raspberrypi.org/documentation/installation/installing-images/mac.md" target="_blank" rel="nofollow">image writing steps</a> were nice because the examples were the exact same thing we had on our system.

Quick Steps

* Format SD Card
* From terminal
	* diskutil list
	* diskutil unmountdisk < /dev/disk4 >
	* cd < to where your image is located >
	* sudo dd bs=1m if=< name of image >.img of=< /dev/rdisk4 >
* Put the SD Card in the Pi and boot!

Overall it didn't take very long, maybe a couple hours total. The longest part was the formatting of the SD card because I didn't choose to quick format. :blush:
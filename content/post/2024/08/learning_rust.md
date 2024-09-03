+++
title = "Learning Rust"
description = "I wrote a quick application to learn Rust. Here's how it went..."
date = "2024-08-31T15:00:00-08:00"
toc = false
draft = false
mermaid = false
categories = [ "Programming",]
tags = [ "development", "rust", "study",]
thumbnail = "https://cdn.smylee.com/images/2024/08/learning_rust_image_0_20240903200546.png"
+++


I was recently presented a challenge to write a small application in Rust.

I've heard a bit about Rust and how it's shot up in the [tiobe index](https://www.tiobe.com/tiobe-index/).

So I took the course "Rust 2021 Fundamentals" by Zachary Bennett on [PluralSight](https://app.pluralsight.com/library/courses/rust-2021-fundamentals/table-of-contents) and whipped up [RustyFileNinja](https://github.com/smyleeface/RustyFileNinja). This application will create, copy, combine, and delete files.

It was a bit of a challenge to grasp some of the Rust terms. I tend to map it to existing programming languages. (Are Rust traits like Python classes?)

There are some default patterns not typically set in most languages I've worked in. For example, all variables are immutable by default and are disposed of after use; when are things in the heap vs the stack. I still need to get a handle on `match` and the `Ok()`, `Err()` functionalities, among many other things. :sweat_smile:

Also need to refactor the code to use dependency injection, so I can write proper tests.

This project was a many first for me. Not only was this my first time writing a Rust application, it was also my first time setting up an install/uninstall script. It also has a release pipeline, which I've made before, but my first time using github-actions and GitHub's release feature.

![rustyfileninja.png](https://cdn.smylee.com/images/2024/08/rustyfileninja.png)

![rustfileninja_uninstall.png](https://cdn.smylee.com/images/2024/08/rustfileninja_uninstall.png)
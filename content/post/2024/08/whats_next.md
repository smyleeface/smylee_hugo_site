+++
title = "What's Next"
description = "What project I want to work on next with a little rant about development environments."
date = "2024-08-02T15:00:00-08:00"
toc = false
draft = false
mermaid = false
categories = [ "Random",]
tags = [ "development", "python", "workflow",]
thumbnail = "https://cdn.smylee.com/images/2024/08/whats_next_image_0_20240903200553.png"
+++


Now that I have a stable codebase for my development workflow, I need to get some pipelines in place for deployment because deploying by hand is not fun.

It's crazy how many things you need for each programming language and your application.

I'm trying to get deeper into python and all these tools I need to set up:

* version management (asdf)
* packages and dependencies (pip, poetry)
* virtual environments (python -m venv)
* testing (pytest)
* linting (flake8, pylint)
* formatting (black)
* IDE configuration (setup pylint, flake8, black)
* coverage (coverage.py)
* documentation (sphinx)
* deployment environment* (docker)
* deployment (github actions)
* observability (grafana, prometheus, jaeger, opentelemetry)

> You may be able to use pre-built docker images for your environment, but quickly realize you need more things installed.

And for every language, you have similar tools and environments you want to set up.

Additionally, any new projects will need these too.

Speaking of new projects, I always struggle on how to set up the project structure.

In writing this, the bot autocomplete recommended [cookiecutter](https://cookiecutter.readthedocs.io/en/stable).

Maybe this will help in the future when I start a fresh project.

For personal projects, we get away with skipping tests, linting, and documentation for the sake of getting it to work.

We're the only ones working on it, so it doesn't matter. Right? I still like to best practice as much as I can, for my future self.

Plus when it's working well, it's pretty sweet. :sunglasses:

Whew, now that all that is set up it's time to actually write code!

But there's actually TWO sets of code that needs to be maintained.

The actual app code and infrastructure code.

The app and infrastructure code also needs observability support (logging, metrics, tracing), terraform, etc.

And now you have platform issues.

On but wait, there's more!

There's THREE sets of code that needs to be maintained.

The actual app code, infrastructure code, and the deployment code.

This becomes very overwhelming when you all you want to do is focus on making fun features and making it available on the internet.

Especially when you feel like you're writing the same code over and over again.

I could use pre-built solutions, but I don't know what I need and what works for me in the long run yet.

I had my development flow once, but after a few years of letting it by, it was already in shambles.

And this is a problem with work environments too, we all find our own way of executing things when there's no defined easy repeatable way.

I've been finding my development flow again. But I do tend to over-engineer and scope creep. :sweat_smile:

One thing I have to remember is to keep it simple.

So what's next?

:white_check_mark: Update my "[business card](https://meet.pattyr.dev)"
<br>
:white_medium_square: Observability for my projects.
<br>
:white_medium_square: Finish the playlist monitor (I'm about 50% complete, but I'll probably end up refactoring much of it with some of the things I've been learning in the python course. :sweat_smile:)
<br>
:white_medium_square: Update my blog and portfolio page.

And add automation as needed. :robot:
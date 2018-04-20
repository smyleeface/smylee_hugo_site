+++
title = "Managing Projects and Ideas"
date = "2018-03-14T11:00:00-08:00"
toc = false
draft = false
categories = ["Notes"]
tags = ["Organization", "Projects", "ZenHub", "GitHub", "Repositories"]
+++

Occasionally I'll think of shiny projects and start chasing them or try to remember them for later. Now when I think of something, I'll put it in my project repository.

## Project Repository
I'm using a single repository to manage all the projects and ideas to backlog and track. The single repo allows my projects that span across different platforms to have single source of management.

Another benefit is the ability to [customize the issue template](https://help.github.com/articles/creating-an-issue-template-for-your-repository/).

## ZenHub
My co-worker found ZenHub and we started evaluating it at work. I liked it so much I decided to try it out for personal use. Slowy adopting it but would like to start configuring it for real use. For example, I have a project I've built for my parents and if they have problems with it, they can create an issue in GitHub and I'll get it. :smile:

They have a great set of [guides](https://www.zenhub.com/guides) that I used for reference.

### Hide GitHub Projects (optional)
I was having a hard time understanding the use of managing both Projects and the ZenHub board. [This article helped me understand why they discontinued support for projects in Zenhub and the difference between the two.](https://www.zenhub.com/blog/dispatches-from-github-universe/) and why I think GitHub projects should be disabled (in your project management repository settings). The article doesn't mention they have similar functionalities, but the UI and workflow ZenHub provides surpasses GitHub's Projects board.

> Without ZenHub, your GitHub issues lack hierarchy; they’re simply a list. There’s no clear indicator of which issues are related and where the dependencies lie. ZenHub’s Epics add this crucial layer of hierarchy. [\[Source\]](https://www.zenhub.com/guides/getting-started-with-epics-in-zenhub)

## Organization

If you're familiar with agile story boarding, GitHub has equivient features in their system.

| Agile      | GitHub             |
|------------|--------------------|
| Epic       | Epic               |
| User Story | GitHub Issue       |
| Sub-Task   | Markdown Checklist |

### Epic
Epics are a items that will take longer than just a sprint and should be broken down into smaller chunks.
> Epics contain Issues related in subject, and the scope is flexible. [Source\]](https://www.zenhub.com/guides/getting-started-with-epics-in-zenhub)

### Issues
Issues should be completed in the smallest amount of time possible and are usually tied to an Epic.

### Checklist
Individual tasks needed to complete the issue

### Milestones
In GitHub, Milestones = sprints
> ...milestones are tied to sprints, they contain Issues related by time, and not necessarily related by subject. [\[Source\]](https://www.zenhub.com/guides/getting-started-with-epics-in-zenhub)

### Estimate
This tracks about how much time it would take to complete an issue in points. It's used to determine which issues could be compeleted and put into a milestone. The total estimate of all issues in an epic is Epic points.

### Releases
Release are a snapshot of your code at specific place in time, usually packaged and ready software for users to download.

### Labels
Labels help identify the type of work that the issue encompasses. Does it need research, is it bug, enhancement, etc.

## GitHub Repositories
If working on specific projects that has a repository or organization on GitHub, adding the repo through ZenHub will display issues from there. This lets you manage not just regular projects, but specific issues side-by-side with your code.

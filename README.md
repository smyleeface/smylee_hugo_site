
[![Build Status](https://travis-ci.org/smyleeface/smylee_hugo_site.svg?branch=master)](https://travis-ci.org/smyleeface/smylee_hugo_site)
[![StackShare](https://img.shields.io/badge/tech-stack-0690fa.svg?style=flat)](https://stackshare.io/smyleeface/smylee-com)

# smylee_hugo_site

* The content for my hugo site.
* Theme [hugo_theme_beg](https://github.com/smyleeface/hugo_theme_beg) (forked)

## Run Hugo Server (Daemon)

```bash
docker run --rm -itd -v $PWD:/smylee_com -p 1313:1313 --name smylee_hugo_site smylee_com_hugo hugo server -b http://localhost:1313 --bind 0.0.0.0 --theme beg --disableFastRender
```
```bash
docker stop smylee_hugo_site
```

## Run Hugo and Generate Site Files

```bash
docker run --rm -it -v $PWD:/smylee_com --name smylee_hugo_site smylee_com_hugo hugo --theme beg
```

## Updating ECR smylee_com_hugo

```bash
eval $(aws ecr get-login --no-include-email) && \
docker build -t smylee_com_hugo -f Dockerfile.build . && \
docker tag smylee_com_hugo:latest 952671759649.dkr.ecr.us-west-2.amazonaws.com/smylee_com_hugo:latest && \
docker push 952671759649.dkr.ecr.us-west-2.amazonaws.com/smylee_com_hugo:latest
```

## Deploy Pipeline

![Smylee.com Deploy Pipeline](https://user-images.githubusercontent.com/8292341/36361300-c16c26fa-14df-11e8-9027-bcf09ffbc977.png "Smylee.com pipeline")


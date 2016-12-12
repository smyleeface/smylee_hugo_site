+++
date = "2016-06-20T21:00:00-07:00"
draft = true
title = "VPC"
categories = ["Review"]
tags = ["AWS", "VPC"]
toc = true
+++

## Description
Reviewing VPC setup from the [acloud.guru](acloud.guru) videos.

http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html
https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#IPv4_CIDR_blocks

## Create VPC
Choose a CIDR (/##) that corresponds to the number
CIDR Block: 10.0.0.0/22 (1,024 IPs)

## Subnets
subnet-a: 10.0.1.0/24 (256 IPs)
subnet-b: 10.0.2.0/25 (128 IPs)
subnet-b: 10.0.2.128/25 (128 IPs)
subnet-c: 10.0.3.0/24 (256 IPs)

## Internet Gateway
Create and attach to VPC. Only one IG per VPC allowed.

## Route Table
* Create a new route table.
* Edit the Routes and add new route:
	* destination: 0.0.0.0/0
	* target: <Internet Gateway created above>
* Edit Subnets Associations and add the subnet that you want to access the Internet. (A Subnet Association can only be attached to one route table.)

## Notes
* Security Groups can be reused across different subnets and availability zones.
* A subnet cannot go across availability zones.

## What does AWS do with those reserved IPs in each subnet?
According to their [docs](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html#SubnetSize)

* first: Network address.
* second: Reserved by AWS for the VPC router.
* third: Reserved by AWS for mapping to the Amazon-provided DNS.
* fourth: Reserved by AWS for future use.
* last: Network broadcast address. We do not support broadcast in a VPC, therefore we reserve this address.
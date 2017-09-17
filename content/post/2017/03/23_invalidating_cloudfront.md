+++
title = "Purging CloudFront Caches"
date = "2017-03-24T17:00:00-08:00"
toc = false
draft = false
categories = ["Step-by-Step Guides", "AWS"]
tags = ["AWS", "CloudFront", "S3"]
thumbnail = "http://cdn.smylee.com/images/2017/03/cloudfront.png"
+++

I had a image uploaded that had some information I didn't mean to post. I made the change but it was already cached in CloudFront.
 
To remove it so it will pickup the updated image, I had to invalidate it (Web Distributions only).

First I had to create a .json file with the path to the image in the bucket:

```
{
  "Paths": {
    "Quantity": 2,
    "Items": [
        "/YOUR/PATH/TO/THE/FILE/IN/S3.jpg",
        "/YOUR/OTHER/PATH/TO/THE/FILE/IN/S3/*"
    ]
  },
  "CallerReference": "removing image with info"
}
```

Then run this command line with the CloudFront distribution id and the path to the .json file:

```
aws cloudfront create-invalidation --distribution-id <DISTRIBUTION ID> --invalidation-batch file://<YOUR/PATH/TO/THE/FILE>.json
```

I read it takes anywhere to 5-30 min for the propigation to complete but it worked!
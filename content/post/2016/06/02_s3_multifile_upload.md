+++
date = "2016-06-02T17:20:47-07:00"
draft = false
title = "S3 Multifile Upload with Evaporate"
+++

So now that my site is using Hugo for static HTML file generation, S3 to store the files, lambda to trigger the Hugo update, and CloudFront to serve images, the next step is to upload files to S3 directly from the browser.
Thanks to my buddy Robert, he got me started and helped me get the API Gateway setup.

* HTML page with input type of file with [evaporate](https://github.com/TTLabs/EvaporateJS). Include the aws_key, bucket: and aws_url.

* Update the signer.py function with the user arn and secret.

* Add the signer to a new lambda function.

* Add the timer to a new lambda function.

* Add a new API Gateway or add to existing

* Create a new Resource for the signer.

* Create a new Method GET for the signer for the signer lambda function.

* In the GET Method Request, add a URL Query String Parameters for "to_sign".
   
* In The GET Integration Request > Body Mapping Template for application/json, add the code

```
#set($keys = [])
#foreach($key in $input.params().querystring.keySet())
  #set($success = $keys.add($key))
#end

#foreach($key in $input.params().headers.keySet())
  #if(!$keys.contains($key))
    #set($success = $keys.add($key))
  #end
#end

#foreach($key in $input.params().path.keySet())
  #if(!$keys.contains($key))
    #set($success = $keys.add($key))
  #end
#end

{
#foreach($key in $keys)
  "$key": "$util.escapeJavaScript($input.params($key))"#if($foreach.hasNext),#end
#end
}
```
  
* In the GET Integration Response, Change the Header Mapping(?), change the Body    Mapping Templates to only "text/html" and for the "text/html" add the code
   
```
#set($inputRoot = $input.path('$'))
$input.path('$')
```

* In the GET Method Response, change the "Response Models for 200" to only "text/html".

* Enable CORS for the Method GET signer. Change Access-Control-Allow-Origin for the domain you're using or '*'.

* Create a new Resource for the timer.

* Create a new Method GET for the timer for the timer lambda function above

* Enable CORS for the Method GET timer. Change Access-Control-Allow-Origin for the domain you're using or '*'.

* Deploy the API and add the API endpoints to the HTML page.

* In the S3 bucket that the file will be uploaded to, add the bucket policy:

```
{
    "Version": "2012-10-17",
    "Id": "Policy145337ddwd",
    "Statement": [
        {
            "Sid": "",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::6681765859115:user/me"
            },
            "Action": [
                "s3:AbortMultipartUpload",
                "s3:ListMultipartUploadParts",
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::mybucket/*"
        }
    ]
}
```

* In the S3 bucket that the file will be uploaded to, add the CORS Configuration:

```
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <CORSRule>
        <AllowedOrigin>*</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <MaxAgeSeconds>3000</MaxAgeSeconds>
        <AllowedHeader>Authorization</AllowedHeader>
    </CORSRule>
    <CORSRule>
        <AllowedOrigin>https://*.yourdomain.com</AllowedOrigin>
        <AllowedOrigin>http://*.yourdomain.com</AllowedOrigin>
        <AllowedMethod>PUT</AllowedMethod>
        <AllowedMethod>POST</AllowedMethod>
        <AllowedMethod>DELETE</AllowedMethod>
        <AllowedMethod>GET</AllowedMethod>
        <ExposeHeader>ETag</ExposeHeader>
        <AllowedHeader>*</AllowedHeader>
    </CORSRule>
</CORSConfiguration>
```

* Upload an image and it should load into the S3 bucket.

* Next I will use this to upload images and content files to the buckets, which will trigger an update to the site without having to login to the AWS console.
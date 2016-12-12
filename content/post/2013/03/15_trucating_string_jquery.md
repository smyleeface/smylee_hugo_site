+++
date = "2013-03-15T21:00:00-07:00"
draft = false
title = "Truncating a String with JQuery"
categories = ["Coding"]
tags = ["Drupal", "JQuery"]
toc = false
+++

<p>For some reason Drupal's views + services + rest output doesn't truncate the body text even when it's set to trim. I couldn't find a quick fix or anyone else having the same problem so I found a <a href="http://stackoverflow.com/questions/4637942/how-can-i-truncate-a-string-in-jquery" target="_blank">Stackoverflow&nbsp;page</a> with a convienent jQuery&nbsp;code snippet to truncate. Changed the substring number from characters to 450 characters and this is the code I ended up with:</p>

```
var node_body = data[key].node_data_field_body_field_body_value;
node_body = $.trim(node_body).substring(0, 450).split(" ").slice(0, -1).join(" ") + "...";
```
<p>Worked great!</p>  
# DSParams Delete Command

# Purpose

Reads a DSParams diff file and removes matching values from a DSParams
file.

# Syntax

<img src="attachments/458556054/2281472001.png?width=340"
class="image-center" loading="lazy"
data-image-src="attachments/458556054/2281472001.png" data-height="211"
data-width="741" data-unresolved-comment-count="0"
data-linked-resource-id="2281472001" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20220816-235220.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="458556054"
data-linked-resource-container-version="14"
data-media-id="d669610a-7332-4c65-a040-32871268bab9"
data-media-type="file" width="340" />

# Example

``` bash
$> mettleci dsparams delete \
   -before ./DSParams \
   -delete ./DSParams_delete \
   -after ./DSParams_new
```

  

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220816-235220.png](attachments/458556054/2281472001.png)
(image/png)  

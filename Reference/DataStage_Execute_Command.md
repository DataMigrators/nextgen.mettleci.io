# DataStage Execute Command

# Purpose

Execute a DataStage job.

# Syntax

<img src="attachments/458817755/2233041004.png" class="image-center"
loading="lazy" data-image-src="attachments/458817755/2233041004.png"
data-height="323" data-width="1266" data-unresolved-comment-count="0"
data-linked-resource-id="2233041004" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20220617-104917.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="458817755"
data-linked-resource-container-version="15"
data-media-id="346a989a-80ed-4255-acde-445ed4c10d13"
data-media-type="file" />

# Example

``` bash
$> mettelci datastage execute \
   -domain test1-svcs.datamigrators.io:59445 \
   -server test1-engn.datamigrators.io \
   -username isadmin -password password1 \
   -project dstage1 \
   -jobname TR_ORDERS \
   -runmode NORMAL
```

  

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220617-104917.png](attachments/458817755/2233041004.png)
(image/png)  

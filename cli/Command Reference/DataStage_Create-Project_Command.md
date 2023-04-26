# DataStage Create-Project Command

# Purpose

This command either creates a DataStage project in a nominated
environment or simply exist with a success code if the DataStage project
already exists. It is used frequently at the beginning of pipelines to
<a href="https://en.wikipedia.org/wiki/Assertion_(software_development)"
rel="nofollow">assert</a> that a target environment with which the
pipeline will deploy and execute code is present and available.

# Syntax

<img src="attachments/408420417/2233041015.png" class="image-center"
loading="lazy" data-image-src="attachments/408420417/2233041015.png"
data-height="288" data-width="1184" data-unresolved-comment-count="0"
data-linked-resource-id="2233041015" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20220617-105608.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="408420417"
data-linked-resource-container-version="33"
data-media-id="3ab78eb3-b352-4873-8769-64d1e523690c"
data-media-type="file" />

# Example

``` bash
$> mettleci datastage create-project \
   -domain service_tier.datamigrators.io:59445 \
   -username isadmin -password mypassword \
   -server engine_tier.datamigrators.io \
   -project Test4

Test4 created successfully.
$>
```

## Usage Notes

Due to a known issue with the DataStage `dsadmin` command itself it is
not possible to distinguish between…

-   a DataStage project that already exists, and

-   a DataStage project that doesn’t exist in the DataStage repository,
    but for which the associated filesystem directories does exist.

There may be some situations in which this causes the `create-project`
command to fail.

When faced with an inexplicable failure of this nature check to see if
the project’s directory structure already exists on the filesystem. If
so, and it’s safe to do so, remove the file structure and try again

------------------------------------------------------------------------

# See also

-   <a
    href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/1791197232"
    rel="nofollow">The `mettleci datastage create-project` command fails</a>

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-10-3_14-6-14.png](attachments/408420417/454852960.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-10-3_14-8-55.png](attachments/408420417/455311489.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-10-3_14-10-44.png](attachments/408420417/454852965.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220617-100637.png](attachments/408420417/2232975396.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220617-105608.png](attachments/408420417/2233041015.png)
(image/png)  

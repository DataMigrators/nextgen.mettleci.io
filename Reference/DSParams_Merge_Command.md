# DSParams Merge Command

# Purpose

Creates a new DSParams file from an existing DSParams file and merging
it with the provided diff file.

# Syntax

<img src="attachments/458556064/2280882184.png" class="image-center"
loading="lazy" data-image-src="attachments/458556064/2280882184.png"
data-height="211" data-width="733" data-unresolved-comment-count="0"
data-linked-resource-id="2280882184" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20220816-095731.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="458556064"
data-linked-resource-container-version="17"
data-media-id="46c20a8c-a885-44ba-b717-586f46202ac4"
data-media-type="file" />

# Example

``` bash
$> mettleci dsparams merge \
   -before .\DSParams \
   -diff .\DSParams_diff \
   -after .\DSParams_new 
   
MettleCI Command Line (build ${buildNumber})
(C) 2018-2020 Data Migrators Pty Ltd
Merging differences from .\DSParams_diff (-diff) into .\DSParams (-before), to create .\DSParams_new (-after)
Comparing section PROJECT...
Section present in -before. Adding entries...
JobAdminEnabled=0
…
Differences added
Comparing section EnvVarValues...
Section not present in -before. Adding entire section.
Merge complete. Writing merged DSParams to .\DSParams_new (-after)
```

  

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220816-095731.png](attachments/458556064/2280882184.png)
(image/png)  

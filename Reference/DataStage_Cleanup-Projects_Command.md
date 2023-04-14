# DataStage Cleanup-Projects Command

# Purpose

Deletes redundant DataStage projects matching a supplied pattern.

## Syntax

<img src="attachments/458424418/2233040967.png" class="image-center"
loading="lazy" data-image-src="attachments/458424418/2233040967.png"
data-height="327" data-width="1241" data-unresolved-comment-count="0"
data-linked-resource-id="2233040967" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20220617-104041.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="458424418"
data-linked-resource-container-version="14"
data-media-id="2e0dbba1-b79b-420e-bae6-199f3c08eb73"
data-media-type="file" />

# Example

``` bash
$> mettleci datastage cleanup-projects \
   -domain my-services.datamigrators.io:59445 \
   -username isadmin \
   -password isadminpwd \
   -server my-engine.datamigrators.io \
   -pattern Test[0-9] \
   -retain 1
Listing projects:
  - ANALYZERPROJECT
  - DataClick
  - dstage1
  - Test1
    - matches pattern
  - Test2
    - matches pattern
  - Test4
    - matches pattern
  - SWPensionStrategy
  - wwi_prod
Cleaning up old projects, retaining 1 most recent projects
 * Delete 'test2-engn.datamigrators.io/Test4' - SKIPPED
Deleting project: SNTest2
 * Delete 'test2-engn.datamigrators.io/Test2' - COMPLETED
Deleting project: SNTest1
 * Delete 'test2-engn.datamigrators.io/Test1' - COMPLETED
```

  

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-10-3_14-10-44.png](attachments/458424418/458424421.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-10-3_14-8-55.png](attachments/458424418/458424424.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-10-3_14-6-14.png](attachments/458424418/458424427.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220617-104001.png](attachments/458424418/2232647762.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220617-104041.png](attachments/458424418/2233040967.png)
(image/png)  

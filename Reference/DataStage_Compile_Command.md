# DataStage Compile Command

# Purpose

Compiles a DataStage Job producing a jUnit-compatible testing output
that can be utilised by built tools orchestrating a CI/CD pipeline.

This command produces a
<a href="JUnit_Test_Results" data-linked-resource-id="1754890299"
data-linked-resource-version="7"
data-linked-resource-type="page">JUnit-compatible</a> XML file called
`mettleci_compilation.xml` which reports each individual job’s
compilation result.

This command is also incorporated into the `mettleci datastage ccmt`
command (<a href="DataStage_Connector_Migration_Command"
data-linked-resource-id="410681364" data-linked-resource-version="23"
data-linked-resource-type="page">documentation here</a>).

# Syntax

<img src="attachments/410157081/2227109925.png?width=544"
class="image-center" loading="lazy"
data-image-src="attachments/410157081/2227109925.png" data-height="290"
data-width="1327" data-unresolved-comment-count="0"
data-linked-resource-id="2227109925" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20220609-083011.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="410157081"
data-linked-resource-container-version="33"
data-media-id="cc4a5324-b8b1-4eb9-b98b-c7493be6aa84"
data-media-type="file" width="544" />

# Example

``` java
$> mettleci datastage compile \
   -domain service_tier.datamigrators.io:59445 \
   -username isadmin \
   -password mypassword \
   -server engine_tier.datamigrators.io \
   -project dstage1 \
   -include-job-in-test-name
Analyzing assets to compile
Compilation folder location = C:\Apps\command-shell\log\compiliation
Attempting to compile with 4 working threads.
Compiling DataStage jobs...
 * Compile 'engine_tier.datamigrators.io/dstage1/Jobs/Load/LD_STOCKITEM.pjb' - COMPLETED
 * Compile 'engine_tier.datamigrators.io/dstage1/Jobs/Load/LD_SALE.pjb' - COMPLETED
 * Compile 'engine_tier.datamigrators.io/dstage1/Jobs/Load/LD_SUPPLIER.pjb' - COMPLETED
 * Compile 'engine_tier.datamigrators.io/dstage1/Jobs/Load/LD_STOCK_HOLDING.pjb' - COMPLETED
Compilation complete
```

  

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-10-3_13-38-3.png](attachments/410157081/454852934.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-10-3_13-59-30.png](attachments/410157081/455213125.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-10-3_13-59-55.png](attachments/410157081/455245970.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2020-1-2_15-46-18.png](attachments/410157081/488898601.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220609-014508.png](attachments/410157081/2226880517.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220609-015003.png](attachments/410157081/2224390303.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220609-083011.png](attachments/410157081/2227109925.png)
(image/png)  

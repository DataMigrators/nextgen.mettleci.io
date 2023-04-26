# QualityStage Rulesets Ignore Incremental Compilation

# Problem

<a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/1266843717/Repeatable+DataStage+Project+Deployments"
data-linked-resource-id="1266843717" data-linked-resource-version="8"
data-linked-resource-type="page">Incremental deployment</a> of files
from the standard <a
href="https://www.ibm.com/docs/en/iis/11.7?topic=job-standardize-rule-sets"
rel="nofollow">QualityStage Standardisation Rule Sets</a> will take
longer than expected to deploy and compile. This will be apparent by the
deployment logs indicating that all of the QualityStage asset (`.dqs`)
files are being imported and compiled despite the fact that no changes
have been made to them by a user.

# Cause

**In summary, previous exports and imports of those files using a**
`.dsx` **file format will alter the way in which the** `istool` **export
process treats those file. Specifically, . and how it differs from
Information Server Manager and** `istool` **methods in relation to the
out-of-the-box Standardisation Rules.**

Consider the following example from a project called `DQSTest`… **

When performing an `.isx` export using `istool` on a new DataStage
project, all unmodified QualityStage-related files are considered to be
non-exportable objects.

<img src="attachments/2298511407/2299756545.png?width=442"
class="image-center" loading="lazy"
data-image-src="attachments/2298511407/2299756545.png" data-height="261"
data-width="452" data-unresolved-comment-count="0"
data-linked-resource-id="2299756545" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="DQS1.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="2298511407"
data-linked-resource-container-version="9"
data-media-id="ee77222a-f9ff-431a-b372-58fa1d36c26f"
data-media-type="file" width="442" />

This not only includes the read-only files such as Pattern Action
(`.pat`) and Classification (`.cls`) files, but editable files such as
Text Override (`.ito` / `.uto`), Pattern Override (`.ipo`/ `.upo`) and
Rule Set Extension (`.rcm` / `.rcr`) files.

<img src="attachments/2298511407/2299101189.png" class="image-center"
loading="lazy" data-image-src="attachments/2298511407/2299101189.png"
data-height="610" data-width="452" data-unresolved-comment-count="0"
data-linked-resource-id="2299101189" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="DQS2.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="2298511407"
data-linked-resource-container-version="9"
data-media-id="c6a0b7ec-9d55-4efa-b7d3-cb5ff5ba5200"
data-media-type="file" />

When exporting assets using the DataStage `.dsx` export function,
however only the read-only files are excluded, allowing the editable
files listed above to be exported as part of the `.dsx` archive.

<img src="attachments/2298511407/2299133961.png?width=442"
class="image-center" loading="lazy"
data-image-src="attachments/2298511407/2299133961.png" data-height="320"
data-width="452" data-unresolved-comment-count="0"
data-linked-resource-id="2299133961" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="DQS3.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="2298511407"
data-linked-resource-container-version="9"
data-media-id="875db01a-5d8e-41ca-bdf4-123f468dd658"
data-media-type="file" width="442" />

Re-importing that `.dsx` archive into DataStage modifies the internal
properties of the editable Standardisation Rule Set files so that they
are now treated as **exportable** when generating an `isx` file using
`istool`.

<img src="attachments/2298511407/2299756551.png?width=442"
class="image-center" loading="lazy"
data-image-src="attachments/2298511407/2299756551.png" data-height="255"
data-width="452" data-unresolved-comment-count="0"
data-linked-resource-id="2299756551" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="DQS4.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="2298511407"
data-linked-resource-container-version="9"
data-media-id="515640f9-3315-4047-9969-5b79bbfae2d0"
data-media-type="file" width="442" />

If those files are exported as part of the MettleCI ‘golden copy’ source
repository, and any subsequent deployments will exhibit the observed
behaviour:

-   The incremental deployment process takes an `istool` preview of the
    target project, and does not list the out-of-the-box QualityStage
    assets.

-   The golden copy contains those out-of-the-box QualityStage assets,
    so they are deemed to be new assets to be imported into the target
    project.

-   Those assets are again imported and compiled, unnecessarily
    consuming valuable time and resources.

Even though these out-of-the-box assets have now been imported into the
target project using the `istool` method, the `istool` method does not
modify the internal properties of those assets in the same way as the
DataStage `.dsx` import process, **so the next time a deployment occurs,
those assets are still not included in the** `istool` **preview, and
will still trigger a full import and compilation**.

Now consider an example project `DQSTest2`, which is the project the
`.isx` extract featuring the problematic QualityStage assets is being
deployed (where assets are imported using `istool` prior to
compilation).

<img src="attachments/2298511407/2298806379.png?width=442"
class="image-center" loading="lazy"
data-image-src="attachments/2298511407/2298806379.png" data-height="245"
data-width="452" data-unresolved-comment-count="0"
data-linked-resource-id="2298806379" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="DQS5.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="2298511407"
data-linked-resource-container-version="9"
data-media-id="1684a842-25a1-44b1-a97f-49d70ac3a764"
data-media-type="file" width="442" />

Note that, even after import of the assets, the next `istool` preview
will still not show them, so subsequent deployments will not fix the
issue.

<img src="attachments/2298511407/2299691023.png?width=442"
class="image-center" loading="lazy"
data-image-src="attachments/2298511407/2299691023.png" data-height="243"
data-width="452" data-unresolved-comment-count="0"
data-linked-resource-id="2299691023" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="DQS6.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="2298511407"
data-linked-resource-container-version="9"
data-media-id="3ce5c090-f8a9-4fdd-8b97-01942da092c0"
data-media-type="file" width="442" />

Because of the difference in how these two methods of exporting and
importing assets work internally there is no way to fix this behaviour.

# Solution

For newer project you will avoid the problem by never exporting and
importing jobs as `.dsx` files.

For older projects, which do contain QualityStage assets which have been
imported from `.dsx` files, the suggested workaround is to determine
which, if any, of these files have been modified by developers. Any of
these out-of-the-box Standardization Rules (`.dqs`) files that have not
been modified should be removed from the ‘golden copy’ source
repository.

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220906-015628.png](attachments/2298511407/2299363329.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220906-015756.png](attachments/2298511407/2299199495.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220906-015835.png](attachments/2298511407/2299461633.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220906-015917.png](attachments/2298511407/2299494401.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220906-015938.png](attachments/2298511407/2299527169.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220906-020010.png](attachments/2298511407/2299035653.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220906-020018.png](attachments/2298511407/2299625473.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220906-020152.png](attachments/2298511407/2299002885.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220906-020206.png](attachments/2298511407/2299527177.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220906-021047.png](attachments/2298511407/2299363348.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220906-021100.png](attachments/2298511407/2299691009.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220906-021718.png](attachments/2298511407/2299691015.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[DQS1.png](attachments/2298511407/2299756545.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[DQS2.png](attachments/2298511407/2299101189.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[DQS3.png](attachments/2298511407/2299133961.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[DQS4.png](attachments/2298511407/2299756551.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[DQS5.png](attachments/2298511407/2298806379.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[DQS6.png](attachments/2298511407/2299691023.png) (image/png)  

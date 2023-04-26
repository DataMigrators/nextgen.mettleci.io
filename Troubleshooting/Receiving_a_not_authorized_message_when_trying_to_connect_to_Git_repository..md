# Receiving a 'not authorized' message when trying to connect to Git repository.

# Problem

When trying to register a Git repository against a DataStage Project in
MettleCI Workbench you receive a `https://{URL}: not authorized` error
message.

<img src="attachments/2261483521/2261188613.png?width=453"
class="image-center" loading="lazy"
data-image-src="attachments/2261483521/2261188613.png" data-height="356"
data-width="931" data-unresolved-comment-count="0"
data-linked-resource-id="2261188613" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20220722-004744.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="2261483521"
data-linked-resource-container-version="1"
data-media-id="c25b5dd6-ca65-4c3e-833b-1c1811320751"
data-media-type="file" width="453" />

# Cause

You do not have Workbench configured to supply your Git host with an
appropriate SSH key.

# Solution

See the explanation <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/1745747969/Configuring+MettleCI+Workbench+to+communicate+with+Git+over+HTTPS"
data-linked-resource-id="1745747969" data-linked-resource-version="26"
data-linked-resource-type="page">here</a>.

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220722-004233.png](attachments/2261483521/2261516289.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220722-004333.png](attachments/2261483521/2261024781.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220722-004713.png](attachments/2261483521/2261450755.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220722-004744.png](attachments/2261483521/2261188613.png)
(image/png)  

# Unit Test fails due to exceeded memory threshold

# Problem

You receive a memory error in the job log when running a unit test

<img src="attachments/634617857/741343360.png" class="image-center"
loading="lazy" data-image-src="attachments/634617857/741343360.png"
data-height="341" data-width="1195" data-unresolved-comment-count="0"
data-linked-resource-id="741343360" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20200511-074032.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="634617857"
data-linked-resource-container-version="8"
data-media-id="d1e6163f-6a0a-49cb-99ce-07ede971ebf7"
data-media-type="file" />

# Solution

You need to provide a Cluster clause in your Unit Test Specification to
help MettleCI optimise memory usage. See <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/644546565/"
rel="nofollow">High Volume Unit Tests</a>.

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200511-074032.png](attachments/634617857/741343360.png)
(image/png)  

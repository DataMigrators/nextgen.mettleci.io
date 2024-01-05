# Jira displays error about Workbench 'not registered as a Consumer' when registering application

# Problem

You receive this message in the Jira ‘Applications’ page when attempting
to <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/1507328025/Integrating+Atlassian+Jira+with+MettleCI+Workbench"
data-linked-resource-id="1507328025" data-linked-resource-version="28"
data-linked-resource-type="page">integrate MettleCI Workbench with
Atlassian Jira</a>:

"MettleCI Workbench (demo115)" (Generic Application) is not

registered as a Consumer and cannot make requests into "JIRA"

(JIRA) using OAuth. (?)

# Cause

You forgot to check the **Create incoming link** checkbox on the **Link
applications** dialog

<img src="attachments/2269413379/2270003203.png" class="image-center"
loading="lazy" data-image-src="attachments/2269413379/2270003203.png"
data-height="839" data-width="556" data-unresolved-comment-count="0"
data-linked-resource-id="2270003203" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20220802-045620.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="2269413379"
data-linked-resource-container-version="2"
data-media-id="97f21be3-7a2c-4de6-80e3-0d3a8ad9dac5"
data-media-type="file" />

# Solution

Ensure you check the **Create incoming link** checkbox on the **Link
applications** dialog!

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220802-045620.png](attachments/2269413379/2270003203.png)
(image/png)  

# Configuring Jobs for Unit Testing

MettleCI's powerful Unit Test capability allows developer to conduct
unit testing using authored, captured, or fabricated data without having
to alter your DataStage job design.  Unit Tests are created, maintained,
and monitored using the MettleCI Workbench.  Unit Tests are executed
using the Windows-based DataStage Designer or browser-based DataStage
Flow Designer.

In order to use the Unit Test Feature, you’ll need to add an Environment
Variable to each DataStage job for which you wish to use automated unit
testing

## Enabling Unit Testing for a Job:

If you are unable to complete these steps because the
$DM_ENABLE_UNIT_TESTING environment variable is not present, please
follow these instructions to <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/455868494/Installing+the+Parallel+Unit+Test+Harness+on+Unix"
rel="nofollow">enable MettleCI Unit Testing for an existing DataStage
project</a>.

1.  In DataStage Designer, open the job you wish to enable unit testing
    for and open the Job Properties dialog:  

    <img src="attachments/470319149/470057187.png" class="image-center"
    loading="lazy" data-image-src="attachments/470319149/470057187.png"
    data-height="289" data-width="461" data-unresolved-comment-count="0"
    data-linked-resource-id="470057187" data-linked-resource-version="1"
    data-linked-resource-type="attachment"
    data-linked-resource-default-alias="image-20191219-031446.png"
    data-base-url="https://datamigrators.atlassian.net/wiki"
    data-linked-resource-content-type="image/png"
    data-linked-resource-container-id="470319149"
    data-linked-resource-container-version="2"
    data-media-id="f850094f-8e25-475e-96d0-48b817216a34"
    data-media-type="file" />

2.  Open the “Parameters” tab and click “Add Environment Variable…”:

    <img src="attachments/470319149/470188132.png" class="image-center"
    loading="lazy" data-image-src="attachments/470319149/470188132.png"
    data-height="438" data-width="943" data-unresolved-comment-count="0"
    data-linked-resource-id="470188132" data-linked-resource-version="1"
    data-linked-resource-type="attachment"
    data-linked-resource-default-alias="image-20191219-031607.png"
    data-base-url="https://datamigrators.atlassian.net/wiki"
    data-linked-resource-content-type="image/png"
    data-linked-resource-container-id="470319149"
    data-linked-resource-container-version="2"
    data-media-id="23d5d7e7-c748-43f8-b94c-c0fffbd26764"
    data-media-type="file" />

3.  Add “$DM_ENABLE_UNIT_TESTING” from the “MettleCI” section:

    <img src="attachments/470319149/470319166.png" class="image-center"
    loading="lazy" data-image-src="attachments/470319149/470319166.png"
    data-height="630" data-width="762" data-unresolved-comment-count="0"
    data-linked-resource-id="470319166" data-linked-resource-version="1"
    data-linked-resource-type="attachment"
    data-linked-resource-default-alias="image-20191219-031743.png"
    data-base-url="https://datamigrators.atlassian.net/wiki"
    data-linked-resource-content-type="image/png"
    data-linked-resource-container-id="470319149"
    data-linked-resource-container-version="2"
    data-media-id="a3111e0a-e1b8-49b6-a8cc-49fab781a072"
    data-media-type="file" />

4.  Save the job. You will now be able to choose the Unit Testing
    Configuration when executing your job:  

    <img src="attachments/470319149/470155360.png" class="image-center"
    loading="lazy" data-image-src="attachments/470319149/470155360.png"
    data-height="410" data-width="569" data-unresolved-comment-count="0"
    data-linked-resource-id="470155360" data-linked-resource-version="1"
    data-linked-resource-type="attachment"
    data-linked-resource-default-alias="image-20191219-032457.png"
    data-base-url="https://datamigrators.atlassian.net/wiki"
    data-linked-resource-content-type="image/png"
    data-linked-resource-container-id="470319149"
    data-linked-resource-container-version="2"
    data-media-id="958dd628-96e2-433f-b54b-cc7b1514a45b"
    data-media-type="file" />

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20191219-031446.png](attachments/470319149/470057187.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20191219-031607.png](attachments/470319149/470188132.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20191219-031743.png](attachments/470319149/470319166.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20191219-032457.png](attachments/470319149/470155360.png)
(image/png)  

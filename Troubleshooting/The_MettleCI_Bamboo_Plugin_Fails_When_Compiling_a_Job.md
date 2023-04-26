# The MettleCI Bamboo Plugin Fails When Compiling a Job

## Problem

MettleCI logs indicate that compilation commences but the process never
completes or Bamboo’s hung build detection kills the processes:

``` java
simple    27-Nov-2019 21:20:52    Compiling DataStage server routines...
```

The `dscc.exe` command line utility included as part of the DataStage
Client will indicate that it is initializing but never complete when it
is run under the `Local System` account in Windows:

``` java
> dscc.exe /d datastage-svcs.datamigrators.io:9080 /h DATASTAGE-ENGN.DATAMIGRATORS.IO /u isadmin /p ***** /j ExampleJob /rcf /rt X ExampleProject

Initializing
```

## Solution

Please verify that any Bamboo or Bamboo Remote Agent Services you have
installed on Windows are running as a user other than `Local System`

To change an existing service to run as another user

1.  Right click your service and select “Properties”

    <img src="attachments/465797125/465600529.png" class="image-center"
    loading="lazy" data-image-src="attachments/465797125/465600529.png"
    data-height="293" data-width="955" data-unresolved-comment-count="0"
    data-linked-resource-id="465600529" data-linked-resource-version="1"
    data-linked-resource-type="attachment"
    data-linked-resource-default-alias="image-20191129-012349.png"
    data-base-url="https://datamigrators.atlassian.net/wiki"
    data-linked-resource-content-type="image/png"
    data-linked-resource-container-id="465797125"
    data-linked-resource-container-version="5"
    data-media-id="cd1b80ba-9d23-45a3-98ae-8659765c0b49"
    data-media-type="file" />

2.  Click the “Log On” tab, Select “This account” and click the
    “Browse…” button.

    <img src="attachments/465797125/465895502.png" class="image-center"
    loading="lazy" data-image-src="attachments/465797125/465895502.png"
    data-height="470" data-width="406" data-unresolved-comment-count="0"
    data-linked-resource-id="465895502" data-linked-resource-version="1"
    data-linked-resource-type="attachment"
    data-linked-resource-default-alias="image-20191202-214106.png"
    data-base-url="https://datamigrators.atlassian.net/wiki"
    data-linked-resource-content-type="image/png"
    data-linked-resource-container-id="465797125"
    data-linked-resource-container-version="5"
    data-media-id="1e2924fd-0ff7-48ad-a465-ce30ed0ec44c"
    data-media-type="file" />

3.  Enter the username of that account you wish to use in the textbox
    and click “Check Names”

    <img src="attachments/465797125/465895507.png" class="image-center"
    loading="lazy" data-image-src="attachments/465797125/465895507.png"
    data-height="255" data-width="460" data-unresolved-comment-count="0"
    data-linked-resource-id="465895507" data-linked-resource-version="1"
    data-linked-resource-type="attachment"
    data-linked-resource-default-alias="image-20191202-214252.png"
    data-base-url="https://datamigrators.atlassian.net/wiki"
    data-linked-resource-content-type="image/png"
    data-linked-resource-container-id="465797125"
    data-linked-resource-container-version="5"
    data-media-id="b8f790a6-fb4b-4cac-8a67-5b728a60d0c1"
    data-media-type="file" />

    If your username is not found after clicking “Check Names”, click
    the “Locations…” button and select “Entire Directory”.

4.  Save all changes restart the Service.

Depending on the permissions set on your Bamboo and/or Bamboo Remove
Agent installation directories, you may get a permission denied error
when attempting to restart the service.

To resolve, ensure the Account you have selected to run the service has
read and write access to the installation directory and all
sub-directories and files.

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20191129-012349.png](attachments/465797125/465600529.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20191129-012710.png](attachments/465797125/465698848.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20191202-214106.png](attachments/465797125/465895502.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20191202-214252.png](attachments/465797125/465895507.png)
(image/png)  

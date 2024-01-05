# CC Migrate Bamboo Task

The MettleCI Connector Migration Tool plugin is used to automate the
changing of Jobs to use Connector Stages instead of the deprecated
Plug-in and Operator Stages. It uses the IBM-supplied Connector
Migration Tool (AKA 'CCMT') which is provided as part of the
installation media for each new version of DataStage.

**Contents**

-   [Configuration Steps](#CCMigrateBambooTask-ConfigurationSteps)
-   [Source Code Checkout
    Settings](#CCMigrateBambooTask-SourceCodeCheckoutSettings)
-   [Execute Connector Migration
    Settings](#CCMigrateBambooTask-ExecuteConnectorMigrationSettings)
    -   [At least one DataStage client capability needs to be
        defined](#CCMigrateBambooTask-AtleastoneDataStageclientcapabilityneedstobedefined)
-   [Remote Agent
    Workaround](#CCMigrateBambooTask-RemoteAgentWorkaround)
-   [Related articles](#CCMigrateBambooTask-Relatedarticles)

------------------------------------------------------------------------

## Configuration Steps

1.  Navigate to the **Artefacts** configuration tab for your job and add
    a new definition for InfoServer Assets:

    |                   |           |              |            |
    |-------------------|-----------|--------------|------------|
    | Name              | Location  | Copy pattern | Operations |
    | InfoServer Assets | datastage | \*\*/\*      | Share      |

    <img src="attachments/458260491/458260503.png?width=900" loading="lazy"
    data-image-src="attachments/458260491/458260503.png"
    data-unresolved-comment-count="0" data-linked-resource-id="458260503"
    data-linked-resource-version="1" data-linked-resource-type="attachment"
    data-linked-resource-default-alias="CCMT-Plugin-Artifacts.png"
    data-base-url="https://datamigrators.atlassian.net/wiki"
    data-linked-resource-content-type="image/png"
    data-linked-resource-container-id="458260491"
    data-linked-resource-container-version="4"
    data-media-id="8be975eb-2f86-4285-82c5-0129338a6408"
    data-media-type="file" width="900" />

2.  Create two Bamboo Tasks in the following order:

    1.  Source Code Checkout
    2.  Execute Connector Migration Tool

    You may add additional tasks in between *Source Code Checkout* and
    *Execute Connector Migration Tool. *However, *Source Code Checkout*
    must always come before *Execute Connector Migration Tool.*

    <img src="attachments/458260491/458260500.png?width=350" loading="lazy"
    data-image-src="attachments/458260491/458260500.png"
    data-unresolved-comment-count="0" data-linked-resource-id="458260500"
    data-linked-resource-version="1" data-linked-resource-type="attachment"
    data-linked-resource-default-alias="CCMT-Tasks.png"
    data-base-url="https://datamigrators.atlassian.net/wiki"
    data-linked-resource-content-type="image/png"
    data-linked-resource-container-id="458260491"
    data-linked-resource-container-version="4"
    data-media-id="b0481b72-51c7-4343-9aab-176a54f4634c"
    data-media-type="file" width="350" />

3.  Configure each task as described below

------------------------------------------------------------------------

## Source Code Checkout Settings

Provide the following details:

<table class="wrapped confluenceTable">
<tbody>
<tr class="header">
<th class="confluenceTh">Input</th>
<th class="confluenceTh">Mandatory</th>
<th class="confluenceTh">Type</th>
<th class="confluenceTh">Description</th>
</tr>
&#10;<tr class="odd">
<td class="confluenceTd">Task description</td>
<td class="confluenceTd">N</td>
<td class="confluenceTd">Text field</td>
<td class="confluenceTd">Description of the Bamboo task</td>
</tr>
<tr class="even">
<td class="confluenceTd">Disable this task</td>
<td class="confluenceTd">N</td>
<td class="confluenceTd">Checkbox</td>
<td class="confluenceTd">If checked, this task will be disabled</td>
</tr>
<tr class="odd">
<td class="confluenceTd">Repository</td>
<td class="confluenceTd">Y</td>
<td class="confluenceTd">Selection</td>
<td class="confluenceTd">The name of the repository</td>
</tr>
<tr class="even">
<td class="confluenceTd">Checkout Directory</td>
<td class="confluenceTd">N</td>
<td class="confluenceTd">Text field</td>
<td class="confluenceTd"><div class="content-wrapper">
<p>Alternate sub-directory to which the code will be checked out</p>
<div>
<p>Suggested Value</p>
<div>
<p>Leave blank</p>
</div>
</div>
</div></td>
</tr>
<tr class="odd">
<td class="confluenceTd">Force Clean Build</td>
<td class="confluenceTd">N</td>
<td class="confluenceTd">Checkbox</td>
<td class="confluenceTd"><div class="content-wrapper">
<p>Removed the source directory and check it out again prior to each
build</p>
<div>
<p>Suggested Value</p>
<div>
<p>Checked</p>
</div>
</div>
</div></td>
</tr>
</tbody>
</table>

<img src="attachments/458260491/458260497.png?width=550" loading="lazy"
data-image-src="attachments/458260491/458260497.png"
data-unresolved-comment-count="0" data-linked-resource-id="458260497"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="CCMT-SourceCodeCheckout.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="458260491"
data-linked-resource-container-version="4"
data-media-id="c621051f-0abe-4d11-aae8-414f2f0597cf"
data-media-type="file" width="550" height="551" />

------------------------------------------------------------------------

## Execute Connector Migration Settings

Provide the following details:

<table class="wrapped confluenceTable">
<tbody>
<tr class="header">
<th class="confluenceTh">Input</th>
<th class="confluenceTh">Mandatory</th>
<th class="confluenceTh">Type</th>
<th class="confluenceTh">Description</th>
</tr>
&#10;<tr class="odd">
<td class="confluenceTd">Task description</td>
<td class="confluenceTd">N</td>
<td class="confluenceTd">Text field</td>
<td class="confluenceTd">Description of the Bamboo task</td>
</tr>
<tr class="even">
<td class="confluenceTd">Disable this task</td>
<td class="confluenceTd">N</td>
<td class="confluenceTd">Checkbox</td>
<td class="confluenceTd">If checked, this task will be disabled</td>
</tr>
<tr class="odd">
<td class="confluenceTd">Executable</td>
<td class="confluenceTd">Y</td>
<td class="confluenceTd">Selection</td>
<td class="confluenceTd"><p>The name of the DataStage client capability
to be used by this task</p>
<h6
id="CCMigrateBambooTask-AtleastoneDataStageclientcapabilityneedstobedefined"
style="text-decoration: none;text-align: left;"><em>At least one
DataStage client capability needs to be defined</em></h6></td>
</tr>
<tr class="even">
<td colspan="4" class="confluenceTd"><strong>InfoServer
Authentication</strong></td>
</tr>
<tr class="odd">
<td class="confluenceTd">Domain</td>
<td class="confluenceTd">Y</td>
<td class="confluenceTd">Text field</td>
<td class="confluenceTd"><p>The URL <em>&lt;domain name&gt;:&lt;port
number&gt;</em> of the IBM Information Server Services tier</p>
<div>
<p>Suggested Value</p>
<div>
<p>${bamboo.Domain}</p>
</div>
</div></td>
</tr>
<tr class="even">
<td class="confluenceTd">Server</td>
<td class="confluenceTd">Y</td>
<td class="confluenceTd">Text field</td>
<td class="confluenceTd"><p>The URL of the IBM Information Server Engine
tier</p>
<div>
<p>Suggested Value</p>
<div>
<p>${bamboo.ServerName}</p>
</div>
</div></td>
</tr>
<tr class="odd">
<td class="confluenceTd">Username</td>
<td class="confluenceTd">Y</td>
<td class="confluenceTd">Text field</td>
<td class="confluenceTd"><p>The username used to connect to IBM
Information server </p>
<div>
<p>Suggested Value</p>
<div>
<p>${bamboo.DatastageName}</p>
</div>
</div></td>
</tr>
<tr class="even">
<td class="confluenceTd">Password</td>
<td class="confluenceTd">Y</td>
<td class="confluenceTd">Text field</td>
<td class="confluenceTd"><p>The password for the username specified
above (if you check the Change password box)</p>
<div>
<p>Suggested Value</p>
<div>
<p>${bamboo.DatastagePassword}</p>
</div>
</div></td>
</tr>
<tr class="odd">
<td colspan="4" class="confluenceTd"><p><strong>Execute
Settings</strong></p></td>
</tr>
<tr class="even">
<td class="confluenceTd">Project Name</td>
<td class="confluenceTd">Y</td>
<td class="confluenceTd">Text field</td>
<td class="confluenceTd">The name of the IBM Information Server
DataStage project containing the job or sequence to execute</td>
</tr>
<tr class="odd">
<td class="confluenceTd">Optional parameters</td>
<td class="confluenceTd">N</td>
<td class="confluenceTd">Text field</td>
<td class="confluenceTd"><div class="content-wrapper">
<p>Optional parameters</p>
<ul>
<li>-R to run the process in preview mode</li>
</ul>
<div>
<div>
<p>Preview mode = list the jobs that needs Connector Migration, but will
not modify the jobs</p>
</div>
</div>
</div></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>Unique CCMigrate Log Filename</p></td>
<td class="confluenceTd">Y</td>
<td class="confluenceTd">Text field</td>
<td class="confluenceTd"><div class="content-wrapper">
<p>Unique log file name.</p>
<div>
<p>Suggested Value</p>
<div>
<p>${bamboo.buildKey}.log</p>
</div>
</div>
</div></td>
</tr>
<tr class="odd">
<td class="confluenceTd">Root ISX Directory</td>
<td class="confluenceTd">Y</td>
<td class="confluenceTd">Textfield</td>
<td class="confluenceTd"><p>It must match the InfoServer Assets location
specified in Artifacts tab</p>
<p><br />
</p></td>
</tr>
<tr class="even">
<td class="confluenceTd">Max Threads</td>
<td class="confluenceTd">Y</td>
<td class="confluenceTd">Textfield</td>
<td class="confluenceTd"><p>Number of threads uses for identify before
and after status</p>
<div>
<p>Suggested Value</p>
<div>
<p>8</p>
</div>
</div></td>
</tr>
<tr class="odd">
<td class="confluenceTd">Fail plan when compile error</td>
<td class="confluenceTd">N</td>
<td class="confluenceTd">Checkbox</td>
<td class="confluenceTd"><p>True = Build plan will fail when it
encounter compilation error</p>
<p>False (default) = Build plan will pass, even if there are compilation
error</p></td>
</tr>
</tbody>
</table>

<img src="attachments/458260491/458260494.png?width=550" loading="lazy"
data-image-src="attachments/458260491/458260494.png"
data-unresolved-comment-count="0" data-linked-resource-id="458260494"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="CCMT-Plugin-Form.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="458260491"
data-linked-resource-container-version="4"
data-media-id="6c7d69fb-c446-4934-94db-7755269087eb"
data-media-type="file" width="550" />

------------------------------------------------------------------------

## Remote Agent Workaround

Atlassian Bamboo Remote Agents running on Windows (**before** Bamboo
v6.10) exhibit a problem for which you may need to implement a
workaround <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/458457095/Bamboo+Agent+produces+chcp+or+-107374+errors"
data-linked-resource-id="458457095" data-linked-resource-version="4"
data-linked-resource-type="page">documented here</a>.

------------------------------------------------------------------------

## Related articles

-   Page:

    <a
    href="/wiki/spaces/MCI/pages/2048327681/How+to+Tag+Bitbucket+repository+during+deployment"
    data-linked-resource-id="2048327681" data-linked-resource-type="page"
    data-linked-resource-version="8">How to Tag Bitbucket repository during
    deployment</a>

-   Page:

    <a
    href="/wiki/spaces/MCI/pages/383484151/HOW-TO%3A+Use+dm-ccmigrate-plugin"
    data-linked-resource-id="383484151" data-linked-resource-type="page"
    data-linked-resource-version="25">HOW-TO: Use dm-ccmigrate-plugin</a>

-   Page:

    <a
    href="/wiki/spaces/MCI/pages/115686480/Install+Information+Server+Client"
    data-linked-resource-id="115686480" data-linked-resource-type="page"
    data-linked-resource-version="11">Install Information Server Client</a>

-   Page:

    <a
    href="/wiki/spaces/MCI/pages/416153612/Creating+a+Rapid+DataStage+Upgrade+Enablement+Environment"
    data-linked-resource-id="416153612" data-linked-resource-type="page"
    data-linked-resource-version="21">Creating a Rapid DataStage Upgrade
    Enablement Environment</a>

-   Page:

    <a
    href="/wiki/spaces/MCI/pages/467337217/HOW-TO%3A+Use+MettleCI+Transmuter+in+Bamboo+Plan"
    data-linked-resource-id="467337217" data-linked-resource-type="page"
    data-linked-resource-version="10">HOW-TO: Use MettleCI Transmuter in
    Bamboo Plan</a>

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[CCMT-Plugin-Form.png](attachments/458260491/458260494.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[CCMT-SourceCodeCheckout.png](attachments/458260491/458260497.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[CCMT-Tasks.png](attachments/458260491/458260500.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[CCMT-Plugin-Artifacts.png](attachments/458260491/458260503.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[ccmigrate-path.png](attachments/458260491/458260506.png) (image/png)  

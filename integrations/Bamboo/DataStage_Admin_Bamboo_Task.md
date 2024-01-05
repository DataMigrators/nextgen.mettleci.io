# DataStage Admin Bamboo Task

MettleCI APIs can be used to perform some DataStage administration tasks
that CI/CD process can leverage:

-   Create DataStage Project
-   Delete DataStage Project
-   Clean up - delete multiple projects based on regular a regular
    expression

**Contents**

-   [Configuration Steps](#DataStageAdminBambooTask-ConfigurationSteps)
-   [Create Project
    settings](#DataStageAdminBambooTask-CreateProjectsettings)
-   [Delete Project
    settings](#DataStageAdminBambooTask-DeleteProjectsettings)
-   [Cleanup Projects
    settings](#DataStageAdminBambooTask-CleanupProjectssettings)

------------------------------------------------------------------------

## Configuration Steps

1.  Navigate to the **Tasks** configuration tab for the job (this will
    be the default job if creating a new plan).

2.  Click the name of an existing DataStage Admin task, or click **Add
    Task** and then search 'DataStage' to easily locate the DataStage
    Admin task type, in order to create a new task.

3.  Complete the following settings:  
      
    **Common Settings**

    |                      |                                                                                                 |
    |------------------------|------------------------------------------------|
    | Task Description     | A description of the task, which is displayed in Bamboo.                                        |
    | Disable this task    | Check, or clear, to selectively run this task.                                                  |
    | Executable           | From the pulldown list, choose a 'Datastage Capability'                                         |
    | Domain               | Enter the Domain of the Datastage instance (Host Name of the Services Tier)                     |
    | Server               | Enter the Server of the Datastage instance (Host Name of the Engine Tier)                       |
    | Username             | Enter the Datastage Username                                                                    |
    | Password             | Enter the Datastage Password                                                                    |
    | DataStage Admin Type | 'Create Project', 'Delete Project' or 'Cleanup Projects'.  See below for type specific settings |

4.  Provide the remaining details to the Task as determined by your
    selected 'Datastage Admin Type'.  See the sections below for more
    details. 

5.  Click **Save**

  

------------------------------------------------------------------------

## **Create Project settings**

Provide the following details:

<table class="relative-table wrapped confluenceTable"
style="width: 43.7465%;">
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<tbody>
<tr class="odd">
<th class="confluenceTh">DataStage Admin Type</th>
<td class="confluenceTd">Create Project</td>
</tr>
<tr class="even">
<th class="confluenceTh">Project name</th>
<td class="confluenceTd">Name of the DataStage project to be
created</td>
</tr>
<tr class="odd">
<th class="confluenceTh">Use default project location?</th>
<td class="confluenceTd"><p>If checked, project files are created in the
standard path under the default Projects directory on the Engine
tier.</p>
<p>If unchecked, enter the custom 'Project Location' below</p></td>
</tr>
<tr class="even">
<th class="confluenceTh">Project Location</th>
<td class="confluenceTd">Enter the custom DataStage project
directory</td>
</tr>
<tr class="odd">
<th class="confluenceTh">Copy roles from another project?</th>
<td class="confluenceTd"><p>Check to copy roles from another project</p>
<p>If checked, enter a 'Roles Project name' below</p></td>
</tr>
<tr class="even">
<th class="confluenceTh">Roles project name</th>
<td class="confluenceTd">Enter the name of the DataStage project to copy
roles from</td>
</tr>
</tbody>
</table>

<img src="attachments/408387649/408387669.png?width=500" loading="lazy"
data-image-src="attachments/408387649/408387669.png"
data-unresolved-comment-count="0" data-linked-resource-id="408387669"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="image2019-4-30_14-20-30.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="408387649"
data-linked-resource-container-version="9"
data-media-id="491c2223-3232-4081-a23a-058f83e83792"
data-media-type="file" width="500" height="800" />

------------------------------------------------------------------------

## **Delete Project settings**

Provide the following details:

|                      |                                        |
|----------------------|----------------------------------------|
| DataStage Admin Type | Delete Project                         |
| Project name         | Name of DataStage project to be delete |

<img src="attachments/408387649/408354973.png?width=500" loading="lazy"
data-image-src="attachments/408387649/408354973.png"
data-unresolved-comment-count="0" data-linked-resource-id="408354973"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="image2019-4-30_14-21-35.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="408387649"
data-linked-resource-container-version="9"
data-media-id="30586854-52dc-48e6-a55b-dac2a97f7101"
data-media-type="file" width="500" height="642" />

------------------------------------------------------------------------

## **Cleanup Projects** **settings** ****

Provide the following details:

<table class="relative-table wrapped confluenceTable"
style="width: 43.9148%;">
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<th class="confluenceTh">DataStage Admin Type</th>
<td class="confluenceTd">Cleanup Projects</td>
</tr>
<tr class="even">
<th class="confluenceTh">Project pattern (regex)</th>
<td class="confluenceTd">Search pattern for existing projects, sorted in
<a href="https://en.wikipedia.org/wiki/Natural_sort_order"
rel="nofollow">natural order</a></td>
</tr>
<tr class="odd">
<th class="confluenceTh">Number of projects to retain</th>
<td class="confluenceTd"><p>Number of projects to retain. Projects at
the top of the sorted list are deleted first. <br />
For example, if the project pattern results in the following sorted
project list:</p>
<ul>
<li>project1</li>
<li>project2</li>
<li>project11</li>
<li>zzProject3</li>
<li>zzProject4</li>
</ul>
<p>A setting of 3 will delete project1 and project2 resulting in 3
retained projects:</p>
<ul>
<li>project11</li>
<li>zzProject3</li>
<li>zzProject4</li>
</ul></td>
</tr>
</tbody>
</table>

<img src="attachments/408387649/408354978.png?width=500" loading="lazy"
data-image-src="attachments/408387649/408354978.png"
data-unresolved-comment-count="0" data-linked-resource-id="408354978"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="image2019-4-30_14-22-35.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="408387649"
data-linked-resource-container-version="9"
data-media-id="c4c7d501-20f1-4a70-b76b-75581f509134"
data-media-type="file" width="500" height="703" />

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2017-3-8_16-56-25.png](attachments/408387649/408322116.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[dsadmin-plugin.png](attachments/408387649/408486022.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-4-30_14-20-30.png](attachments/408387649/408387669.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-4-30_14-21-35.png](attachments/408387649/408354973.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-4-30_14-22-35.png](attachments/408387649/408354978.png)
(image/png)  

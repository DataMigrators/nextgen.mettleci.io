# Export DataStage Asset Bamboo Task

You can use the Export DataStage Asset task to export one or more
DataStage assets as individual ISX files in a folder structure matching
the project.  The assets to be exported can be specified by name, list
or entire project.

Task Availability

This task is available after installing the **MettleCI - ISX Export
Plugin** (dm-isxexport-plugin.jar)

**Contents**

-   [Configuration
    Steps](#ExportDataStageAssetBambooTask-ConfigurationSteps)
-   [Asset Name](#ExportDataStageAssetBambooTask-AssetName)
-   [Asset List](#ExportDataStageAssetBambooTask-AssetList)
-   [Entire Project](#ExportDataStageAssetBambooTask-EntireProject)

## Configuration Steps

1.  Navigate to the **Tasks** configuration tab for the job (this will
    be the default job if creating a new plan).

2.  Click the name of an existing Export DataStage Asset task, or click
    **Add Task** and then search 'DataStage' to easily locate
    the Export DataStage Asset task type, in order to create a new task.

3.  Complete the following settings:

    |                   |                                                                                      |
    |-----------------------|-------------------------------------------------|
    | Task Description  | A description of the task, which is displayed in Bamboo.                             |
    | Disable this task | Check, or clear, to selectively run this task.                                       |
    | Executable        | From the pulldown list, choose a 'DataStage Capability'                              |
    | Domain            | Enter the Domain of the DataStage instance (Host Name of the Services Tier)          |
    | Server            | Enter the Server of the DataStage instance (Host Name of the Engine Tier)            |
    | Username          | Enter the DataStage Username                                                         |
    | Password          | Enter the DataStage Password                                                         |
    | Project name      | DataStage Project containing assets to be exported                                   |
    | Export Type       | 'Asset Name', 'Asset List' or 'Entire Project'.  See below for type specific options |

4.  Provide the remaining details to the Task as determined by your
    selected 'Export Type'.  See the sections below for more details. 

5.  Click **Save**  

    <img src="attachments/409305095/409272347.png?width=546" loading="lazy"
    data-image-src="attachments/409305095/409272347.png"
    data-unresolved-comment-count="0" data-linked-resource-id="409272347"
    data-linked-resource-version="1" data-linked-resource-type="attachment"
    data-linked-resource-default-alias="image2018-3-29_15-27-43.png"
    data-base-url="https://datamigrators.atlassian.net/wiki"
    data-linked-resource-content-type="image/png"
    data-linked-resource-container-id="409305095"
    data-linked-resource-container-version="3"
    data-media-id="d01404d8-c95e-4f99-a0df-1560fd0c2838"
    data-media-type="file" width="546" height="929" />

  

  

------------------------------------------------------------------------

## **Asset Name**

Provide the following details:

<table class="wrapped relative-table confluenceTable"
style="width: 48.5698%;">
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<th class="confluenceTh">Export Type</th>
<td class="confluenceTd">Asset Name</td>
</tr>
<tr class="even">
<th class="confluenceTh">Asset name</th>
<td class="confluenceTd">Comma separated list of asset names to be
exported</td>
</tr>
<tr class="odd">
<th class="confluenceTh">Delete ISX when asset not in project</th>
<td class="confluenceTd"><p>Use this option to apply project deletions
or moves between categories to an existing directory of assets.  Rules
used by this option are as follows:</p>
<p>If ISX file exists and the asset has been deleted in the project then
the existing ISX file will be deleted.</p>
<p>If ISX file exists and the asset has moved categories in the project
then the existing ISX file will be deleted before re-exporting.</p></td>
</tr>
<tr class="even">
<th class="confluenceTh">Include binaries</th>
<td class="confluenceTd">Check to include binary files containing the
compiled assets</td>
</tr>
<tr class="odd">
<th class="confluenceTh">Include previews</th>
<td class="confluenceTd">Check to allow the ISX to be viewed using the
MettleCI ISX preview plugin for Bitbucket.</td>
</tr>
<tr class="even">
<th class="confluenceTh">Export location</th>
<td class="confluenceTd">Enter the sub-directory to export to</td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## **Asset List**

 Provide the following details:

|                  |                                                                                          |
|-----------------------|-------------------------------------------------|
| Export Type      | Asset List                                                                               |
| List file name   | File containing a list of assets to be exported                                          |
| Include Binaries | Check to include binary files containing the compiled assets                             |
| Include previews | Check to allow the ISX to be viewed using the MettleCI ISX preview plugin for Bitbucket. |
| Export location  | Enter the sub-directory to export to                                                     |

------------------------------------------------------------------------

## **Entire Project**

Provide the following details:

|                  |                                                                                          |
|-----------------------|-------------------------------------------------|
| Export Type      | Entire Project                                                                           |
| Include Binaries | Check to include binary files containing the compiled assets                             |
| Include previews | Check to allow the ISX to be viewed using the MettleCI ISX preview plugin for Bitbucket. |
| Export location  | Enter the sub-directory to export to                                                     |

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2018-3-29_15-27-43.png](attachments/409305095/409272347.png)
(image/png)  

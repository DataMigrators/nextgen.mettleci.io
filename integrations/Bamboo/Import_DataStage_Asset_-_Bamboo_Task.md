# Import DataStage Asset - Bamboo Task

You can use this task to import ISX files into an existing DataStage
project.  Import can be performed using a specific ISX file, list of ISX
files or entire directory containing ISX files.

Task Availability

This task is available after installing the **MettleCI - ISX Import
Plugin** (dm-isximport-plugin.jar)

## To configure an Import Datastage Asset task

Steps

1.  Navigate to the **Tasks** configuration tab for the job (this will
    be the default job if creating a new plan).

2.  Click the name of an existing Import Datastage Asset task, or click
    **Add Task** and then search 'Datastage' to easily locate the Import
    Datastage Asset task type, in order to create a new task.

3.  Complete the following settings:

    |                   |                                                                                             |
    |------------------------|------------------------------------------------|
    | Task Description  | A description of the task, which is displayed in Bamboo.                                    |
    | Disable this task | Check, or clear, to selectively run this task.                                              |
    | Executable        | From the pulldown list, choose a 'Datastage Capability'                                     |
    | Domain            | Enter the Domain of the Datastage instance (Host Name of the Services Tier)                 |
    | Server            | Enter the Server of the Datastage instance (Host Name of the Engine Tier)                   |
    | Username          | Enter the Datastage Username                                                                |
    | Password          | Enter the Datastage Password                                                                |
    | Project name      | DataStage Project containing assets to be Imported                                          |
    | Import Type       | 'Import File', 'File List', 'Entire Directory'.  See below for import type specific options |

      
    **Import File**

    |                                         |                                                                                                |
    |-----------------------------------------|------------------------------------------------------------------------------------------------|
    | Import Type                             | Import File                                                                                    |
    | ISX File                                | Enter the ISX File Name to be imported                                                         |
    | Delete all project assets not in import | Check to delete any assets that exist in the DataStage project that do not exist in the import |

      
    **File List**

    <table class="wrapped relative-table confluenceTable"
    style="width: 49.0746%;">
    <colgroup>
    <col style="width: 32%" />
    <col style="width: 67%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <th class="confluenceTh"><p>Import Type</p></th>
    <td class="confluenceTd">File List</td>
    </tr>
    <tr class="even">
    <th class="confluenceTh">List file name</th>
    <td class="confluenceTd">File containing a list of ISX files to be
    imported, this list is relative to the Root ISX Directory</td>
    </tr>
    <tr class="odd">
    <th class="confluenceTh">Root ISX Directory</th>
    <td class="confluenceTd"><p>Optional: Root directory containing ISX
    files</p>
    <p>If not specified, the agent working directory is used</p></td>
    </tr>
    <tr class="even">
    <th class="confluenceTh">Delete all project assets not in import</th>
    <td class="confluenceTd">Check to delete any assets that exist in the
    DataStage project that do not exist in the import directory</td>
    </tr>
    </tbody>
    </table>

      
    **Entire Directory**

    <table class="wrapped relative-table confluenceTable"
    style="width: 48.7942%;">
    <colgroup>
    <col style="width: 33%" />
    <col style="width: 66%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <th class="confluenceTh"><p>Import Type</p></th>
    <td class="confluenceTd">Entire Directory</td>
    </tr>
    <tr class="even">
    <th class="confluenceTh">Root ISX Directory</th>
    <td class="confluenceTd"><p>Optional: Root directory containing ISX
    files</p>
    <p>If not specified, the agent working directory is used</p></td>
    </tr>
    <tr class="odd">
    <th class="confluenceTh">Delete all project assets not in import</th>
    <td class="confluenceTd">Check to delete any assets that have not been
    included in this import</td>
    </tr>
    </tbody>
    </table>

     

4.  Click **Save**  
      

    <img src="attachments/409796627/409763858.png" loading="lazy"
    data-image-src="attachments/409796627/409763858.png"
    data-unresolved-comment-count="0" data-linked-resource-id="409763858"
    data-linked-resource-version="1" data-linked-resource-type="attachment"
    data-linked-resource-default-alias="image2017-3-9_16-17-18.png"
    data-base-url="https://datamigrators.atlassian.net/wiki"
    data-linked-resource-content-type="image/png"
    data-linked-resource-container-id="409796627"
    data-linked-resource-container-version="1"
    data-media-id="b97dc71c-a3a8-4de7-8015-6fbbda03576d"
    data-media-type="file" />

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2017-3-9_16-17-18.png](attachments/409796627/409763858.png)
(image/png)  

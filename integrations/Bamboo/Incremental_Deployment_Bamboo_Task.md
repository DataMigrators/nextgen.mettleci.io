# Incremental Deployment Bamboo Task

You can use the Incremental DataStage Deployment task to deploy an
entire directory of ISX files to an existing DataStage Project. 
Functionally, this is the equivalent of deleting everything from the
existing project, importing all ISX files, provisioning all QualityStage
rules and compiling all Jobs, Sequence, Server Routines and BuildOps. 
However, the task will minimize the deployment time by performing as few
operations based on the content of the existing project.

Task Availability

This task is available after installing the **MettleCI - DataStage
Deployment Plugin** (dm-dsdeploy-plugin.jar)

  

------------------------------------------------------------------------

## Configuration Steps

1.  Navigate to the **Tasks** configuration tab for the job (this will
    be the default job if creating a new plan).

2.  Click the name of an existing Incremental DataStage Deployment task,
    or click **Add Task** and then search 'Datastage' to easily locate
    the Incremental DataStage Deployment task type, in order to create a
    new task.

3.  Complete the following settings:

    <table class="wrapped relative-table confluenceTable"
    style="width: 48.6259%;">
    <tbody>
    <tr class="odd">
    <th class="confluenceTh">Task Description</th>
    <td class="confluenceTd">A description of the task, which is displayed
    in Bamboo.</td>
    </tr>
    <tr class="even">
    <th class="confluenceTh">Disable this task</th>
    <td class="confluenceTd">Check, or clear, to selectively run this
    task.</td>
    </tr>
    <tr class="odd">
    <th class="confluenceTh">Executable</th>
    <td class="confluenceTd">From the pulldown list, choose a 'Datastage
    Capability'</td>
    </tr>
    <tr class="even">
    <th class="confluenceTh">Domain</th>
    <td class="confluenceTd">Enter the Domain of the Datastage instance
    (Host Name of the Services Tier)</td>
    </tr>
    <tr class="odd">
    <th class="confluenceTh">Server</th>
    <td class="confluenceTd">Enter the Server of the Datastage instance
    (Host Name of the Engine Tier)</td>
    </tr>
    <tr class="even">
    <th class="confluenceTh">Username</th>
    <td class="confluenceTd">Enter the Datastage Username</td>
    </tr>
    <tr class="odd">
    <th class="confluenceTh">Password</th>
    <td class="confluenceTd">Enter the Datastage Password</td>
    </tr>
    <tr class="even">
    <th class="confluenceTh">Project name</th>
    <td class="confluenceTd">DataStage Project containing assets to
    be exported</td>
    </tr>
    <tr class="odd">
    <th class="confluenceTh">Root ISX Directory</th>
    <td class="confluenceTd"><p>Optional: Root directory containing ISX
    files to deploy</p>
    <p>If no value is specified, the agents working directory will be
    used</p></td>
    </tr>
    <tr class="even">
    <th class="confluenceTh">Max Threads</th>
    <td class="confluenceTd">The number of threads that should be used
    during compilation</td>
    </tr>
    <tr class="odd">
    <th class="confluenceTh">Parse compilation logs</th>
    <td class="confluenceTd"><br />
    </td>
    </tr>
    <tr class="even">
    <th class="confluenceTh">Deploy Parameter Sets</th>
    <td class="confluenceTd">If checked, a directory containing parameter
    set value files will be deployed. </td>
    </tr>
    <tr class="odd">
    <th class="confluenceTh">Parameter Set Directory</th>
    <td class="confluenceTd"><p>Required if previous option is checked.</p>
    <p>Specifies a directory of parameter set value files in Bitbucket.
    Usually '<em>Parameter Sets'</em> which actually means
    '<em>/datastage/Parameter Sets'</em></p>
    <p>The file format should match the format of files found on your
    DataStage Engine under <em>${DSHOME}../Projects/${Project
    Name}/ParameterSets</em> directory</p></td>
    </tr>
    </tbody>
    </table>

4.  Click **Save  
    <img src="attachments/264962064/264962071.png?width=574" loading="lazy"
    data-image-src="attachments/264962064/264962071.png"
    data-unresolved-comment-count="0" data-linked-resource-id="264962071"
    data-linked-resource-version="1" data-linked-resource-type="attachment"
    data-linked-resource-default-alias="image2018-3-29_17-10-1.png"
    data-base-url="https://datamigrators.atlassian.net/wiki"
    data-linked-resource-content-type="image/png"
    data-linked-resource-container-id="264962064"
    data-linked-resource-container-version="4"
    data-media-id="cc17e18c-d6b9-451d-872a-c13341ad4c0c"
    data-media-type="file" width="574" height="992" />  
    **

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2018-3-29_17-10-1.png](attachments/264962064/264962071.png)
(image/png)  

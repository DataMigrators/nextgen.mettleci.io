# Execute DataStage Job Bamboo Task

You can use the Execute DataStage Job task to execute a DataStage job or
sequence. 

Task Availability

This task is available after installing the **MettleCI - DataStage
Execute Plugin** (dm-dsexecute-plugin.jar)

## To configure an Execute Datastage Job Task

Steps

1.  Navigate to the **Tasks** configuration tab for the job (this will
    be the default job if creating a new plan).

2.  Click the name of an existing Execute Datastage Job task, or click
    **Add Task** and then search 'Datastage' to easily locate
    the Execute Datastage Job task type, in order to create a new task.

3.  Complete the following settings:

    <table class="wrapped confluenceTable">
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
    <td class="confluenceTd">DataStage Project containing assets to be
    executed</td>
    </tr>
    <tr class="odd">
    <th class="confluenceTh">Job/Sequence Name</th>
    <td class="confluenceTd">Enter the Job/Sequence Name to be executed</td>
    </tr>
    <tr class="even">
    <th class="confluenceTh">Run Mode</th>
    <td class="confluenceTd">Choose NORMAL, RESET, RESTART or VALIDATE</td>
    </tr>
    <tr class="odd">
    <th class="confluenceTh">Use Property File for Optional Parameters</th>
    <td class="confluenceTd">Check this option if parameters should come
    from a file rather than configuring in the plan</td>
    </tr>
    <tr class="even">
    <th class="confluenceTh">Optional Parameters</th>
    <td class="confluenceTd"><p>Use this multi-line text box to enter job
    parameters as key value pairs (eg. "DBPassword=tiger")</p>
    <p>Alternatively, if the previous property is set, you can enter a
    filename contain parameters as key value pairs</p></td>
    </tr>
    </tbody>
    </table>

      
      

4.  Click **Save**  
      

    <img src="attachments/116528256/116528345.png" loading="lazy"
    data-image-src="attachments/116528256/116528345.png"
    data-unresolved-comment-count="0" data-linked-resource-id="116528345"
    data-linked-resource-version="1" data-linked-resource-type="attachment"
    data-linked-resource-default-alias="image2017-3-9_13-34-38.png"
    data-base-url="https://datamigrators.atlassian.net/wiki"
    data-linked-resource-content-type="image/png"
    data-linked-resource-container-id="116528256"
    data-linked-resource-container-version="8"
    data-media-id="5198b2c9-b332-4fe3-a6f3-30e933922ced"
    data-media-type="file" />

  

  

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2017-3-9_11-50-32.png](attachments/116528256/116528260.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2017-3-9_11-15-36.png](attachments/116528256/116528263.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2017-3-7_16-53-12.png](attachments/116528256/116528266.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2017-3-8_16-56-25.png](attachments/116528256/116528269.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2017-3-8_17-44-41.png](attachments/116528256/116528272.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2017-3-9_13-34-38.png](attachments/116528256/116528345.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2017-3-9_14-22-49.png](attachments/116528256/116528719.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2017-3-9_14-30-36.png](attachments/116528256/116528824.png)
(image/png)  

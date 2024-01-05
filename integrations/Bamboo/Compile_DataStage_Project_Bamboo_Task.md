# Compile DataStage Project Bamboo Task

You can use the Compile DataStage Project task to compile all Jobs,
Sequences, Server Routines and/or QualityStage Rulesets within a
DataStage project.  Compilation results can optionally be added to the
build result as test results.

Task Availability

This task is available after installing the **MettleCI - DataStage
Compiler Plugin** (dm-dscompile-plugin.jar)

## To configure a Compile Datastage Project Task

Steps

1.  Navigate to the **Tasks** configuration tab for the job (this will
    be the default job if creating a new plan).

2.  Click the name of an existing Compile Datastage Project task, or
    click **Add Task** and then search 'Datastage' to easily locate
    the Compile Datastage Project task type, in order to create a new
    task.

3.  Complete the following settings:

    |                                 |                                                                                                                          |
    |---------------------------------|--------------------------------------------------------------------------------------------------------------------------|
    | Task Description                | A description of the task, which is displayed in Bamboo.                                                                 |
    | Disable this task               | Check, or clear, to selectively run this task.                                                                           |
    | Executable                      | From the pulldown list, choose a 'Datastage Capability'                                                                  |
    | Domain                          | Enter the Domain of the Datastage instance (Host Name of the Services Tier)                                              |
    | Server                          | Enter the Server of the Datastage instance (Host Name of the Engine Tier)                                                |
    | Username                        | Enter the Datastage Username                                                                                             |
    | Password                        | Enter the Datastage Password                                                                                             |
    | Project name                    | DataStage Project containing assets to be compiled                                                                       |
    | Max Compile Threads             | How many jobs to compile concurrently.                                                                                   |
    | Parse compilation logs          | If checked, compilation logs are parsed and added as test results. The build will fail if no compilation logs are found. |
    | Skip compiled job               | Check to skip any jobs which are already compiled.                                                                       |
    | Include server routines         | Check, or clear, to selectively compile server routines.                                                                 |
    | Provision QualityStage Rulesets | Check to include QualityStage rule provisioning as part of compilation                                                   |

      
      

4.  Click **Save**  
      

    <img src="attachments/116526376/264012017.png?width=539" loading="lazy"
    data-image-src="attachments/116526376/264012017.png"
    data-unresolved-comment-count="0" data-linked-resource-id="264012017"
    data-linked-resource-version="1" data-linked-resource-type="attachment"
    data-linked-resource-default-alias="image2018-3-29_10-1-1.png"
    data-base-url="https://datamigrators.atlassian.net/wiki"
    data-linked-resource-content-type="image/png"
    data-linked-resource-container-id="116526376"
    data-linked-resource-container-version="12"
    data-media-id="e0b088a0-e7fe-43c1-939d-7af4a2a6932e"
    data-media-type="file" width="539" height="870" />

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2017-3-8_17-44-41.png](attachments/116526376/116526380.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2017-3-8_16-56-25.png](attachments/116526376/116526383.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2017-3-7_16-53-12.png](attachments/116526376/116526386.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2017-3-9_11-15-36.png](attachments/116526376/116526427.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2017-3-9_11-50-32.png](attachments/116526376/116526757.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2018-3-29_10-1-1.png](attachments/116526376/264012017.png)
(image/png)  

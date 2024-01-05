# DataStage Message Handlers Bamboo Task

You can use the DataStage Message Handlers task to inject job level
message handlers into ISX files that then will be imported into
DataStage.

Task Availability

This task is available after installing the **MettleCI - DataStage
Message Handlers Plugin** (dm-dsmsgh-plugin.jar)

  

------------------------------------------------------------------------

## Configuration Steps

1.  Navigate to the **Tasks** configuration tab for the job (this will
    be the default job if creating a new plan).

2.  Click the name of an existing DataStage Message Handlers task, or
    click **Add Task** and then search 'Datastage' to easily locate
    the DataStage Message Handlers task type, in order to create a new
    task.

3.  Complete the following settings:

    |                                |                                                                             |
    |----------------|--------------------------------------------------------|
    | Task Description               | A description of the task, which is displayed in Bamboo.                    |
    | Disable this task              | Check, or clear, to selectively run this task.                              |
    | Root ISX directory             | From the pulldown list, choose a 'Datastage Capability'                     |
    | Root message handler directory | Enter the Domain of the Datastage instance (Host Name of the Services Tier) |

4.  Click **Save**  
    <img src="attachments/412155905/412221441.png?width=560" loading="lazy"
    data-image-src="attachments/412155905/412221441.png"
    data-unresolved-comment-count="0" data-linked-resource-id="412221441"
    data-linked-resource-version="1" data-linked-resource-type="attachment"
    data-linked-resource-default-alias="image2018-6-21_16-21-41.png"
    data-base-url="https://datamigrators.atlassian.net/wiki"
    data-linked-resource-content-type="image/png"
    data-linked-resource-container-id="412155905"
    data-linked-resource-container-version="3"
    data-media-id="046f107f-bbf6-48c4-a877-bb870f5c72ee"
    data-media-type="file" width="560" height="338" />

## See also

<a href="ISX_Message-Handlers_Command"
data-linked-resource-id="412286979" data-linked-resource-version="21"
data-linked-resource-type="page">DataStage Message Handlers CLI</a>

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2018-6-21_16-21-41.png](attachments/412155905/412221441.png)
(image/png)  

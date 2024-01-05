# Properties Configuration Task

You can use the Properties Configuration Task in Bamboo Jobs to replace
specially-formatted text placeholders in DataStage configuration files
(e.g. DSParams) with environment-specific values as part of the
MettleCI-automated deployment process. The replacement values can be
taken from Plan Variables (e.g. ${bamboo.buildResultKey}) and / or
MettleCI Override files.

Placeholders are written in the following format:
*${PlanVariableNameOrOverrideFileReference}*

  

Task Availability

This Task is available after installing the **DataMigrators - Bamboo
Properties Configuration Plugin**

 (dm-bamboo-properties-config-plugin-\<version\>.jar)

## To configure an Properties Configuration Task

Steps

1.  Navigate to the **Tasks** configuration tab for the job (this will
    be the default job if creating a new plan).

2.  Click the name of an existing Properties Configuration Task, or
    click **Add Task** and then search 'Properties Configuration' to
    easily locate the Properties Configuration Task type, in order to
    create a new task.

3.  Complete the following settings:

    <table class="wrapped relative-table confluenceTable"
    style="width: 48.559%;">
    <colgroup>
    <col style="width: 17%" />
    <col style="width: 82%" />
    </colgroup>
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
    <th class="confluenceTh">Base Directory</th>
    <td class="confluenceTd"><p>Optional: A relative path from the working
    directory to the root directory of configuration file(s). This path will
    be the root of file patterns.</p>
    <p>If not specified, the agent working directory will be used</p></td>
    </tr>
    <tr class="even">
    <th class="confluenceTh">File Patterns</th>
    <td class="confluenceTd"><p>Relative paths to different configuration
    files from the base directory (wild card is acceptable). Each line is
    one pattern. </p>
    <p>Examples: </p>
    <p>*.apt<br />
    DSParams<br />
    Parameter Sets/*/*</p></td>
    </tr>
    <tr class="odd">
    <th class="confluenceTh">Override File</th>
    <td class="confluenceTd"><p>Optional: A relative path from the working
    directory to a Java properties file containing variable values to be
    used during substitution.  </p></td>
    </tr>
    <tr class="even">
    <th class="confluenceTh">Output Directory</th>
    <td class="confluenceTd"><p>Optional: A relative path from working
    directory to write all filled configuration files to (all relative path
    from the base directory will be preserved. If output directory is the
    same as base directory, all original configuration files will be
    replaced. </p>
    <p>If not specified, the agent working directory will be used</p></td>
    </tr>
    </tbody>
    </table>

4.  Click **Save  
    <img src="attachments/266862593/273809412.png" loading="lazy"
    data-image-src="attachments/266862593/273809412.png"
    data-unresolved-comment-count="0" data-linked-resource-id="273809412"
    data-linked-resource-version="1" data-linked-resource-type="attachment"
    data-linked-resource-default-alias="image2018-4-12_15-50-53.png"
    data-base-url="https://datamigrators.atlassian.net/wiki"
    data-linked-resource-content-type="image/png"
    data-linked-resource-container-id="266862593"
    data-linked-resource-container-version="8"
    data-media-id="a738165a-eca1-45d7-9c9d-f6f61ad0382b"
    data-media-type="file" />  
    **

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2018-3-29_17-10-1.png](attachments/266862593/266862596.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2018-4-3_11-14-5.png](attachments/266862593/267026463.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2018-4-12_15-50-53.png](attachments/266862593/273809412.png)
(image/png)  

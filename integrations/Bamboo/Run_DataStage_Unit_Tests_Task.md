# Run DataStage Unit Tests Task

You can use the Run DataStage Unit Tests task to execute Unit Test
specification created by the MettleCI Workbench. 

Task Availability

This task is available after installing the **MettleCI - DataStage Unit
Test Plugin** (dm-dstest-plugin.jar)

## To configure an Run DataStage Unit Tests Task

Steps

1.  Navigate to the **Tasks** configuration tab for the job (this will
    be the default job if creating a new plan).

2.  Click the name of an existing Execute Datastage Job task, or click
    **Add Task** and then search 'Datastage' to easily locate the Run
    Datastage Unit Tests task type, in order to create a new task.

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
    <th class="confluenceTh">Specification Directory</th>
    <td class="confluenceTd"><p>Enter the location of Unit Test spec
    directory used by the Unit Tests harness, typically
    <code>/opt/dm/mci/specs/&lt;Project Name&gt;</code>.</p>
    <p>See notes <a href="#RunDataStageUnitTestsTask-remote"
    data-linked-resource-id="512163847" data-linked-resource-version="1"
    data-linked-resource-type="page">below</a> when the Bamboo agent does
    not have direct access to directories on the DataStage engine.</p></td>
    </tr>
    <tr class="even">
    <th class="confluenceTh">Reports Directory</th>
    <td class="confluenceTd"><p>Enter the location of Unit Test reports
    directory which the Unit Tests harness writes to, typically
    <code>/opt/dm/mci/reports/&lt;Project Name&gt;</code>.</p>
    <p>See notes <a href="#RunDataStageUnitTestsTask-remote"
    data-linked-resource-id="512163847" data-linked-resource-version="1"
    data-linked-resource-type="page">below</a> when the Bamboo agent does
    not have direct access to directories on the DataStage engine.</p></td>
    </tr>
    <tr class="odd">
    <th class="confluenceTh">Only test changed jobs?</th>
    <td class="confluenceTd">Skip all tests related to jobs which have not
    changed since the last execution of this task.</td>
    </tr>
    <tr class="even">
    <th class="confluenceTh">Fail build when a Unit Test fails?</th>
    <td class="confluenceTd">Fail the build if any Unit Tests fail.</td>
    </tr>
    <tr class="odd">
    <th class="confluenceTh">Maximum Concurrent Jobs</th>
    <td class="confluenceTd">Specify the maximum number of concurrent jobs
    executed during Unit Testing.</td>
    </tr>
    </tbody>
    </table>

      
      

4.  Click **Save**  
      

    <img src="attachments/512163847/512327701.png" loading="lazy"
    data-image-src="attachments/512163847/512327701.png"
    data-unresolved-comment-count="0" data-linked-resource-id="512327701"
    data-linked-resource-version="1" data-linked-resource-type="attachment"
    data-linked-resource-default-alias="image2020-1-16_13-13-18.png"
    data-base-url="https://datamigrators.atlassian.net/wiki"
    data-linked-resource-content-type="image/png"
    data-linked-resource-container-id="512163847"
    data-linked-resource-container-version="1"
    data-media-id="4d73f61f-35c8-452a-8857-f02cc7e32ca8"
    data-media-type="file" />

## Running Unit Testing without direct access to DataStage engine storage

When the Run DataStage Unit Tests task does not have direct access to
the test specifications and reports directories on the DataStage engine,
the tasks provided by the **MettleCI - SFTP** **Plugin **can be used to
work around this limitation.  Below is a high level overview of running
Unit Test Specifications from a Git repository without direct access to
the Specifications and Reports directories on the DataStage Engine:

<img src="attachments/512163847/512163916.png" loading="lazy"
data-image-src="attachments/512163847/512163916.png"
data-unresolved-comment-count="0" data-linked-resource-id="512163916"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="image2020-1-16_13-35-15.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="512163847"
data-linked-resource-container-version="1"
data-media-id="e4f84e3d-dddd-4e1c-a52a-de31f6775604"
data-media-type="file" />

### Task Execution Description

1.  **Source Code Checkout** is used to checkout the Unit Test
    specifications that have been created by Workbench and checked into
    Git.  These typically reside in the `unittest` directory in the root
    of your Git repository.
2.  **SFTP Upload** recursively transfers the content of the `unittest`
    directory to the remote `/opt/dm/mci/specs/<project name>` directory
    on the DataStage Engine.
3.  **Run DataStage Unit Tests** with the Specifications directory
    option referring to the `unittest` directory created by step 1 and
    the Reports directory set to `test-reports`.  The Fail build when a
    Unit Test fails? option but be unchecked.
4.  **SFTP Download** recursively transfers the content of the remote
    `/opt/dm/mci/reports/<project name>` directory on the DataStage
    engine to the local `test-reports` directory.
5.  **JUnit Parser** is configured to recursively parse all test results
    produced by Steps 3 and 4 using the pattern `test-reports/**/*.xml`

  

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2017-3-9_14-30-36.png](attachments/512163847/512163850.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2017-3-9_14-22-49.png](attachments/512163847/512163853.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2017-3-9_13-34-38.png](attachments/512163847/512163856.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2017-3-8_17-44-41.png](attachments/512163847/512163859.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2017-3-8_16-56-25.png](attachments/512163847/512163862.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2017-3-7_16-53-12.png](attachments/512163847/512163865.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2017-3-9_11-15-36.png](attachments/512163847/512163868.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2017-3-9_11-50-32.png](attachments/512163847/512163871.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2020-1-16_13-13-18.png](attachments/512163847/512327701.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2020-1-16_13-35-15.png](attachments/512163847/512163916.png)
(image/png)  

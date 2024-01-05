# Compliance Test InfoServer Asset Bamboo Task

MettleCI provides a function to evaluate a set of ISX files against
user-defined compliance Rules.  The report that is produced by the
compliance testing function provides details on success or failure of
these tests.  In a CI/CD scenario, this information will determine
whether to continue to the next step of the process.

The Bamboo implementation of the Compliance Test function provides
additional functionality to the command line version:

-   Executes the Compliance Rules and generate the report file
-   Provides an additional option to select a specific set of ISX asset
    files instead of an entire directory
-   Assesses the contents of the report file and optionally halt the
    process in event of failure

  

------------------------------------------------------------------------

## Configuration Steps

1.  Navigate to the **Tasks** configuration tab for the job (this will
    be the default job if creating a new plan).

2.  Click the name of an existing Datastage Admin task, or click **Add
    Task** and then search 'Datastage' to easily locate the Datastage
    Admin task type, in order to create a new task.

3.  <table class="wrapped confluenceTable">
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
    <th class="confluenceTh">Compliance rule directory</th>
    <td class="confluenceTd">Directory containing Compliance Rule (*.grm)
    files.</td>
    </tr>
    <tr class="even">
    <th class="confluenceTh">Compliance Test type</th>
    <td class="confluenceTd"><p>The type of compliance test to run:</p>
    <ul>
    <li>Entire Directory - Recursively compliance test all ISX files in a
    given directory</li>
    <li>File List - Selectively compliance test ISX files in a given
    directory based on a list</li>
    </ul></td>
    </tr>
    <tr class="odd">
    <th class="confluenceTh">Root ISX directory</th>
    <td class="confluenceTd">Root of a directory structure containing ISX
    files for compliance testing. </td>
    </tr>
    <tr class="even">
    <th class="confluenceTh">List file name</th>
    <td class="confluenceTd"><p>Path to file containing a list of ISX files
    to compliance test. ISX file names are expected to be relative to the
    Root ISX directory.</p>
    <p>Only shown when Compliance Test type is "File List".</p></td>
    </tr>
    <tr class="odd">
    <th class="confluenceTh">Fail build when a Compliance Test fails?</th>
    <td class="confluenceTd">Check this option to have the Bamboo build fail
    when at least one compliance test fails</td>
    </tr>
    <tr class="even">
    <th class="confluenceTh"><br />
    </th>
    <td class="confluenceTd"><br />
    </td>
    </tr>
    </tbody>
    </table>

4.  Click **Save**

<img src="attachments/408322090/408518662.png?width=532" loading="lazy"
data-image-src="attachments/408322090/408518662.png"
data-unresolved-comment-count="0" data-linked-resource-id="408518662"
data-linked-resource-version="1" data-linked-resource-type="attachment"
data-linked-resource-default-alias="image2018-4-3_11-19-8.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="408322090"
data-linked-resource-container-version="5"
data-media-id="097e7ece-616a-4091-a59c-b149f2162a67"
data-media-type="file" width="532" height="475" />

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2018-4-3_11-19-8.png](attachments/408322090/408518662.png)
(image/png)  

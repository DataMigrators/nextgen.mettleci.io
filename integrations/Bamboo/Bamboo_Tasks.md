# Bamboo Tasks

MettleCI includes an array of Tasks that can be used within your Bamboo
Plans and Deployments.  MettleCI's build and deployment tasks are are
delivered as Bamboo Plugins, and are described below.  Please refer to
the <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/264110081/User+Guides"
data-linked-resource-id="264110081" data-linked-resource-version="12"
data-linked-resource-type="page">User Guides</a> section for
recommendations about how these can be used to support specific
processes.

<table class="confluenceTable" data-layout="full-width"
data-local-id="efe34a73-4fc4-48ca-8130-82a74c5437b7">
<tbody>
<tr class="header">
<th class="confluenceTh"><p>Plugin Name</p></th>
<th class="confluenceTh"><p>Deployed Component</p></th>
<th class="confluenceTh"><p>Components Included</p></th>
</tr>
&#10;<tr class="odd">
<td class="confluenceTd"><p><strong>Bamboo Build
Deltas</strong></p></td>
<td class="confluenceTd"><p>dm-bamboo-delta-plugin.jar</p></td>
<td class="confluenceTd"><p><a href="Build_Commit_Log_Bamboo_Task"
data-linked-resource-id="116471927" data-linked-resource-version="19"
data-linked-resource-type="page"><strong>Build Commit Log
Task</strong></a> <strong></strong> - Builds a log file containing a
list of files that have changed in a given repository since the last
successful build</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p><strong>Bamboo Properties
Configuration</strong></p></td>
<td
class="confluenceTd"><p>dm-bamboo-properties-config-plugin.jar</p></td>
<td class="confluenceTd"><p><a href="Properties_Configuration_Task"
data-linked-resource-id="266862593" data-linked-resource-version="8"
data-linked-resource-type="page"><strong>Properties Configuration
Task</strong></a> - Substitute ${variable} placeholders in config files
with environment specific values from plan variables and override
files.</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p><strong>Bamboo SFTP</strong></p></td>
<td class="confluenceTd"><p>dm-bamboo-sftp-plugin.jar</p></td>
<td class="confluenceTd"><p><a href="SFTP_Download_Bamboo_Task"
data-linked-resource-id="499220487" data-linked-resource-version="3"
data-linked-resource-type="page"><strong>SFTP Download Bamboo
Task</strong></a> - Transfer files from a remote server to the local
working directory</p>
<p><a href="SFTP_Upload_Bamboo_Task" data-linked-resource-id="499056670"
data-linked-resource-version="3"
data-linked-resource-type="page"><strong>SFTP Upload Bamboo
Task</strong></a> - Transfer files in the local working directory to a
remote server</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p><strong>Compliance</strong></p></td>
<td class="confluenceTd"><p>dm-compliance-plugin.jar</p></td>
<td class="confluenceTd"><p><a
href="Compliance_Test_InfoServer_Asset_Bamboo_Task"
data-linked-resource-id="408322090" data-linked-resource-version="5"
data-linked-resource-type="page"><strong>Compliance Test InfoServer
Asset Task</strong></a> - Tests a set of ISX files against user defined
compliance rules.</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p><strong>DataStage
Administration</strong></p></td>
<td class="confluenceTd"><p>dm-dsadmin-plugin.jar</p></td>
<td class="confluenceTd"><p><a href="DataStage_Admin_Bamboo_Task"
data-linked-resource-id="408387649" data-linked-resource-version="9"
data-linked-resource-type="page"><strong>DataStage Admin Bamboo
Task</strong></a> - Create or delete DataStage Projects.</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p><strong>DataStage Compiler</strong></p></td>
<td class="confluenceTd"><p>dm-dscompile-plugin.jar</p></td>
<td class="confluenceTd"><p><a
href="Compile_DataStage_Project_Bamboo_Task"
data-linked-resource-id="116526376" data-linked-resource-version="12"
data-linked-resource-type="page"><strong>Compile DataStage Project
Task</strong></a> - Compiles all compilable assets within a DataStage
project.</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p><strong>DataStage
Deployment</strong></p></td>
<td class="confluenceTd"><p>dm-dsdeploy-plugin.jar</p></td>
<td class="confluenceTd"><p><a href="Incremental_Deployment_Bamboo_Task"
data-linked-resource-id="264962064" data-linked-resource-version="4"
data-linked-resource-type="page"><strong>Incremental DataStage
Deployment Task</strong></a> - Intelligently provision an entire
directory of ISX files to an existing DataStage Project using the
minimum number of delta operations.  </p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p><strong>DataStage Execute</strong></p></td>
<td class="confluenceTd"><p>dm-dsexecute-plugin.jar</p></td>
<td class="confluenceTd"><p><a href="Execute_DataStage_Job_Bamboo_Task"
data-linked-resource-id="116528256" data-linked-resource-version="8"
data-linked-resource-type="page"><strong>Execute DataStage Job
Task</strong></a><strong> </strong>- Execute a DataStage job or
sequence.</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p><strong>DataStage Message
Handler</strong></p></td>
<td class="confluenceTd"><p>dm-dsmessagehandler-plugin.jar</p></td>
<td class="confluenceTd"><p><a
href="DataStage_Message_Handlers_Bamboo_Task"
data-linked-resource-id="412155905" data-linked-resource-version="3"
data-linked-resource-type="page"><strong>DataStage Message Handler
Task</strong></a> - Inject job-level message handlers into ISX files
that will then will be imported into DataStage.</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p><strong>Git</strong></p></td>
<td class="confluenceTd"><p>dm-git-plugin.jar</p></td>
<td class="confluenceTd"><p><a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/116537387/Git+Bamboo+Task"
data-linked-resource-id="116537387" data-linked-resource-version="16"
data-linked-resource-type="page"><strong>Git Bamboo
Task</strong></a> - Perform Git operations (Clone, Checkin, Pull, Tag,
Branch) which extend Bamboo's capabilities.</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p><strong>ISX Export</strong></p></td>
<td class="confluenceTd"><p>dm-isxexport-plugin.jar</p></td>
<td class="confluenceTd"><p><a href="Export_DataStage_Asset_Bamboo_Task"
data-linked-resource-id="409305095" data-linked-resource-version="3"
data-linked-resource-type="page"><strong>Export DataStage Asset
Task</strong></a> - Export DataStage assets (specified by name, list or
entire project) as individual ISX files in a folder structure matching
the project.</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p><strong>ISX Import</strong></p></td>
<td class="confluenceTd"><p>dm-isximport-plugin.jar</p></td>
<td class="confluenceTd"><p><a
href="Import_DataStage_Asset_-_Bamboo_Task"
data-linked-resource-id="409796627" data-linked-resource-version="1"
data-linked-resource-type="page"><strong>Import DataStage Asset
Task</strong></a> - Import ISX files (either specific files, a list of
files, or an entire directory) into an existing DataStage
project.</p></td>
</tr>
</tbody>
</table>

  
Note that MettleCI plugins also provide some Bamboo configuration pages:

|                          |                                    |                                                                                                                                                                                       |
|--------------------------|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Plugin name              | Deployed Component                 | Components Included                                                                                                                                                                   |
| **Bamboo License Admin** | dm-bamboo-license-admin-plugin.jar | <a                                                                                                                                                                                    
                                                                 href="https://datamigrators.atlassian.netnull/pages/createpage.action?spaceKey=MCIDOC&amp;title=Bamboo%20MettleCI%20License%20Details&amp;linkCreation=true&amp;fromPageId=264241153"  
                                                                 rel="nofollow"><strong>License Details Admin Page</strong></a> - Inserts MettleCI License                                                                                              |

  

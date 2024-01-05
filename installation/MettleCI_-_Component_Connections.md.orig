# MettleCI - Component Connections

## Component Connections

The following table describes which interactions take place between the
software components listed above, and which functions those interactions
support.  Note that if a component or protocol isn't specified then it’s
either irrelevant to MettleCI, or MettleCI can re-use whatever your
infrastructure dictates.

<table class="confluenceTable" data-layout="default"
data-local-id="1e76c455-b752-4b96-ad41-2fec57fc15ab">
<tbody>
<tr class="header">
<th class="confluenceTh"><p><strong>Connection</strong></p></th>
<th class="confluenceTh"><p><strong>First Host -
Application</strong></p></th>
<th class="confluenceTh"><p><strong>Second Host -
Application</strong></p></th>
<th class="confluenceTh"><p><strong>Protocol(s)</strong></p></th>
<th class="confluenceTh"><p><strong>Authentication</strong></p></th>
<th class="confluenceTh"><p><strong>Related MettleCI
Function(s)</strong></p></th>
<th class="confluenceTh"><p><strong>Comments</strong></p></th>
</tr>
&#10;<tr class="odd">
<td class="confluenceTd"><p><strong>1</strong></p></td>
<td class="confluenceTd"><p>DataStage
Development <strong>Engine</strong> Tier - MettleCI Workbench
Service</p></td>
<td class="confluenceTd"><p>Git Host - Git service</p></td>
<td class="confluenceTd"><p>SSH (default), HTTP(S)</p></td>
<td class="confluenceTd"><p>Git user credentials.</p>
<p>See relevant build tool pages <a
href="https://datamigrators.atlassian.net/wiki/label/MCIDOC/authentication"
rel="nofollow">here</a>.</p></td>
<td class="confluenceTd"><p>Commit</p></td>
<td class="confluenceTd"><p>See <a
href="Configuring_MettleCI_Workbench_to_communicate_with_Git_over_HTTPS"
data-linked-resource-id="1745747969" data-linked-resource-version="25"
data-linked-resource-type="page">Configuring MettleCI Workbench to
communicate with Git over HTTPS</a></p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p><strong>2</strong></p></td>
<td class="confluenceTd"><p>DataStage
Development <strong>Engine</strong> Tier - MettleCI Workbench
service</p></td>
<td class="confluenceTd"><p>Work item Management Host - Work Item
Management service</p></td>
<td class="confluenceTd"><p>Work item Management
service-dependent</p></td>
<td class="confluenceTd"><p>Work item Management service’s API. See
relevant pages <a
href="https://datamigrators.atlassian.net/wiki/label/MCIDOC/work-item-management"
rel="nofollow">here</a>.</p></td>
<td class="confluenceTd"><p>Dynamic Work item lookup during
Commit</p></td>
<td class="confluenceTd"><p>'Work Item Management service' means Jira,
Service Now, etc. The ports and protocols depend upon your selected
tool. See <a
href="https://datamigrators.atlassian.net/wiki/label/MCIDOC/authentication+work-item-management"
rel="nofollow">these pages</a> for more details.</p></td>
</tr>
<tr class="odd">
<td rowspan="3" class="confluenceTd"><p><strong>3</strong></p></td>
<td class="confluenceTd"><p>Developer Workstation - Web browser</p></td>
<td class="confluenceTd"><p>Git Host - Git service</p></td>
<td class="confluenceTd"><p>HTTP(S)</p></td>
<td class="confluenceTd"><p>Git user credentials</p></td>
<td class="confluenceTd"><p>Git tasks</p></td>
<td class="confluenceTd"></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>Developer Workstation - Web browser</p></td>
<td class="confluenceTd"><p>Work item Management Host - Work Item
Management service</p></td>
<td class="confluenceTd"><p>HTTP(S)</p></td>
<td class="confluenceTd"><p>Work Item Management user
credentials</p></td>
<td class="confluenceTd"><p>Work Item Management tasks</p></td>
<td class="confluenceTd"></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>Developer Workstation - Web browser</p></td>
<td class="confluenceTd"><p>Build Host - Build Tool controller</p></td>
<td class="confluenceTd"><p>HTTP(S)</p></td>
<td class="confluenceTd"><p>Build tool user credentials</p></td>
<td class="confluenceTd"><p>Build tasks</p></td>
<td class="confluenceTd"></td>
</tr>
<tr class="even">
<td rowspan="2" class="confluenceTd"><p><strong>4</strong></p></td>
<td class="confluenceTd"><p>Developer Workstation - Web browser</p></td>
<td class="confluenceTd"><p>DataStage Development
<strong>Engine</strong> Tier - MettleCI Workbench Service</p></td>
<td class="confluenceTd"><p>HTTP(S)</p></td>
<td class="confluenceTd"><p>DataStage user credentials</p></td>
<td class="confluenceTd"><ul>
<li><p>All MettleCI Workbench functionality</p>
<ul>
<li><p>Compliance</p></li>
<li><p>Test</p></li>
<li><p>Commit</p></li>
</ul></li>
</ul></td>
<td class="confluenceTd"><p>Ports are configurable in the MettleCI
configuration file.</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>Developer Workstation - Web browser</p></td>
<td class="confluenceTd"><p>DataStage Development
<strong>Engine</strong> Tier - MettleCI Workbench Service</p></td>
<td class="confluenceTd"><p>SSH</p></td>
<td class="confluenceTd"><p>DataStage Development
<strong>Engine</strong> Tier O/S user credentials</p></td>
<td class="confluenceTd"><ul>
<li><p>Filesystem asset version control</p></li>
<li><p>Non Information Server (ISX) asset version control</p></li>
</ul></td>
<td class="confluenceTd"><p>OPTIONAL </p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p><strong>5</strong></p></td>
<td class="confluenceTd"><p>Developer Workstation - Remote
Desktop</p></td>
<td class="confluenceTd"><p>MettleCI Agent Host - Microsoft
Windows</p></td>
<td class="confluenceTd"><p>RDP</p></td>
<td class="confluenceTd"><p>MS Windows</p></td>
<td class="confluenceTd"><p>Configuration and diagnostics</p></td>
<td class="confluenceTd"><p>OPTIONAL  </p>
<p>Required during setup, but Developers shouldn’t require this access
on a day-to-day basis.</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p><strong>6</strong></p></td>
<td class="confluenceTd"><p>Built Host - Build Tool Controller</p></td>
<td class="confluenceTd"><p>MettleCI Agent Host - Built Tool
Agent</p></td>
<td class="confluenceTd"><p>Build tool dependent</p></td>
<td class="confluenceTd"><p>Build tool dependent</p></td>
<td class="confluenceTd"><p>Build Controller can execute pipelines
requiring a ‘MettleCI Command Line Interface’ capability</p></td>
<td class="confluenceTd"><p>See the documentation of your chosen build
tool</p></td>
</tr>
<tr class="even">
<td rowspan="2" class="confluenceTd"><p><strong>7</strong></p></td>
<td class="confluenceTd"><p>MettleCI Agent Host - Built Tool
Agent</p></td>
<td class="confluenceTd"><p>DataStage Development
<strong>Engine</strong> Tier</p></td>
<td class="confluenceTd"><p>DataStage (IBM-specified), SCP, SSH</p></td>
<td class="confluenceTd"><p>DataStage user credentials.</p>
<p>Various authentication mechanisms required by each MettleCI Commands.
See <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/458850547/MettleCI+Command+Line+Reference"
data-linked-resource-id="458850547" data-linked-resource-version="58"
data-linked-resource-type="page">this page</a> for details on each
command.</p></td>
<td class="confluenceTd"><ul>
<li><p>MettleCI Deployment (via SCP)</p></li>
<li><p>Script Execution (via SSH)</p></li>
</ul></td>
<td class="confluenceTd"><p>This link will use the same ports and
protocols that the customer uses for its standard installation of the
DataStage Client on end-user hardware, as well as SCP and SSH for
certain <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/458850547/MettleCI+Command+Line+Reference"
data-linked-resource-id="458850547" data-linked-resource-version="58"
data-linked-resource-type="page">MettleCI Commands</a>.</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>MettleCI Agent Host - DataStage Client
Tools</p></td>
<td class="confluenceTd"><p>DataStage Development
<strong>Services</strong> and <strong>Engine</strong> Tiers</p></td>
<td class="confluenceTd"><p>DataStage (IBM-specified)</p></td>
<td class="confluenceTd"><p>IBM-specified</p></td>
<td class="confluenceTd"><p>Normal DataStage Client operations</p></td>
<td class="confluenceTd"><p>This link will use the same ports and
protocols that the customer uses for its standard installation of the
DataStage Client on end-user hardware.</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p><strong>8</strong></p></td>
<td class="confluenceTd"><p>MettleCI Agent Host - Built Tool
Agent</p></td>
<td class="confluenceTd"><p>DataStage Testing (and potentially
Production) <strong>Services</strong> and <strong>Engine</strong>
Tiers</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>DataStage user credentials.</p>
<p>Various authentication mechanisms required by each MettleCI Commands.
See <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/458850547/MettleCI+Command+Line+Reference"
data-linked-resource-id="458850547" data-linked-resource-version="58"
data-linked-resource-type="page">this page</a> for details on each
command.</p></td>
<td class="confluenceTd"><ul>
<li><p>Normal DataStage Client operations</p></li>
<li><p>MettleCi Deployment (via SCP)</p></li>
<li><p>Script Execution (via SSH)</p></li>
</ul></td>
<td class="confluenceTd"><p>This link will use the same ports and
protocols that the customer uses for its standard installation of the
DataStage Client on end-user hardware.</p></td>
</tr>
</tbody>
</table>

  

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[MettleCI topology (simplified) Copy
Copy](attachments/1122500829/2097184789) (application/gliffy+json)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[MettleCI topology (simplified) Copy
Copy.png](attachments/1122500829/2096136296.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[MettleCI topology (simplified)
Connections](attachments/1122500829/2097315853)
(application/gliffy+json)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[MettleCI topology (simplified)
Connections.png](attachments/1122500829/2097446923.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[MettleCI topology (simplified)
Connections](attachments/1122500829/2348253194)
(application/gliffy+json)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[MettleCI topology (simplified)
Connections.png](attachments/1122500829/2348318725.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[MettleCI topology (simplified)
Connections](attachments/1122500829/2097479683)
(application/gliffy+json)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[MettleCI topology (simplified)
Connections.png](attachments/1122500829/2096136301.png) (image/png)  

# MettleCI Command Line Reference

Refer to the <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/408354840/MettleCI+CLI+Operating+Modes"
data-linked-resource-id="408354840" data-linked-resource-version="47"
data-linked-resource-type="page">MettleCI Command Line Interface</a> to
understand how the interface works, and what each of the columns in the
table below means.

Refer to the <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/264110081/User+Guides"
data-linked-resource-id="264110081" data-linked-resource-version="12"
data-linked-resource-type="page">User Guides</a> section for
recommendations about how these can be used to support specific
processes.

# Available Namespaces

-   <a href="Compliance_Namespace" data-linked-resource-id="2262990849"
    data-linked-resource-version="3"
    data-linked-resource-type="page">Compliance Namespace</a>
-   <a href="DataStage_Namespace" data-linked-resource-id="2263056385"
    data-linked-resource-version="3"
    data-linked-resource-type="page">DataStage Namespace</a>
-   <a href="Deploy_Namespace" data-linked-resource-id="2263056437"
    data-linked-resource-version="1" data-linked-resource-type="page">Deploy
    Namespace</a>
-   <a href="DSParams_Namespace" data-linked-resource-id="2263056424"
    data-linked-resource-version="2"
    data-linked-resource-type="page">DSParams Namespace</a>
-   <a href="ISX_Namespace" data-linked-resource-id="2263056398"
    data-linked-resource-version="3" data-linked-resource-type="page">ISX
    Namespace</a>
-   <a href="Properties_Namespace" data-linked-resource-id="2262990862"
    data-linked-resource-version="2"
    data-linked-resource-type="page">Properties Namespace</a>
-   <a href="RDU-Backlog_Namespace_⛔️" data-linked-resource-id="2263056450"
    data-linked-resource-version="2"
    data-linked-resource-type="page">RDU-Backlog Namespace ⛔️</a>
-   <a href="Remote_Namespace" data-linked-resource-id="2262794241"
    data-linked-resource-version="4" data-linked-resource-type="page">Remote
    Namespace</a>
-   <a href="UnitTest_Namespace" data-linked-resource-id="2263056411"
    data-linked-resource-version="1"
    data-linked-resource-type="page">UnitTest Namespace</a>
-   <a href="🔒_Railroad_Diagrams_Specifications"
    data-linked-resource-id="455311472" data-linked-resource-version="36"
    data-linked-resource-type="page">🔒 Railroad Diagrams Specifications</a>

# Available Commands

| Command Documentation                                                                                              | Namespace   | Command          | Plugin Name | Plugin File                     | Credentials | Windows Client |
|--------------------------------------------------------------------------------------------------------------------|-------------|------------------|-------------|---------------------------------|-------------|----------------|
| [RDU-Backlog API command ⛔️](/wiki/spaces/MCIDOC/pages/458522681)                                                  | rdu-backlog | api              | rdu-backlog | dm-backlog-generator.jar        | JIRA        | \-             |
| [ISX Cat Command](/wiki/spaces/MCIDOC/pages/458784837/ISX+Cat+Command)                                             | isx         | cat              | isx         | dm-isxexport-plugin.jar         | \-          | \-             |
| [DataStage Connector Migration Command](/wiki/spaces/MCIDOC/pages/410681364/DataStage+Connector+Migration+Command) | datastage   | ccmt             | datastage   | dm-ccmigrate-plugin.jar         | IS/DS       | Y              |
| [DataStage Cleanup-Projects Command](/wiki/spaces/MCIDOC/pages/458424418/DataStage+Cleanup-Projects+Command)       | datastage   | cleanup-projects | datastage   | dm-dsadmin-plugin.jar           | IS/DS       | \-             |
| [DataStage Compile Command](/wiki/spaces/MCIDOC/pages/410157081/DataStage+Compile+Command)                         | datastage   | compile          | datastage   | dm-dscompile-plugin.jar         | IS/DS       | Y              |
| [Properties Config Command](/wiki/spaces/MCIDOC/pages/718962693/Properties+Config+Command)                         | properties  | config           | properties  | dm-properties-config-plugin.jar | \-          | \-             |
| [DataStage Create-Project Command](/wiki/spaces/MCIDOC/pages/408420417/DataStage+Create-Project+Command)           | datastage   | create-project   | datastage   | dm-dsadmin-plugin.jar           | IS/DS       | \-             |
| [RDU-Backlog CSV Command ⛔️](/wiki/spaces/MCIDOC/pages/430342145)                                                  | rdu-backlog | csv              | rdu-backlog | dm-backlog-generator.jar        | \-          | \-             |
| [ISX Cut Command](/wiki/spaces/MCIDOC/pages/458817574/ISX+Cut+Command)                                             | isx         | cut              | isx         | dm-isxexport-plugin.jar         | \-          | \-             |
| [DataStage Delete-Project Command](/wiki/spaces/MCIDOC/pages/458424387/DataStage+Delete-Project+Command)           | datastage   | delete-project   | datastage   | dm-dsadmin-plugin.jar           | IS/DS       | \-             |
| [DSParams Delete Command](/wiki/spaces/MCIDOC/pages/458556054/DSParams++Delete+Command)                            | dsparams    | delete           | dsparams    | dm-dsadmin-plugin.jar           | \-          | \-             |
| [DataStage Deploy Command](/wiki/spaces/MCIDOC/pages/423952410/DataStage+Deploy+Command)                           | datastage   | deploy           | datastage   | dm-dsdeploy-plugin.jar          | IS/DS       | Y              |
| [Deploy DevOps-Pipeline Command](/wiki/spaces/MCIDOC/pages/549225052/Deploy+DevOps-Pipeline+Command)               | deploy      | devops-pipeline  | deploy      | dm-command-bamboo-plugin.jar    | IS/DS       | \-             |
| [DSParams Diff Command](/wiki/spaces/MCIDOC/pages/458785100/DSParams++Diff+Command)                                | dsparams    | diff             | dsparams    | dm-dsadmin-plugin.jar           | \-          | \-             |
| [Remote Download Command](/wiki/spaces/MCIDOC/pages/716636187/Remote+Download+Command)                             | remote      | download         | remote      | dm-bamboo-sftp-plugin.jar       | OS          | \-             |
| [Remote Execute Command](/wiki/spaces/MCIDOC/pages/784367633/Remote+Execute+Command)                               | remote      | execute          | remote      | dm-bamboo-sftp-plugin.jar       | OS          | \-             |
| [DataStage Execute Command](/wiki/spaces/MCIDOC/pages/458817755/DataStage+Execute+Command)                         | datastage   | execute          | datastage   | dm-dsexecute-plugin.jar         | IS/DS       | \-             |
| [ISX Export Command](/wiki/spaces/MCIDOC/pages/409305099/ISX+Export+Command)                                       | isx         | export           | isx         | dm-isxexport-plugin.jar         | IS/DS       | Y              |
| [ISX Import Command](/wiki/spaces/MCIDOC/pages/409894937/ISX+Import+Command)                                       | isx         | import           | isx         | dm-isximport-plugin.jar         | IS/DS       | Y              |
| [DSParams Merge Command](/wiki/spaces/MCIDOC/pages/458556064/DSParams+Merge+Command)                               | dsparams    | merge            | dsparams    | dm-dsadmin-plugin.jar           | \-          | \-             |
| [ISX Message-Handlers Command](/wiki/spaces/MCIDOC/pages/412286979/ISX+Message-Handlers+Command)                   | isx         | message-handlers | isx         | dm-dsmsgh-plugin.jar            | \-          | \-             |
| [Compliance Query Command](/wiki/spaces/MCIDOC/pages/458556115/Compliance+Query+Command)                           | compliance  | query            | compliance  | dm-compliance-plugin.jar        | \-          | \-             |
| [Compliance ReportCard Command ⛔️](/wiki/spaces/MCIDOC/pages/720994614)                                            | compliance  | reportcard       | compliance  | dm-complexity-report jar        | \-          | \-             |
| [ISX Set-Params Command](/wiki/spaces/MCIDOC/pages/458850355/ISX+Set-Params+Command)                               | isx         | set-params       | isx         | dm-isxexport-plugin.jar         | \-          | \-             |
| [UnitTest Test Command](/wiki/spaces/MCIDOC/pages/718831617/UnitTest+Test+Command)                                 | unittest    | test             | unittest    | dm-dstest-plugin.jar            | IS/DS       | \-             |
| [Compliance Test Command](/wiki/spaces/MCIDOC/pages/408322069/Compliance+Test+Command)                             | compliance  | test             | compliance  | dm-compliance-plugin.jar        | \-          | \-             |
| [UnitTest Generate Command](/wiki/spaces/MCIDOC/pages/2176647169/UnitTest+Generate+Command)                        | unittest    | test             | unittest    | dm-dstest-plugin.jar            | IS/DS       | \-             |
| [Compliance UnitTest Command ⛔️](/wiki/spaces/MCIDOC/pages/2236350465)                                             | compliance  | unittest         | compliance  | dm-compliance-plugin.jar        | \-          | \-             |
| [Remote Upload Command](/wiki/spaces/MCIDOC/pages/716603405/Remote+Upload+Command)                                 | remote      | upload           | remote      | dm-bamboo-sftp-plugin.jar       | OS          | \-             |

Some command invocations will require credentials. For more on
credentials, see <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/1109491875/MettleCI+-+User+Accounts"
data-linked-resource-id="1109491875" data-linked-resource-version="6"
data-linked-resource-type="page">Mettle CI User Accounts</a>.

## Types of credentials

|          |                                                                                                                                                                                              |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Code** | **Meaning**                                                                                                                                                                                  |
| IS/DS    | This command requires credentials of an IS user that has the DataStage Admin permission and is bound/mapped to a valid DataStage user                                                        |
| OS       | This command requires credentials of an Operating System user that has sufficient authority to ssh/scp and to write in the project and other project related directories and invoke scripts. |
| IGC      | This command requires credentials of an IGC user (an IS user that has IGC user permissions)                                                                                                  |
| JIRA     | This command requires credentials of an Atlassian Jira user that has sufficient permission to create, view and delete issues and comments.                                                   |
| \-       | This command does not need any credentials                                                                                                                                                   |

# Windows-Only Commands

Note from the ‘Windows Client’ column of the command list above that the
following MettleCI commands rely on functionality only available on the
DataStage Client tier, and as such can only be executed on a
Windows-based DataStage Client tier.

| Title                                                                                                              | Namespace | Command | Credentials |
|--------------------------------------------------------------------------------------------------------------------|-----------|---------|-------------|
| [DataStage Compile Command](/wiki/spaces/MCIDOC/pages/410157081/DataStage+Compile+Command)                         | datastage | compile | IS/DS       |
| [DataStage Connector Migration Command](/wiki/spaces/MCIDOC/pages/410681364/DataStage+Connector+Migration+Command) | datastage | ccmt    | IS/DS       |
| [DataStage Deploy Command](/wiki/spaces/MCIDOC/pages/423952410/DataStage+Deploy+Command)                           | datastage | deploy  | IS/DS       |
| [ISX Export Command](/wiki/spaces/MCIDOC/pages/409305099/ISX+Export+Command)                                       | isx       | export  | IS/DS       |
| [ISX Import Command](/wiki/spaces/MCIDOC/pages/409894937/ISX+Import+Command)                                       | isx       | import  | IS/DS       |

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-10-25_22-51-19.png](attachments/458850547/458850550.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-10-22_13-35-5.png](attachments/458850547/458850553.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-10-22_13-3-50.png](attachments/458850547/458850556.png)
(image/png)  

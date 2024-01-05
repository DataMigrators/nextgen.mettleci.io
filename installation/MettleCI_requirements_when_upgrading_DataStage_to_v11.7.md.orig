# MettleCI requirements when upgrading DataStage to v11.7

When upgrading to the latest non-Cloud Pak version of DataStage you’ll
wonder which MettleCI tools and assets need to be upgraded, replaced, or
reconfigured, and which can be safely left in place. This page discusses
the technical aspects of re-configuration and will deliberately omit the
important project management aspects of handling a cutover between old
and new DataStage environments.

# Affected Components

-   **MettleCI Workbench:** As this is installed on your DataStage
    Engine tier you’ll need a new installation of this on your new
    DataStage v11.7 Engine.

-   **MettleCI Unit Test Harness: An agent integrated into Customer’s
    DataStage Engine which selectively modifies DataStage job
    definitions at runtime to provide data interception and unit test
    execution capabilities.**

-   **MettleCI Command Line Interface (CLI):** The MettleCI Command Line
    Interface works with all in-support versions of DataStage but
    because it lives on the MettleCI Build host**.** As this is
    effectively a client tier (for dedicated use by your build tool)
    this will require a new host containing…

    -   a new v11.7 DataStage client

    -   an instance of the build tool’s agent

    -   an instance of the MettleCI CLI

Your ALM (Application Lifecycle Management) platform - Git, Work Item
Management, and Build tools - would remain as is, but you’d establish
new DataStage asset repositories along with associated build pipelines,
and (potentially) new work item projects.

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[ihgk](attachments/2193358849/2193227779) (application/gliffy+json)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[ihgk.png](attachments/2193358849/2193719297.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[ihgk](attachments/2193358849/2195488769) (application/gliffy+json)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[ihgk.png](attachments/2193358849/2195292165.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[ihgk](attachments/2193358849/2195521541) (application/gliffy+json)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[ihgk.png](attachments/2193358849/2195554305.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[ihgk](attachments/2193358849/2195554315) (application/gliffy+json)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[ihgk.png](attachments/2193358849/2195521551.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[ihgk](attachments/2193358849/2325905449) (application/gliffy+json)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[ihgk.png](attachments/2193358849/2325774389.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[ihgk](attachments/2193358849/2193195012) (application/gliffy+json)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[ihgk.png](attachments/2193358849/2193588225.png) (image/png)  

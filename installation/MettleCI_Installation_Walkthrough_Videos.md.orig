# MettleCI Installation Walkthrough Videos

# Assumptions

This page will provide an illustrated walk through of the installation
and configuration of MettleCI’s components on a simple DataStage v11.7
topology using a Unix Engine tier. It is geared towards users who have
seen the
<a href="https://www.youtube.com/watch?v=QnZW68zdegU&amp;t=1719s"
rel="nofollow">MettleCI demo video</a> and have some understanding of
how the following functions are accessed and used…

-   MettleCI Workbench (including DataStage Designer menus)

-   MettleCI Compliance

-   MettleCI Unit testing

-   MettleCI Git Commit (including Work Item lookup)

# Contents

-   [Topology](#MettleCIInstallationWalkthroughVideos-Topology)
-   [Introduction and
    Prerequisites](#MettleCIInstallationWalkthroughVideos-IntroductionandPrerequisites)
-   [Install MettleCI
    Workbench](#MettleCIInstallationWalkthroughVideos-InstallMettleCIWorkbench)
-   [Deploy Git Repositories and Register Workbench
    Project](#MettleCIInstallationWalkthroughVideos-DeployGitRepositoriesandRegisterWorkbenchProject)
-   [DataStage Designer
    Menus](#MettleCIInstallationWalkthroughVideos-DataStageDesignerMenus)
-   [Define Work Item Management
    System](#MettleCIInstallationWalkthroughVideos-DefineWorkItemManagementSystem)
-   [Install Unit Test
    Harness](#MettleCIInstallationWalkthroughVideos-InstallUnitTestHarness)
-   [Onboarding a DataStage Project into
    Git](#MettleCIInstallationWalkthroughVideos-OnboardingaDataStageProjectintoGit)

------------------------------------------------------------------------

# Topology

------------------------------------------------------------------------

# Introduction and Prerequisites

-   Support resources

-   Scope

-   Introduce installation demo environment

-   Acquiring MettleCI download assets

-   Introducing the MettleCI download assets

    -   Data Migrators Customers

    -   IBM Customers **(**<a
        href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/2244149314/MettleCI+IBM+OEM+Release+History"
        data-linked-resource-id="2244149314" data-linked-resource-version="13"
        data-linked-resource-type="page"><strong>link</strong></a>**)**

-   Install OpenJDK v8 (non-IBM JVM)
    **(**<a href="Prerequisite_Java_Installation"
    data-linked-resource-id="488800406" data-linked-resource-version="24"
    data-linked-resource-type="page"><strong>link</strong></a>**)**

    -   On the DataStage Engine (for MettleCI Workbench)

    -   On the Agent Host (for MettleCI CLI)

    -   WINDOWS Using `.msi` installer (not demonstrated)

    -   UNIX Using package manager(e.g., `yum`)

**Running time:** 17m 00s

------------------------------------------------------------------------

# Install MettleCI Workbench

-   Install Workbench Service

    -   WINDOWS Using `.msi` within `.zip` file (not demonstrated)

    -   UNIX Using `.rpm` file

-   Deploy `mettleci.lic` license file

    -   Rename from `license.txt`

-   HTTPS Configuration
    **(**<a href="Configuring_MettleCI_Workbench_to_use_HTTPS"
    data-linked-resource-id="458556297" data-linked-resource-version="56"
    data-linked-resource-type="page"><strong>link</strong></a>**)**

    -   Generate Java KeyStore

    -   Update `config.yml` to add `Server` section, then restart
        Workbench service

    -   Add certificate to Windows client and restart browser

**Running time:** 19m 17s

------------------------------------------------------------------------

# Deploy Git Repositories and Register Workbench Project

-   DataStage & Compliance Repositories

    -   Create remote repository

    -   Extract supplied repository template locally

-   Configure Authentication to Remote Repository

    -   Register workbench.key.pub against Git repository

-   Populate Remote Repositories

    -   Associate local repository with remote repository

    -   Synchronize with git add, git commit, and git push

-   Repeat for Compliance Repository

    -   Create Remote, Create Local, Authenticate, Push

-   Test Workbench Access to Git Repositories

    -   MettleCI Compliance fetches from the Compliance repository

    -   MettleCI Commit pushes to the DataStage repository

**Running time:** 19m 28s

------------------------------------------------------------------------

# DataStage Designer Menus

-   Automatically using `.exe` **(**<a
    href="Integrating_MettleCI_Workbench_and_DataStage_Designer_on_Windows"
    data-linked-resource-id="454623235" data-linked-resource-version="15"
    data-linked-resource-type="page"><strong>link</strong></a>**)**

-   Manually using Designer’s Tools → `Customize` option **(**<a
    href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/745078910/No+permission+to+install+the+DataStage+Designer+MettleCI+menu+items"
    data-linked-resource-id="745078910" data-linked-resource-version="12"
    data-linked-resource-type="page"><strong>link</strong></a>**)**

**Running time:** 3m 31s

------------------------------------------------------------------------

# Define Work Item Management System

-   Authentication to Jira
    (<a href="#" rel="nofollow"><strong>link</strong></a>)

    -   Generation of `.pcks8` and `.pem` files for Workbench and Jira

    -   Creating a Jira Application Link to Workbench

-   Define a Jira Work Item Management System in Workbench

-   Associate our Jira Project with our DataStage Project in Workbench

-   Test Work Item lookup using the Workbench Commit page

COMING SOON!

------------------------------------------------------------------------

# Install Unit Test Harness

-   Install Parallel Test Harness

    -   WINDOWS Using `.exe` file (not demonstrated)

    -   UNIX Using `.rpm` file

-   Add `$DM_ENABLE_UNIT_TESTING` environment variable to DSParams

    -   For demo project + template DSParams for future projects

-   Test Parallel Test Harness

    -   Interception

    -   Test

COMING SOON!

------------------------------------------------------------------------

# Onboarding a DataStage Project into Git

-   Use `git pull` to align your local Git repository with the remote
    repository

-   Export your DataStage project to the local Git repository

-   Use `mettleci isx cut` to separate it into individual assets

-   `git add`, `git commit`, and `git push` to get all your assets into
    Git

COMING SOON!

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[aws_icon.png](attachments/2293497857/2293432325.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[aws-black-1.png](attachments/2293497857/2293497867.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[Installation Demo](attachments/2293497857/2293858312)
(application/gliffy+json)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[Installation Demo.png](attachments/2293497857/2293727235.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[Installation Demo](attachments/2293497857/2294087681)
(application/gliffy+json)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[Installation Demo.png](attachments/2293497857/2293465110.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[Installation Demo](attachments/2293497857/2296184835)
(application/gliffy+json)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[Installation Demo.png](attachments/2293497857/2295496733.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[Installation Demo](attachments/2293497857/2293366805)
(application/gliffy+json)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[Installation Demo.png](attachments/2293497857/2293858307.png)
(image/png)  

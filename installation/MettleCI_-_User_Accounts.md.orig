# MettleCI - User Accounts

# MettleCI Platform Components

The following high-level MettleCI architecture shows the key software
components to be installed, and their communications between hosts. 

Some points to note:

-   MettleCI works with all Information Server deployment topologies,
    including High Availability, Grid, and Cluster environments, For
    clarity, this diagram shows each tier residing on its own, dedicated
    host.

-   Application Lifecycle Management components can be co-hosted with
    the other tools on the MettleCI Host or located on another host
    (on-premise, cloud or SaaS).

------------------------------------------------------------------------

# User Accounts

MettleCI needs the dedicated accounts described in the sections below to
enable installation activities as well as support on-going operation.

**Note:** The names given below are simply proposals for reference
purposes and can be changed to meet your organisational requirements. If
you administer your accounts via a centralised repository (e.g. Active
Directory) then any accounts specified in the following list with the
same name can, of course, be the same account with privileges as
necessary to cover multiple roles across multiple environments and
components.

**Note:** The account used to install MettleCI is not required to be
shared with the Developers. Developers log in to MettleCI using their
existing DataStage user accounts.

## MettleCI Host

1.  Two Windows user accounts are required for the purpose of installing
    and administering MettleCI-related components on this host. They
    must...

    1.  ideally be named **mciconfig1** and **mciconfig2**

    2.  have administrator privileges sufficient to

        1.  run Windows tools "...as administrator"

        2.  install software for use by other users on the host; and

        3.  create, remove, start and stop Windows services.

    3.  **Note:** The second account acts to complement the first
        account in case the owner of the first account becomes
        unavailable, for whatever reason, or we collectively choose to
        perform work in parallel. 

2.  A Windows user account is required to act as a service account for
    executing MettleCI services. It ...

    1.  would ideally be named **mciservice**

    2.  must have only sufficient privileges to run the services
        installed by the **mciconfig*****\**** accounts

## DataStage Development Engine Tier

1.  An operating system user account <u>and corresponding DataStage
    application account</u> for in-bulk tasks (e.g. CI, CD) performed by
    MettleCI

    1.  Ideally named **mciagent**

    2.  Accessible via SSH from both the MettleCI Host and the MettleCI
        consultant's computer.

    3.  Capable of accessing your DataStage Engine Tier's filesystem
        such that DataStage can read files and directories generated or
        modified by this account.

        1.  In particular this account will make changes to the contents
            of your DataStage Projects directory.

    4.  Primary group must be **dstage** (or equivalent as configured
        for your DataStage platform)

    5.  On \*nix hosts, this account must be able to source the
        `$DSHOME/.dsenv` file.

    6.  The DataStage application account must be assigned the
        Information Server **Suite Administrator** and **DataStage
        Administrator** roles.

2.  An operating system user account <u>and corresponding DataStage
    application account</u> for use by MettleCI end-user functions (e.g.
    MettleCI Workbench)

    1.  Ideally named **mciworkb**

    2.  Accessible via SSH from both the MettleCI Host and the MettleCI
        consultant's computer.

    3.  Primary group must be **dstage** (or equivalent as configured
        for your DataStage platform)

    4.  `root` must be able to run commands under this user (via `sudo`)
        from within a SysVinit service.

    5.  On \*nix hosts, this account must be able to source the
        `$DSHOME/.dsenv` file.

    6.  The DataStage application account must be assigned the
        Information Server 'Suite Administrator'  and 'DataStage
        Administrator' roles.

## Password Expiry

All MettleCI-related service accounts (both application and operating
system) should have passwords that don't expire. A change to a service
account password will require updates to MettleCI configuration to
re-enable the MettleCI functions that rely on that service account.
Unplanned service account password changes are highly likely to cause
unnecessary delays.

------------------------------------------------------------------------

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[MettleCI topology (simplified)
Copy.png](attachments/1109491875/1109491878.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[MettleCI topology (simplified) Copy](attachments/1109491875/1109491881)
(application/gliffy+json)  

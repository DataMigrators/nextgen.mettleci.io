# MettleCI IBM OEM Release 1.0 Fix Pack 1

# Package Summary

|                               |                  |
|-------------------------------|------------------|
| **Package name**              | MettleCI 1.0 fp1 |
| **Release Date (yyyy-mm-dd)** | 2021-10-13       |

# Package Contents

<table class="confluenceTable" data-layout="default"
data-local-id="2acf7ff5-62d1-45b6-a6cb-4095b88fa3ae">
<tbody>
<tr class="odd">
<td class="confluenceTd"
data-highlight-colour="#f0f0f0"><p><strong>Function</strong></p></td>
<td class="confluenceTd"
data-highlight-colour="#f0f0f0"><p><strong>File</strong></p></td>
<td class="confluenceTd"
data-highlight-colour="#f0f0f0"><p><strong>Timestamp</strong></p></td>
<td class="confluenceTd"
data-highlight-colour="#f0f0f0"><p><strong>Size</strong></p></td>
<td class="confluenceTd"
data-highlight-colour="#f0f0f0"><p><strong>Type</strong></p></td>
<td class="confluenceTd"
data-highlight-colour="#f0f0f0"><p><strong>Notes</strong></p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>Command Shell</p></td>
<td
class="confluenceTd"><p><code>dm-mettleci-command-shell-1.1-179-dist.zip</code> WINDOWS</p>
<p><code>dm-mettleci-command-shell-1.1-179.noarch.rpm</code> UNIX</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>ZIP</p>
<p>RPM</p></td>
<td class="confluenceTd"><p>These Command Shell distributions each
include a full set of the latest versions of all MettleCI CLI plugins
(commands).</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>Workbench</p></td>
<td
class="confluenceTd"><p><code>dm-mettleci-workbench-1.0-1348-setup.exe</code> WINDOWS</p>
<p><code>dm-mettleci-workbench-1.0-1348.noarch.rpm</code> UNIX</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>EXE</p>
<p>RPM</p></td>
<td class="confluenceTd"></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>Compliance Rules</p></td>
<td
class="confluenceTd"><p><code>dm-compliance-rules-175m.zip</code></p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>ZIP</p></td>
<td class="confluenceTd"><p>A ready-to-use Git repository
folder</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>Sample Build Pipelines</p></td>
<td class="confluenceTd"><p><code>mettleci-azure-template.zip</code></p>
<p><code>mettleci-gitlab-template.zip</code></p>
<p><code>mettleci-jenkins-template.zip</code></p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>ZIP</p>
<p>ZIP</p>
<p>ZIP</p></td>
<td class="confluenceTd"></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>Parallel Unit Test Harness</p></td>
<td
class="confluenceTd"><p><code>dm-unittest-harness-1.0-343-setup.exe</code> WINDOWS</p>
<p><code>dm-unittest-harness-1.0-343.noarch.rpm</code> UNIX</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>EXE</p>
<p>RPM</p></td>
<td class="confluenceTd"></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>Server Unit Test Harness</p></td>
<td
class="confluenceTd"><p><code>dm-server-unit-test-harness-1.0-343.zip</code>
 WINDOWS  UNIX</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>ZIP</p></td>
<td class="confluenceTd"><p>This provides a Server interface to the
capabilities provided by the Parallel test harness which must also be
installed to provide unit test functionality.</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>CP4D Integration</p></td>
<td
class="confluenceTd"><p><code>workbench-icp4d-integration-1.0.zip</code></p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>TXT</p></td>
<td class="confluenceTd"><p>MettleCI CP4D integration scripts</p></td>
</tr>
</tbody>
</table>

Note that to use this distribution you will need to source a MettleCI
license file from the <a href="MettleCI_IBM_OEM_Release_1.0"
data-linked-resource-id="2245033985" data-linked-resource-version="10"
data-linked-resource-type="page">MettleCI Release v1.0 package</a>.

All MettleCI v1.0 Fix Pack 1 package contents only include assets which
are changed from those delivered in the initial v1.0 release and are
supplied in this structure:

``` java
.
├── Documentation
│ └── MCIDOC.zip                                                  # Archive of
├── README.pdf                                                    # This document
└── Software
    └── Distribution
        ├── CLI                                                   # MettleCI Command Line Interface
        │   ├── dm-mettleci-command-shell-1.1-179-dist.zip        # Windows
        │   └── dm-mettleci-command-shell-1.1-179.noarch.rpm      # Unix/Linux
        ├── Git Repos
        │   └── dm-compliance-rules-175m.zip                      # Sample MettleCI Compliance Rules
        ├── Unit Test Harness
        │   ├── dm-server-unit-test-harness-routine-1.0-343.zip   # Server UTH - All platforms
        │   ├── dm-unittest-harness-1.0-343-setup.exe             # Parallel UTH - Windows
        │   └── dm-unittest-harness-1.0-343.noarch.rpm            # Parallel UTH - Unix/Linux
        └── Workbench
            ├── dm-mettleci-workbench-1.0-1348-setup.exe          # Workbench for Windows DS Engines
            └── dm-mettleci-workbench-1.0-1348.noarch.rpm         # Workbench for Unix/Linux DS Engines
            └── CP4D
                └── workbench-icp4d-integration-1.0.zip           # MettleCI CP4D integration scripts
```

# Upgrade Process

Customers performing an initial installation, or upgrading from a
previous version of MettleCI licensed directly from Data Migrators can
follow the instructions here:

-   MettleCI installation/upgrade on standalone (traditional) DataStage
    environments is described here: Installation and Configuration

-   MettleCI installation/upgrade on Cloud Pak for Data environments is
    described here: MettleCI for IBM Cloud Pak for Data

# Improvements and New Features

## MettleCI Compliance

-   General minor wording and documentation improvements across most
    rules.

-   New and significantly updated rules:

|                                              |                  |          |                                                                                                                                 |
|----------------------------------------------|------------------|----------|---------------------------------------------------------------------------------------------------------------------------------|
| **Compliance Rule**                          | **Asset Type**   | **Type** | **Change Type**                                                                                                                 |
| DataStage Flow Designer Stages               | PARALLEL         | Update   | Updated stage list to align with recent IBM announcements.                                                                      |
| Database Row Limit                           | PARALLEL, SERVER | Update   | Compliance error message now includes the configured limit value.                                                               |
| Default Values in Job Params                 | PARALLEL, SERVER | New      | Ensures all job parameters have a default value.                                                                                |
| Entire Partitioning on Non- Reference Link   | PARALLEL         | New      | Ensures links with partitioning set to Entire are reference links for Lookup stages.                                            |
| Job Activity with Hardcoded Parameter Values | SEQUENCE         | Update   | Refactored for improved compatibility and error handling.                                                                       |
| Link Auto Partitioning set                   | PARALLEL         | New      | Reports links whose partitioning is set to ‘Auto’.                                                                              |
| Link Partitioning Must Match Sort            | PARALLEL         | New      | Ensures link partitioning keys match those of a link sort (so sort works as expected)                                           |
| Log Column Values                            | PARALLEL, SERVER | New      | Identify stages using ‘Log column values on first row error’ as they may expose sensitive information in the DataStage job log. |
| Sort Post Join Stage                         | PARALLEL, SERVER | New      | Identifies potentially redundant sorting (a sort stage or link sort) situated immediately after a Join stage.                   |
| Stage Naming                                 | PARALLEL         | Update   | Updated stage list to align with recent IBM announcements.                                                                      |

## Cloud Pak for Data

-   This release includes a number of scripts (along with supporting
    documentation) which support the integration of MettleCI into
    versions of IBM Cloud Pak for Data <a
    href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/1512439920"
    data-linked-resource-id="1512439920" data-linked-resource-version="11"
    data-linked-resource-type="page">prior to v4.0.2</a>.

## MettleCI Workbench

-   MettleCI Workbench now supports associating different Work Item
    Management systems with each DataStage project
    (<a href="https://datamigrators.atlassian.net/browse/MCI-3615"
    rel="nofollow">MCI-3615</a>) (documentation)

-   MettleCI Workbench now supports HTTPS connections to Git services
    (<a href="https://datamigrators.atlassian.net/browse/MCI-3851"
    rel="nofollow">MCI-3851</a>) (documentation)

-   MettleCI Workbench now performs the Git Commit and Push using
    user-specific Git credentials rather than a generic application-wide
    SSH key
    (<a href="https://datamigrators.atlassian.net/browse/MCI-3851"
    rel="nofollow">MCI-3851</a>) (documentation)

-   MettleCI Workbench works with Git systems which no longer use
    ‘Master’ as the term for their default branch
    (<a href="https://datamigrators.atlassian.net/browse/MCI-4056"
    rel="nofollow">MCI-4056</a>)

-   Improved SSL protocol negotiation to support recent changes to IBM's
    proprietary JVM extensions
    (<a href="https://datamigrators.atlassian.net/browse/MCI-4116"
    rel="nofollow">MCI-4116</a>)

-   Multiple minor UI and reliability fixes (detailed below)

# Fixes and Features

<table class="confluenceTable" data-layout="default"
data-local-id="f6e5106e-84d1-4cd4-8806-805bfd43ff12">
<tbody>
<tr class="header">
<th class="confluenceTh"><p><strong>Reference</strong></p></th>
<th class="confluenceTh"><p><strong>Component</strong></p></th>
<th class="confluenceTh"><p><strong>Type</strong></p></th>
<th class="confluenceTh"><p><strong>Description</strong></p></th>
</tr>
&#10;<tr class="odd">
<td class="confluenceTd"><p><a
href="https://datamigrators.atlassian.net/browse/MCI-3768"
rel="nofollow">MCI-3768</a></p></td>
<td class="confluenceTd"><p>Workbench Setup Wizard</p></td>
<td class="confluenceTd"><p>Technical Debt</p></td>
<td class="confluenceTd"><p>Workbench Setup Wizard redundant Issue
Management system selection removed</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p><a
href="https://datamigrators.atlassian.net/browse/MCI-3794"
rel="nofollow">MCI-3794</a></p></td>
<td class="confluenceTd"><p>Workbench</p></td>
<td class="confluenceTd"><p>Bug</p></td>
<td class="confluenceTd"><p>Workbench column validation seems to have
issues with ustrings and dates</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p><a
href="https://datamigrators.atlassian.net/browse/MCI-3797"
rel="nofollow">MCI-3797</a></p></td>
<td class="confluenceTd"><p>Improvement</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>Workbench initial empty file display
usability enhancements</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p><a
href="https://datamigrators.atlassian.net/browse/MCI-3809"
rel="nofollow">MCI-3809</a></p>
<p><a href="https://datamigrators.atlassian.net/browse/MCI-4033"
rel="nofollow">MCI-4033</a></p>
<p><a href="https://datamigrators.atlassian.net/browse/MCI-4035"
rel="nofollow">MCI-4035</a></p></td>
<td class="confluenceTd"><p>Workbench Data Fabrication</p></td>
<td class="confluenceTd"><p>Bug</p></td>
<td class="confluenceTd"><p>Workbench Data Fabrication for date cannot
update</p>
<p>Phone Number Data Fabrication not honouring the format</p>
<p>Date Fabrication throws exception when trying to modify date from
text box (instead of date picker)</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p><a
href="https://datamigrators.atlassian.net/browse/MCI-3800"
rel="nofollow">MCI-3800</a></p></td>
<td class="confluenceTd"><p>Workbench Installer</p></td>
<td class="confluenceTd"><p>Bug</p></td>
<td class="confluenceTd"><p>Corrected file permissions that are set in
Workbench RPM installer</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p><a
href="https://datamigrators.atlassian.net/browse/MCI-3799"
rel="nofollow">MCI-3799</a></p></td>
<td class="confluenceTd"><p>Workbench Installer</p></td>
<td class="confluenceTd"><p>Bug</p></td>
<td class="confluenceTd"><p>Fix Workbench RPM Installer on AIX</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p><a
href="https://datamigrators.atlassian.net/browse/MCI-3851"
rel="nofollow">MCI-3851</a></p>
<p><a href="https://datamigrators.atlassian.net/browse/MCI-3861"
rel="nofollow">MCI-3861</a></p>
<p><a href="https://datamigrators.atlassian.net/browse/MCI-3863"
rel="nofollow">MCI-3863</a></p>
<p><a href="https://datamigrators.atlassian.net/browse/MCI-3866"
rel="nofollow">MCI-3866</a></p>
<p><a href="https://datamigrators.atlassian.net/browse/MCI-3880"
rel="nofollow">MCI-3880</a></p>
<p><a href="https://datamigrators.atlassian.net/browse/MCI-3960"
rel="nofollow">MCI-3960</a></p>
<p><a href="https://datamigrators.atlassian.net/browse/MCI-3908"
rel="nofollow">MCI-3908</a></p>
<p><a href="https://datamigrators.atlassian.net/browse/MCI-3949"
rel="nofollow">MCI-3949</a></p>
<p><a href="https://datamigrators.atlassian.net/browse/MCI-3947"
rel="nofollow">MCI-3947</a></p>
<p><a href="https://datamigrators.atlassian.net/browse/MCI-3948"
rel="nofollow">MCI-3948</a></p>
<p><a href="https://datamigrators.atlassian.net/browse/MCI-3940"
rel="nofollow">MCI-3940</a></p>
<p><a href="https://datamigrators.atlassian.net/browse/MCI-3957"
rel="nofollow">MCI-3957</a></p></td>
<td class="confluenceTd"><p>Workbench Git Integration</p></td>
<td class="confluenceTd"><p>New feature</p></td>
<td class="confluenceTd"><p>Add support for user-specific git
credentials</p>
<p>Implement backend system to store users' git credentials</p>
<p>Implement config option to enable git via HTTPS</p>
<p>Update edit profile endpoint to accept git credentials</p>
<p>Add encryption key for git credentials to JWT</p>
<p>Git credentials use secrets directory</p>
<p>Implement front end for git credentials changes</p>
<p>User Friendly warnings when committing via https without credentials
setup</p>
<p>Generate git credential keystore password</p>
<p>Handle commit/compliance when git password can't be decrypted</p>
<p>Execute commit and compliance using user git credentials</p>
<p>Modify the add/update project endpoints to not accept HTTPS URLs if
git over HTTPS is disabled</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p><a
href="https://datamigrators.atlassian.net/browse/MCI-4027"
rel="nofollow">MCI-4027</a></p></td>
<td class="confluenceTd"><p>Workbench Git Integration</p></td>
<td class="confluenceTd"><p>Bug</p></td>
<td class="confluenceTd"><p>Workbench Git Credentials - ssh commit fails
when git username is null</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p><a
href="https://datamigrators.atlassian.net/browse/MCI-4055"
rel="nofollow">MCI-4055</a></p></td>
<td class="confluenceTd"><p>Workbench Setup Wizard</p></td>
<td class="confluenceTd"><p>Bug</p></td>
<td class="confluenceTd"><p>Rerunning Setup Wizard leaves
git-credentials in broken state</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p><a
href="https://datamigrators.atlassian.net/browse/MCI-4139"
rel="nofollow">MCI-4139</a></p></td>
<td class="confluenceTd"><p>Workbench Installer</p></td>
<td class="confluenceTd"><p>Bug</p></td>
<td class="confluenceTd"><p>Remove redundant message from MettleCI
Workbench Service banner message<br />
Workbench returns to home screen if no project has been
registered</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p><a
href="https://datamigrators.atlassian.net/browse/MCI-3897"
rel="nofollow">MCI-3897</a></p></td>
<td class="confluenceTd"><p>Workbench</p></td>
<td class="confluenceTd"><p>Bug</p></td>
<td class="confluenceTd"><p>Workbench returns to home screen if no
project has been registered</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p><a
href="https://datamigrators.atlassian.net/browse/MCI-3879"
rel="nofollow">MCI-3879</a></p></td>
<td class="confluenceTd"><p>Workbench Security</p></td>
<td class="confluenceTd"><p>Technical Debt</p></td>
<td class="confluenceTd"><p>Create log4j false-positive suppression XML
and regenerate test report</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p><a
href="https://datamigrators.atlassian.net/browse/MCI-4054"
rel="nofollow">MCI-4054</a></p></td>
<td class="confluenceTd"><p>Workbench Unit Testing</p></td>
<td class="confluenceTd"><p>Bug</p></td>
<td class="confluenceTd"><p>Unit Testing - “Incorrect column metadata”
errors not appearing in test result</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p><a
href="https://datamigrators.atlassian.net/browse/MCI-3891"
rel="nofollow">MCI-3891</a></p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>Bug</p></td>
<td class="confluenceTd"><p>Various Xmeta queries fail for engine with
non-default port</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p><a
href="https://datamigrators.atlassian.net/browse/MCI-3615"
rel="nofollow">MCI-3615</a></p>
<p><a href="https://datamigrators.atlassian.net/browse/MCI-3605"
rel="nofollow">MCI-3605</a></p>
<p><a href="https://datamigrators.atlassian.net/browse/MCI-3606"
rel="nofollow">MCI-3606</a></p>
<p><a href="https://datamigrators.atlassian.net/browse/MCI-3607"
rel="nofollow">MCI-3607</a></p>
<p><a href="https://datamigrators.atlassian.net/browse/MCI-3608"
rel="nofollow">MCI-3608</a></p></td>
<td class="confluenceTd"><p>Workbench Work Item Management
Integration</p></td>
<td class="confluenceTd"><p>New feature</p></td>
<td class="confluenceTd"><p>Add support for multiple concurrent Work
Item Management systems</p>
<p>Notify customers of breaking change which comes with Workbench and
the new Multi-WIM feature</p>
<p>Mystery customer test of Workbench upgrade with Multi- WIM
enabled</p>
<p>Align Workbench upgrade documentation for Multi-WIM feature</p>
<p>Workbench with Multi-WIM enabled by default</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p><a
href="https://datamigrators.atlassian.net/browse/MCI-4116"
rel="nofollow">MCI-4116</a></p></td>
<td class="confluenceTd"><p>Workbench</p></td>
<td class="confluenceTd"><p>Bug</p></td>
<td class="confluenceTd"><p>Fresh Workbench install produces cipher
suite error on most very recent version of DataStage</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p><a
href="https://datamigrators.atlassian.net/browse/MCI-4023"
rel="nofollow">MCI-4023</a></p></td>
<td class="confluenceTd"><p>Compliance</p></td>
<td class="confluenceTd"><p>Bug</p></td>
<td class="confluenceTd"><p>Handle a null`XMLProperties` object when
running Compliance against a DataStage job with a new, unmodified
Connector Stage.</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p><a
href="https://datamigrators.atlassian.net/browse/MCI-4201"
rel="nofollow">MCI-4201</a></p></td>
<td class="confluenceTd"><p>Workbench</p></td>
<td class="confluenceTd"><p>Bug</p></td>
<td class="confluenceTd"><p>Identified and removed race condition in
issue management page preventing project registration.</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p><a
href="https://datamigrators.atlassian.net/browse/MCI-4214"
rel="nofollow">MCI-4214</a></p></td>
<td class="confluenceTd"><p>Workbench Unit Testing</p></td>
<td class="confluenceTd"><p>Bug</p></td>
<td class="confluenceTd"><p>Setting 24Hr time in Windows produces wrong
date values in JUnit Test results.</p></td>
</tr>
</tbody>
</table>

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[dm-server-unit-test-harness-routine-1.0-350.zip](attachments/2245034041/2245034055.zip)
(application/zip)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[dm-unittest-harness-1.0-350.noarch.rpm](attachments/2245034041/2245034058.rpm)
(application/x-rpm)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[dm-unittest-harness-1.0-350-setup.exe](attachments/2245034041/2245034061.exe)
(application/x-msdownload)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[command-shell-1.1-133-dist.zip](attachments/2245034041/2245034064.zip)
(application/zip)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[dm-s2px-conversion-plugin-1.0-436.jar](attachments/2245034041/2245034067.jar)
(application/java-archive)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[dm-s2px-analysis-plugin-1.0-46.jar](attachments/2245034041/2245034070.jar)
(application/java-archive)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[dm-mettleci-workbench-1.0-1425-setup.exe](attachments/2245034041/2245034073.exe)
(application/x-msdownload)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[dm-mettleci-workbench-1.0-1425.noarch.rpm](attachments/2245034041/2245034076.rpm)
(application/x-rpm)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10711?size=medium](attachments/2245034041/2357723350) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10715?size=medium](attachments/2245034041/2357723240) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10703?size=medium](attachments/2245034041/2357723273) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10710?size=medium](attachments/2245034041/2357723251) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10715?size=medium](attachments/2245034041/2357723295) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10710?size=medium](attachments/2245034041/2357723262) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10710?size=medium](attachments/2245034041/2357723383) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10703?size=medium](attachments/2245034041/2357723284) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10703?size=medium](attachments/2245034041/2357723328) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10715?size=medium](attachments/2245034041/2357723306) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10715?size=medium](attachments/2245034041/2357723317) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10715?size=medium](attachments/2245034041/2357723339) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10703?size=medium](attachments/2245034041/2357723372) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10715?size=medium](attachments/2245034041/2357723361) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10711?size=medium](attachments/2245034041/2357723216) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10715?size=medium](attachments/2245034041/2357723416) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10703?size=medium](attachments/2245034041/2357723394) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10710?size=medium](attachments/2245034041/2357723405) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10703?size=medium](attachments/2245034041/2357723488) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10710?size=medium](attachments/2245034041/2357723449) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10715?size=medium](attachments/2245034041/2357723427) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10715?size=medium](attachments/2245034041/2357723438) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10715?size=medium](attachments/2245034041/2357723521) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10710?size=medium](attachments/2245034041/2357723460) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10710?size=medium](attachments/2245034041/2357723477) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10718?size=medium](attachments/2245034041/2357723471) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10710?size=medium](attachments/2245034041/2357723499) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10703?size=medium](attachments/2245034041/2357723543) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10710?size=medium](attachments/2245034041/2357723510) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10710?size=medium](attachments/2245034041/2357723234) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10715?size=medium](attachments/2245034041/2357723532) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10715?size=medium](attachments/2245034041/2357723576) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10703?size=medium](attachments/2245034041/2357723554) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10703?size=medium](attachments/2245034041/2357723565) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10703?size=medium](attachments/2245034041/2357723228) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10715?size=medium](attachments/2245034041/2357723222) (image/svg+xml)  

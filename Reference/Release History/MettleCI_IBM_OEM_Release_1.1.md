# MettleCI IBM OEM Release 1.1

-   [Package Summary](#MettleCIIBMOEMRelease1.1-PackageSummary)
-   [Package Contents](#MettleCIIBMOEMRelease1.1-PackageContents)
-   [Change Log](#MettleCIIBMOEMRelease1.1-ChangeLog)
    -   [New Features](#MettleCIIBMOEMRelease1.1-NewFeatures)
        -   [New MettleCI Compliance
            Rules](#MettleCIIBMOEMRelease1.1-NewMettleCIComplianceRules)
    -   [Fixes](#MettleCIIBMOEMRelease1.1-Fixes)
        -   [MettleCI
            Foundations](#MettleCIIBMOEMRelease1.1-MettleCIFoundations)
        -   [MettleCI
            Workbench](#MettleCIIBMOEMRelease1.1-MettleCIWorkbench)
        -   [MettleCI Unit Test
            Harnesses](#MettleCIIBMOEMRelease1.1-MettleCIUnitTestHarnesses)
        -   [MettleCI Command Line
            Interface](#MettleCIIBMOEMRelease1.1-MettleCICommandLineInterface)
-   [Upgrade Process](#MettleCIIBMOEMRelease1.1-UpgradeProcess)
-   [Known Issues](#MettleCIIBMOEMRelease1.1-KnownIssues)
-   [Notes](#MettleCIIBMOEMRelease1.1-Notes)

# Package Summary

|                               |              |
|-------------------------------|--------------|
| **Package name**              | MettleCI 1.1 |
| **Release Date (yyyy-mm-dd)** | 2022-12-22   |

# Package Contents

This release also bundles **S2PX v.1.1**.

See <a
href="https://datamigrators.atlassian.net/wiki/spaces/S2PX/pages/2211414017/Server-to-Parallel+-+S2PX+Release+v1.1"
data-linked-resource-id="2211414017" data-linked-resource-version="27"
data-linked-resource-type="page">this page</a> for detailed release
notes for S2PX.

This MettleCI v1.1 package contains a complete set of MettleCI and S2PX
assets which give you everything you need to get up and running with
these tools. You do **not** need to install any previous MettleCI or
S2PX releases to use this package.

``` java
.
└── Software
    ├── CLI
    │   ├── dm-mettleci-command-shell-1.1-238-dist.zip
    │   └── dm-mettleci-command-shell-1.1-238.noarch.rpm
    ├── License
    │   ├── mettleci.lic
    │   └── properties.txt
    ├── Repositories
    │   ├── dm-compliance-rules-233.zip
    │   └── mettleci-repo-examples-27.zip
    ├── S2PX
    │   ├── dm-s2px-analysis-plugin-1.0-82.jar
    │   └── dm-s2px-conversion-plugin-1.0-570.jar
    ├── Unit Test Harnesses
    │   ├── dm-server-unit-test-harness-routine-1.1-391.zip
    │   ├── dm-unittest-harness-1.1-391-setup.exe
    │   └── dm-unittest-harness-1.1-391.noarch.rpm
    └── Workbench
        ├── dm-mettleci-workbench-1.0-1520-setup.exe
        └── dm-mettleci-workbench-1.0-1520.noarch.rpm
```

<table class="confluenceTable" data-layout="default"
data-local-id="2acf7ff5-62d1-45b6-a6cb-4095b88fa3ae">
<tbody>
<tr class="header">
<th class="confluenceTh"
data-highlight-colour="#f0f0f0"><p><strong>Function</strong></p></th>
<th class="confluenceTh"
data-highlight-colour="#f0f0f0"><p><strong>File</strong></p></th>
<th class="confluenceTh"
data-highlight-colour="#f0f0f0"><p><strong>Notes</strong></p></th>
</tr>
&#10;<tr class="odd">
<td class="confluenceTd"><p>Command Shell</p></td>
<td
class="confluenceTd"><p><code>dm-mettleci-command-shell-1.1-238-dist.zip</code> WINDOWS</p>
<p><code>dm-mettleci-command-shell-1.1-238.noarch.rpm</code> UNIX</p></td>
<td class="confluenceTd"><p>These operating system-specific <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/2216886273/MettleCI+Command+Line+Interface"
data-linked-resource-id="2216886273" data-linked-resource-version="1"
data-linked-resource-type="page">MettleCI Command Shell</a>
distributions each include a full set of the latest versions of all <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/2125725711/CLI+Plugins"
data-linked-resource-id="2125725711" data-linked-resource-version="7"
data-linked-resource-type="page">MettleCI CLI plugins</a>.</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>Compliance Rules</p></td>
<td class="confluenceTd"><p><code>dm-compliance-rules-233.zip</code> ALL
PLATFORMS</p></td>
<td class="confluenceTd"><p>A ready-to-deploy Git repository containing
all the MettleCI sample <a href="Compliance_Rules_Reference"
data-linked-resource-id="2213085185" data-linked-resource-version="11"
data-linked-resource-type="page">Compliance Rules</a>.</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>Template Git Repositories</p></td>
<td class="confluenceTd"><p><code>mettleci-repo-examples-27.zip</code>
ALL PLATFORMS</p></td>
<td class="confluenceTd"><p>Contains two example Git repositories:</p>
<ul>
<li><p><code>jenkins-mci-shared-libraries.zip</code> (ALL PLATFORMS)
containing example <a href="#" rel="nofollow">Jenkins Reusable Pipeline
Components</a>.</p></li>
<li><p><code>mettleci-repo-template.zip</code> (ALL PLATFORMS)
containing example CI/CD pipeline definitions for <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/741376173/GitHub"
data-linked-resource-id="741376173" data-linked-resource-version="9"
data-linked-resource-type="page">GitHub</a>, <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/741244932/GitLab"
data-linked-resource-id="741244932" data-linked-resource-version="20"
data-linked-resource-type="page">GitLab</a>, <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/731709604/Jenkins"
data-linked-resource-id="731709604" data-linked-resource-version="11"
data-linked-resource-type="page">Jenkins</a>, and <a href="#"
rel="nofollow">Microsoft Azure DevOps</a>.</p></li>
</ul>
<div class="panel"
style="background-color: #EAE6FF;border-color: #998DD9;border-width: 1px;">
<div class="panelContent" style="background-color: #EAE6FF;">
<p><strong>Unsupported Examples</strong></p>
<p>Note that despite being fully functional, these assets are supplied
without warranty or support and are provided to serve as examples of how
you can utilise the MettleCI Command Line Interface to construct your
own build and deployment pipelines to meet your unique requirements.</p>
</div>
</div></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>License</p></td>
<td class="confluenceTd"><p><code>mettleci.lic</code> ALL PLATFORMS</p>
<p><code>properties.txt</code> ALL PLATFORMS</p></td>
<td class="confluenceTd"><p>The MettleCI license file (valid to the end
of 2099) required to enable MettleCI functionality, along with a
human-readable properties file describing the license constraints.</p>
<div class="panel"
style="background-color: #EAE6FF;border-color: #998DD9;border-width: 1px;">
<div class="panelContent" style="background-color: #EAE6FF;">
<p><strong>Licence Update</strong></p>
<p>If you download this MettleCI Release package v1.1 from IBM Passport
Advantage (or a similar IBM site <strong>excluding Fix Central</strong>)
then it includes a full IBM OEM MettleCI license file. From this release
forward this license file will be named <code>mettleci.lic</code> which
is the filename expected by MettleCI Workbench. Other than the name
change the contents of the file are unaltered, so existing users of
MettleCI do not need to replace their existing license file.</p>
</div>
</div></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>Server Unit Test Harness</p></td>
<td
class="confluenceTd"><p><code>dm-server-unit-test-harness-routine-1.1-391.zip</code>
 ALL PLATFORMS</p></td>
<td class="confluenceTd"><p>The MettleCI Server Job Unit Test Harness
for installation on your DataStage Engine.</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>Parallel Unit Test Harness</p></td>
<td
class="confluenceTd"><p><code>dm-unittest-harness-1.1-391-setup.exe</code> WINDOWS</p>
<p><code>dm-unittest-harness-1.1-391.noarch.rpm</code> UNIX</p></td>
<td class="confluenceTd"><p>The MettleCI Parallel Job Unit Test Harness
for installation on your Unix (<code>.rpm</code>) or Windows
(<code>.exe</code>) DataStage Engine.</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>Workbench</p></td>
<td
class="confluenceTd"><p><code>dm-mettleci-workbench-1.0-1520-setup.exe</code> WINDOWS</p>
<p><code>dm-mettleci-workbench-1.0-1520.noarch.rpm</code> UNIX</p></td>
<td class="confluenceTd"><p>The <a href="#" rel="nofollow">MettleC
Workbench Service</a>.</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>S2PX</p></td>
<td
class="confluenceTd"><p><code>dm-s2px-analysis-plugin-1.0-82.jar</code>
ALL PLATFORMS</p>
<p><code>dm-s2px-conversion-plugin-1.0-570.jar</code> ALL
PLATFORMS</p></td>
<td class="confluenceTd"><p>Two <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/2125725711/CLI+Plugins"
data-linked-resource-id="2125725711" data-linked-resource-version="7"
data-linked-resource-type="page">MettleCI CLI Plugins</a> which perform
<a
href="https://datamigrators.atlassian.net/wiki/spaces/S2PX/pages/2080440325/Running+S2PX+Analysis"
data-linked-resource-id="2080440325" data-linked-resource-version="3"
data-linked-resource-type="page">pre-conversion analysis</a> of a DSX
containing Server Jobs and the <a
href="https://datamigrators.atlassian.net/wiki/spaces/S2PX/pages/2080440348/Running+S2PX+Conversion"
data-linked-resource-id="2080440348" data-linked-resource-version="3"
data-linked-resource-type="page">Server-to-Parallel conversion</a> of an
ISX containing Server Jobs. See <a href="http://s2px.mettleci.io/"
rel="nofollow">http://s2px.mettleci.io</a> for more details.</p></td>
</tr>
</tbody>
</table>

# Change Log

## New Features

-   A significantly enhanced implementation of Unit Test Interception
    for Parallel Jobs using Sparse Lookups (<a
    href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4992"
    rel="nofollow">MCI-4992</a>).

    -   See documentation of the <a
        href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/534413695/Unit+Testing+Sparse+Lookup+Stages?src=search#Sparse-Lookup-Stage-(&#39;Replace&#39;-method)"
        rel="nofollow">Sparse Lookup ‘Replace’ method</a>.

-   Initial release of Azure pipeline examples.

-   Initial release of GitHub pipeline examples.

-   Initial release of GitLab pipeline examples.

-   Substantial overhaul of Jenkins Pipeline examples

    -   Introduction of reusable Groovy components (CCMT, Compile,
        Deploy, Unit Test) for use across multiple Jenkins pipelines

    -   Upgraded unified DevOps and Upgrade pipelines

    -   Two new multi-purpose pipelines: Build and Deploy

-   More new Compliance rules (details below)

### New MettleCI Compliance Rules

This release introduces nine new Compliance rules: (click the title of
each for more details)

|                                                               |                                                                                    |
|---------------------------------------------------------------|------------------------------------------------------------------------------------|
| **Issue Reference**                                           | **Summary**                                                                        |
| <a href="https://datamigrators.atlassian.net/browse/MCI-973"  
 rel="nofollow">MCI-973</a>                                     | <a                                                                                 
                                                                 href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/2356281345"      
                                                                 rel="nofollow">Oracle Connector Not Using Partition Read</a>                        |
| <a href="https://datamigrators.atlassian.net/browse/MCI-1541" 
 rel="nofollow">MCI-1541</a>                                    | <a                                                                                 
                                                                 href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/2352480257"      
                                                                 rel="nofollow">Job Using Transformer Surrogate Key</a>                              |
| <a href="https://datamigrators.atlassian.net/browse/MCI-2921" 
 rel="nofollow">MCI-2921</a>                                    | <a href="Sequential_File_Read_Using_Same_Partitioning"                             
                                                                 data-linked-resource-id="2352742401" data-linked-resource-version="3"               
                                                                 data-linked-resource-type="page">Sequential File Read Using Same                    
                                                                 Partitioning</a>                                                                    |
| <a href="https://datamigrators.atlassian.net/browse/MCI-2948" 
 rel="nofollow">MCI-2948</a>                                    | <a href="Transformer_Uses_Abort_after_rows_"                                       
                                                                 data-linked-resource-id="2351300609" data-linked-resource-version="4"               
                                                                 data-linked-resource-type="page">Transformer Uses Abort After Rows</a>              |
| <a href="https://datamigrators.atlassian.net/browse/MCI-3000" 
 rel="nofollow">MCI-3000</a>                                    | <a href="Data_Sets_not_using_Same_partitioning_method"                             
                                                                 data-linked-resource-id="2351300693" data-linked-resource-version="1"               
                                                                 data-linked-resource-type="page">DataSet Not Using Same Partition</a>               |
| <a href="https://datamigrators.atlassian.net/browse/MCI-3565" 
 rel="nofollow">MCI-3565</a>                                    | <a href="Join_Partition_vs_Join_Key"                                               
                                                                 data-linked-resource-id="2218721401" data-linked-resource-version="6"               
                                                                 data-linked-resource-type="page">Join Partition vs Join Key</a>                     |
| <a href="https://datamigrators.atlassian.net/browse/MCI-4517" 
 rel="nofollow">MCI-4517</a>                                    | <a href="Date_Format_in_Annotation" data-linked-resource-id="2365882369"           
                                                                 data-linked-resource-version="7" data-linked-resource-type="page">Date              
                                                                 Format in Annotation</a> (template for seeking arbitrary text in a Job Annotation)  |
| <a href="https://datamigrators.atlassian.net/browse/MCI-4381" 
 rel="nofollow">MCI-4381</a>                                    | <a href="#" rel="nofollow">Column Name Contains Unsupported                        
                                                                 Characters</a>.                                                                     |
| <a href="https://datamigrators.atlassian.net/browse/MCI-4974" 
 rel="nofollow">MCI-4974</a>                                    | <a href="Transformer_Uses_Rnd_Function"                                            
                                                                 data-linked-resource-id="2351300651" data-linked-resource-version="6"               
                                                                 data-linked-resource-type="page">Job Using Rnd() Function</a>                       |

## Fixes

### MettleCI Foundations

These are cross-module fixes, often related to security enhancements or
updates to <a href="MettleCI_Open_Source_Reference"
data-linked-resource-id="456818726" data-linked-resource-version="28"
data-linked-resource-type="page">third party libraries</a>.

|                                                                                                |                                                                                    |
|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| **Issue Reference**                                                                            | **Summary**                                                                        |
| <a href="https://datamigrators.atlassian.net/browse/MCI-3832"                                  
 rel="nofollow">MCI-3832</a>                                                                     | XML specification allows the use of entities that can be external (Security issue) |
| <a href="https://datamigrators.atlassian.net/browse/MCI-3831"                                  
 rel="nofollow">MCI-3831</a>                                                                     | X-Frame-Options header is not included in the HTTP response (CWE-16)               |
| <a                                                                                             
 href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-5054"  
 rel="nofollow">MCI-5054</a>                                                                     | OWASP security vulnerabilities                                                     |

### MettleCI Workbench

Starting from this release the MettleCI Workbench Setup Wizard no longer
generates SHA-1 RSA keys (now <a
href="https://github.blog/2021-09-01-improving-git-protocol-security-github/"
rel="nofollow">deprecated by GitHub</a>) but instead generates
GitHub-supported ECDSA keys by default. See <a
href="http://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4875"
rel="nofollow">MCI-4875</a> below.

A number of minor cosmetic issues were addressed, plus the following
notable fixes and improvements:

|                                                                                                |                                                                                                                                       |
|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| **Issue Reference**                                                                            | **Summary**                                                                                                                           |
| <a                                                                                             
 href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-1294"  
 rel="nofollow">MCI-1294</a>                                                                     | Standardise 'Loading' messages between the Workbench pages                                                                            |
| <a                                                                                             
 href="http://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-1297"   
 rel="nofollow">MCI-1297</a>                                                                     | Workbench toaster messages should be user-dismissible.                                                                                |
| <a                                                                                             
 href="http://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-2606"   
 rel="nofollow">MCI-2606</a>                                                                     | Update command line text when workbench `rpm` is installed.                                                                           |
| <a                                                                                             
 href="http://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-3008"   
 rel="nofollow">MCI-3008</a>                                                                     | Requesting Unit Test Results for a job without a Unit Test should prompt a user to create one.                                        |
| <a                                                                                             
 href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-3708"  
 rel="nofollow">MCI-3708</a>                                                                     | Workbench to log the constraints/properties of the MettleCI license in use.                                                           |
| <a                                                                                             
 href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-3718"  
 rel="nofollow">MCI-3718</a>                                                                     | Workbench Install - update docs to warn about file perms/owns.                                                                        |
| <a                                                                                             
 href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-3798"  
 rel="nofollow">MCI-3798</a>                                                                     | Uploading new file when file is empty should not produce a warning.                                                                   |
| <a                                                                                             
 href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-3836"  
 rel="nofollow">MCI-3836</a>                                                                     | Prevent the registration of a DS project that doesn't exist.                                                                          |
| <a                                                                                             
 href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-3837"  
 rel="nofollow">MCI-3837</a>                                                                     | Invalid CSV files should not be saved.                                                                                                |
| <a                                                                                             
 href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-3838"  
 rel="nofollow">MCI-3838</a>                                                                     | Review token expiry time.                                                                                                             |
| <a                                                                                             
 href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-3842"  
 rel="nofollow">MCI-3842</a>                                                                     | Sensitive files should be read/write only by `mciworkb`.                                                                              |
| <a                                                                                             
 href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4203"  
 rel="nofollow">MCI-4203</a>                                                                     | Installing Workbench Designer menus asks to confirm ‘v11.5’ installation on any platform.                                             |
| <a                                                                                             
 href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4251"  
 rel="nofollow">MCI-4251</a>                                                                     | Prevent column data from overlapping in the Unit Test Results screen.                                                                 |
| <a                                                                                             
 href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4252"  
 rel="nofollow">MCI-4252</a>                                                                     | Provide a read-only view of Workbench project settings to non-admin users.                                                            |
| <a                                                                                             
 href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4301"  
 rel="nofollow">MCI-4301</a>                                                                     | Update Workbench to default token session expiry to 1 hour.                                                                           |
| <a                                                                                             
 href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4405"  
 rel="nofollow">MCI-4405</a>                                                                     | Workbench needs to provide to user enough info to configure Issue Management callback URL.                                            |
| <a                                                                                             
 href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4425"  
 rel="nofollow">MCI-4425</a>                                                                     | Fresh MettleCI install can (unintentionally) present all pages with no registered project.                                            |
| <a                                                                                             
 href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4426"  
 rel="nofollow">MCI-4426</a>                                                                     | Add ‘processing’ indication to Register Project page while validating supplied Git URL.                                               |
| <a                                                                                             
 href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4446"  
 rel="nofollow">MCI-4446</a>                                                                     | Workbench Project Registration error validating GitLab SSH URI.                                                                       |
| <a                                                                                             
 href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4505"  
 rel="nofollow">MCI-4505</a>                                                                     | Server Unit Tests should stub all passive stages.                                                                                     |
| <a                                                                                             
 href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4513"  
 rel="nofollow">MCI-4513</a>                                                                     | Can't successfully register an Azure DevOps project in MCI Workbench.                                                                 |
| <a                                                                                             
 href="http://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4514"   
 rel="nofollow">MCI-4514</a>                                                                     | Generated `workbench.key.pub` should have comment `mettleci@{hostname}` to distinguish keys in complex environments.                  |
| <a                                                                                             
 href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4548"  
 rel="nofollow">MCI-4548</a>                                                                     | Improve Case Search in Workbench.                                                                                                     |
| <a                                                                                             
 href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4575"  
 rel="nofollow">MCI-4575</a>                                                                     | Document Workbench HTTPS configuration using an existing certificate rather than a new, self signed, certificate.                     |
| <a                                                                                             
 href="http://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4675"   
 rel="nofollow">MCI-4675</a>                                                                     | Catch and display error when workbench fails to source a project list from DataStage.                                                 |
| <a                                                                                             
 href="http://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4734"   
 rel="nofollow">MCI-4734</a>                                                                     | Workbench on Windows has an issue with `config.yml` setting `httpsCredentialsStore`.                                                  |
| <a                                                                                             
 href="http://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4772"   
 rel="nofollow">MCI-4772</a>                                                                     | Workbench startup problems on RHEL8 systems.                                                                                          |
| <a                                                                                             
 href="http://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4794"   
 rel="nofollow">MCI-4794</a>                                                                     | Enhance Workbench Setup Wizard to display or log error when failing during completion step.                                           |
| <a                                                                                             
 href="http://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4841"   
 rel="nofollow">MCI-4841</a>                                                                     | Enhance Workbench Windows Installer to allow silent mode.                                                                             |
| <a                                                                                             
 href="http://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4874"   
 rel="nofollow">MCI-4874</a>                                                                     | Remove reference to ‘Work Item Management Platform’ on Workbench Setup Wizard.                                                        |
| <a                                                                                             
 href="http://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4875"   
 rel="nofollow">MCI-4875</a>                                                                     | SSH key generation performed by setup wizard must align with new GitHub requirements (ECDSA not RSA).                                 |
| <a                                                                                             
 href="http://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4884"   
 rel="nofollow">MCI-4884</a>                                                                     | Workbench (Windows) is not able to find `git-credentials-keystore-password` file from Setup Wizard generated `config.yml`.            |
| <a                                                                                             
 href="http://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4886"   
 rel="nofollow">MCI-4886</a>                                                                     | Don’t display a ‘ReadOnly’ message when creating a new test data file after opening a ‘ReadOnly’ file from a Unit Test Specification. |
| <a                                                                                             
 href="http://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4887"   
 rel="nofollow">MCI-4887</a>                                                                     | Inconsistent use of license/licence in Workbench Setup Wizard summary screen.                                                         |
| <a                                                                                             
 href="http://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4889"   
 rel="nofollow">MCI-4889</a>                                                                     | Workbench Setup Wizard’s 'ECDSA Key' page displays an RSA template.                                                                   |
| <a                                                                                             
 href="http://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4923"   
 rel="nofollow">MCI-4923</a>                                                                     | Fix `chkconfig` settings in Workbench `rpm` Service.                                                                                  |

### MettleCI Unit Test Harnesses

<table class="confluenceTable" data-layout="default"
data-local-id="9908a3e0-f840-4d01-8528-80520b638e11">
<tbody>
<tr class="header">
<th class="confluenceTh"><p><strong>Issue Reference</strong></p></th>
<th class="confluenceTh"><p><strong>Summary</strong></p></th>
</tr>
&#10;<tr class="odd">
<td class="confluenceTd"><p><a
href="http://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-3904"
rel="nofollow">MCI-3904</a></p></td>
<td class="confluenceTd"><p>Update to support new <a
href="http://s2px.mettleci.io/" rel="nofollow">S2PX</a> Asset Query
which detects instances of custom DS Basic Routines in
Transformers.</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p><a
href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4470"
rel="nofollow">MCI-4470</a></p></td>
<td class="confluenceTd"><p>Unit Test Harness occasionally aborts with
‘ds_anyopen() - Slot1 1 already in use’ error</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p><a
href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4524"
rel="nofollow">MCI-4524</a></p></td>
<td class="confluenceTd"><p>Parallel Unit Test Spec, for Jobs with
certain conditions, incorrectly fails validation</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p><a
href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4545"
rel="nofollow">MCI-4545</a></p></td>
<td class="confluenceTd"><p>Server Unit Test Interception crashes when
intercepting input connected to Collector stages</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p><a
href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4842"
rel="nofollow">MCI-4842</a></p></td>
<td class="confluenceTd"><p>Enhance Unit Test Harness Windows Installer
to allow silent mode</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p><a
href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4903"
rel="nofollow">MCI-4903</a>,</p>
<p><a
href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4904"
rel="nofollow">MCI-4904</a>,</p>
<p><a
href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4977"
rel="nofollow">MCI-4977</a></p></td>
<td class="confluenceTd"><p>Remodel some Unit Test underpinnings in
preparation for forthcoming CP4D integration</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p><a
href="https://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4992"
rel="nofollow">MCI-4992</a></p></td>
<td class="confluenceTd"><p>Implement Sparse Lookup interception for
Parallel Unit Testing</p></td>
</tr>
</tbody>
</table>

### MettleCI Command Line Interface

|                                                                                               |                                                                                                                      |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| **Issue Reference**                                                                           | **Summary**                                                                                                          |
| <a                                                                                            
 href="http://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4686"  
 rel="nofollow">MCI-4686</a>                                                                    | Handle leading space in front of namespace when invoking from MettleCI CLI interactive session.                      |
| <a                                                                                            
 href="http://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4805"  
 rel="nofollow">MCI-4805</a>                                                                    | MettleCI command should permit user-specified Java options.                                                          |
| <a                                                                                            
 href="http://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4900"  
 rel="nofollow">MCI-4900</a>                                                                    | MettleCLI (Windows) not able to handle password with `!` (since introduction of supporting `-Xms` & `-Xmx` options). |
| <a                                                                                            
 href="http://build.datamigrators.io/bamboo/project/jiraRedirect.action?jiraIssueKey=MCI-4922"  
 rel="nofollow">MCI-4922</a>                                                                    | MCI CLI `config.properties` file should have default uncommented `license.file` entry should be the Windows version. |
| <a href="https://datamigrators.atlassian.net/browse/MCI-4928"                                 
 rel="nofollow">MCI-4928</a>                                                                    | MettleCI CLI on Windows dropping arguments which include wildcard characters.                                        |

# Upgrade Process

Customers performing an initial installation, or upgrading from a
previous version of MettleCI, can follow the instructions included (or
linked) from these pages:

-   <a
    href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/415367258/Installation+and+Configuration"
    data-linked-resource-id="415367258" data-linked-resource-version="11"
    data-linked-resource-type="page">Installation and Configuration</a>

    -   <a
        href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/453902355/Installing+MettleCI+Workbench"
        data-linked-resource-id="453902355" data-linked-resource-version="13"
        data-linked-resource-type="page">Installing MettleCI Workbench</a>

    -   <a
        href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/454393879/Installing+MettleCI+Unit+Test+Harness"
        data-linked-resource-id="454393879" data-linked-resource-version="12"
        data-linked-resource-type="page">Installing MettleCI Unit Test
        Harness</a>

    -   <a
        href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/488898631/Installing+MettleCI+Command+Line+Interface"
        data-linked-resource-id="488898631" data-linked-resource-version="9"
        data-linked-resource-type="page">Installing MettleCI Command Line
        Interface</a>

# Known Issues

|                                                               |                                                                                                                                                                                                                                                                                       |
|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Issue Reference**                                           | **Summary**                                                                                                                                                                                                                                                                           |
| <a href="https://datamigrators.atlassian.net/browse/MCI-5055" 
 rel="nofollow">MCI-5055</a>                                    | The integration with Microsoft Azure currently assumes that your Azure DevOps project uses an Azure DevOps-hosted Git repository. MettleCI does not currently support Azure DevOps projects using externally-linked GitHub repositories. This is a priority fix for the next release. |

# Notes

For documentation please visit <a href="http://docs.mettleci.io"
rel="nofollow"><u>http://docs.mettleci.io</u></a>

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[dm-server-unit-test-harness-routine-1.0-350.zip](attachments/2311225345/2311225360.zip)
(application/zip)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[dm-unittest-harness-1.0-350.noarch.rpm](attachments/2311225345/2311225363.rpm)
(application/x-rpm)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[dm-unittest-harness-1.0-350-setup.exe](attachments/2311225345/2311225366.exe)
(application/x-msdownload)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[command-shell-1.1-133-dist.zip](attachments/2311225345/2311225369.zip)
(application/zip)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[dm-s2px-conversion-plugin-1.0-436.jar](attachments/2311225345/2311225372.jar)
(application/java-archive)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[dm-s2px-analysis-plugin-1.0-46.jar](attachments/2311225345/2311225375.jar)
(application/java-archive)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[dm-mettleci-workbench-1.0-1425-setup.exe](attachments/2311225345/2311225378.exe)
(application/x-msdownload)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[dm-mettleci-workbench-1.0-1425.noarch.rpm](attachments/2311225345/2311225381.rpm)
(application/x-rpm)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10711?size=medium](attachments/2311225345/2358280376) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10715?size=medium](attachments/2311225345/2358280266) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10703?size=medium](attachments/2311225345/2358280299) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10710?size=medium](attachments/2311225345/2358280277) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10715?size=medium](attachments/2311225345/2358280321) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10710?size=medium](attachments/2311225345/2358280288) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10710?size=medium](attachments/2311225345/2358280409) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10703?size=medium](attachments/2311225345/2358280310) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10703?size=medium](attachments/2311225345/2358280354) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10715?size=medium](attachments/2311225345/2358280332) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10715?size=medium](attachments/2311225345/2358280343) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10715?size=medium](attachments/2311225345/2358280365) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10703?size=medium](attachments/2311225345/2358280398) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10715?size=medium](attachments/2311225345/2358280387) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10711?size=medium](attachments/2311225345/2358280242) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10715?size=medium](attachments/2311225345/2358280442) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10703?size=medium](attachments/2311225345/2358280420) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10710?size=medium](attachments/2311225345/2358280431) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10703?size=medium](attachments/2311225345/2358280514) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10710?size=medium](attachments/2311225345/2358280475) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10715?size=medium](attachments/2311225345/2358280453) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10715?size=medium](attachments/2311225345/2358280464) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10715?size=medium](attachments/2311225345/2358280547) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10710?size=medium](attachments/2311225345/2358280486) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10710?size=medium](attachments/2311225345/2358280503) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10718?size=medium](attachments/2311225345/2358280497) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10710?size=medium](attachments/2311225345/2358280525) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10703?size=medium](attachments/2311225345/2358280569) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10710?size=medium](attachments/2311225345/2358280536) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10710?size=medium](attachments/2311225345/2358280260) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10715?size=medium](attachments/2311225345/2358280558) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10715?size=medium](attachments/2311225345/2358280602) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10703?size=medium](attachments/2311225345/2358280580) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10703?size=medium](attachments/2311225345/2358280591) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10703?size=medium](attachments/2311225345/2358280254) (image/svg+xml)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[10715?size=medium](attachments/2311225345/2358280248) (image/svg+xml)  

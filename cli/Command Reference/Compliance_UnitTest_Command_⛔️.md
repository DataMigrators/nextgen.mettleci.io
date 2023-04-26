# Compliance UnitTest Command ⛔️

This is available on request to certain MettleCI direct customer
opportunities at the sole discretion of Justin McCamish and John
McKeever.

This documentation page remains - with viewing restrictions enabled and
the ⛔️ icon - purely for reference by Data Migrators engineers.

**DO NOT CHANGE THE VIEWING RESTRICTIONS OF THIS PAGE!**

This page also lacks some information required to make it useful:

-   An example unit test requirement file (.json)

-   An example with output

This page is for running MettleCI **COMPLIANCE RULES**.  If you're
looking for the Asset Queries typically used in a MettleCI Report Card
then please see the <a
href="https://datamigrators.atlassian.net/wiki/pages/resumedraft.action?draftId=458556115"
rel="nofollow">Compliance Query Command</a>.

# Purpose

Tests the supplied rules against the Jobs presented in a supplied list
(the ‘requirement file’) which is `json` formatted.

This command supports Compliance Rule development. Compared to the
`compliance test` command, which reports ‘*Job X failed Compliance Rule
X*', the `compliance unittest` command reports '*Job X failed Compliance
Rule X, but was expected to pass*’. The conclusion, then, would be that
the definition of Compliance Rule X has a problem.

# Syntax

# Example

This example demonstrates how to export a set of ISX files and run
Compliance against them. Note that asset paths specification in the
export command uses the
<a href="https://www.ibm.com/docs/en/iis/11.7?topic=command-asset-paths"
rel="nofollow">same wildcard rules</a> as the `istool` command.

``` bash
# ============================== 
# Export the required ISX assets
# ============================== 
$> mettleci isx export
     -domain services-host.mycorp.com:59445 
     -username myusername -password mypassword 
     -server engine-host.mycorp.com 
     -project my_project 
     -jobname .*/MyFolder/*.*

MettleCI Command Line (build 122)
(C) 2018-2020 Data Migrators Pty Ltd
Analyzing engine-host.mycorp.com/my_project
Exporting [.*/MyFolder/*.*] from repository...
Exporting DataStage assets...
 * Export 'engine-host.mycorp.com/my_project/Jobs/MyFolder/TestJob.pjb' - COMPLETED
 * Export 'engine-host.mycorp.com/my_project/Jobs/MyFolder/TestJob_0921.pjb' - COMPLETED
 * Export 'engine-host.mycorp.com/my_project/Jobs/MyFolder/TestJob_0930.pjb' - COMPLETED
Export complete

# ==================================================================
# Run the specified compliance rules against the exported ISX assets
# ==================================================================
$> mettleci compliance unittest \
  -rules compliance_rules \
  -assets datastage \
  -report compliance_report_warn.xml \
  -junit \
  -project-cache ./project-cache \
  -test-suite warnings \
  -ignore-test-failures \
  -include-job-in-test-name

MettleCI Command Line (build 122)
(C) 2018-2020 Data Migrators Pty Ltd
rules configuration discovered
new rule discovered - 'Adjacent Transformers' (PARALLEL_JOB)
new rule discovered - 'CCMigrateTool Stages' (PARALLEL_JOB)
new rule discovered - 'CCMigrateTool Stages' (SERVER_JOB)
new rule discovered - 'Database Row Limit' (PARALLEL_JOB)
new rule discovered - 'Database Row Limit' (SERVER_JOB)
new rule discovered - 'Debug Row Limit' (PARALLEL_JOB)
<SNIP>
new rule discovered - 'One Dataflow' (SERVER_JOB)
new rule discovered - 'Range Lookup' (PARALLEL_JOB)
new rule discovered - 'Too Many Stages' (PARALLEL_JOB)
new rule discovered - 'Too Many Stages' (SERVER_JOB)
new rule discovered - 'Unique Sort' (PARALLEL_JOB)
[1/3] TestJob_0921 (PARALLEL_JOB)
[2/3] TestJob_0930 (PARALLEL_JOB)
[3/3] TestJob (PARALLEL_JOB)

# Done!
$>
```

  
This example produces an output file `compliance.csv` in the current
directory which looks like this (formatted here for clarity):

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220609-082633.png](attachments/2236350465/2236350485.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220609-020256.png](attachments/2236350465/2236350488.png)
(image/png)  

# UnitTest Test Command

# Purpose

Run one or more MettleCI Unit Tests against one or more DataStage jobs.

The `-reports` option is used to specify the directory into which the
JUnit XML files produced by this command will be placed. Each job tested
will produce a separate XML file named after the Job (e.g. Job
`MY_JOB_ABC` will produce a JUnit file named `MY_JOB_ABC.xml`)

The `-ignore-test-failures` option will prevent a failing Unit Test from
being interpreted as a command failure by your build system, and
consequently halting your CI/CD pipeline.

See <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/1266843717/Repeatable+DataStage+Project+Deployments"
data-linked-resource-id="1266843717" data-linked-resource-version="8"
data-linked-resource-type="page">Repeatable DataStage Project
Deployments</a> for more details on how the `-project-cache` parameter
is used to implement **incremental tests**. For more information on
using the `-project-cache` parameter see our <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/1356890161/MettleCI+CLI+and+the+project-cache+directory"
rel="nofollow">detailed explanation</a>.

# Syntax

# Example

``` bash
C:\> mettleci.cmd unittest test ^
    -domain test1-svcs.datamigrators.io:59445 ^
    -server test1-engn.datamigrators.io ^
    -username isadmin ^
    -password my_password ^
    -project my_project ^
    -specs unittest ^
    -reports unittest_reports ^
    -project-cache "C:\MettleCI\cache\test1-engn.datamigrators.io\my_project"
MettleCI Command Line (build 128)
(C) 2018-2022 Data Migrators Pty Ltd
Loading Unit Test Specifications from 'unittest'
Reading test1-engn.datamigrators.io/my_project
Attempting to identify changes with 1 working threads.
Inspecting DataStage assets for changes...
 * Check test1-engn.datamigrators.io/my_project/Jobs/Transform/TR_ORDERS.pjb - COMPLETED
Change identification complete
Executing Tests with 4 concurrent jobs...
 * Test TR_ORDERS/TR_ORDERS - SKIPPED
Updating incremental state...
Attempting to identify last change with 1 working threads.
Inspecting DataStage assets for last change...
 * Check test1-engn.datamigrators.io/my_project/Jobs/Transform/TR_ORDERS.pjb - COMPLETED
Last change identification complete
Test execution completed successfully.

C:\>
```

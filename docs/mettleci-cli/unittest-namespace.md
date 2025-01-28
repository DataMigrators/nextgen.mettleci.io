---
status: reviewed #Status can be draft, reviewed or published. 
owner: John McKeever
tags:
  - DataStage
  - Running Tests
---
# UnitTest namespace

## UnitTest Generate

![unittest generate syntax](./images/unittest-generate.png "unittest generate syntax")

Generates a DataStage test case for one or more specified DataStage flows.

The optional `-check-row-count-only` flag will cause the generation of a test case which checks row counts, rather than the default option which is to compare data row-by-row.

### Example

```shell
$> mettleci unittest generate \
   -assets /opt/dm/mci/jobs \
   -joblist ./joblist.txt \
   -specs /opt/dm/mci/testspecs
```

---

## UnitTest Test

![unittest test syntax](./images/unittest-test.png "unittest test syntax")


Run one or more MettleCI Unit Tests against one or more DataStage jobs.

The `-reports` option is used to specify the directory into which the JUnit XML files produced by this command will be placed.  Each job tested will produce a separate XML file named after the Job (e.g. Job MY_JOB_ABC will produce a JUnit file named  MY_JOB_ABC.xml)

The `-ignore-test-failures` option will prevent a failing Unit Test from being interpreted as a command failure by your build system, and consequently halting your CI/CD pipeline. 

See [Repeatable DataStage Project Deployments]() for more details on how the -project-cache parameter is used to implement incremental tests. For more information on using the `-project-cache` parameter see our detailed explanation.


### The 'ignore-test-failures' option

MettleCI unit tests can be executed in two ways: 

1. Manually, using the MettleCI Workbench tool’s under interface, or
2. From the command line using the mettleci unittest test (documentation) command.

When using the MettleCI command line to execute unit tests from within a build orchestration system (Jenkins, GitHub actions, Bamboo, etc.) it’s important to understand how the mettleci unittest test command and your build system interact.

The  mettleci unittest test command has three potential outcomes:

* The command executes successfully and runs a unit test which passes,
* The command executes successfully and runs a unit test which fails, or
* The command fails to execute for any reason, and the unit test is never invoked (e.g. due to a misconfigured parameter such as referencing a non-existent unit test)

Like all shell commands, the `mettleci unittest test` command returns an [exit code](https://en.wikipedia.org/wiki/Exit_status) informing the host system of the success, or otherwise, of the invoked process - in this case a DataStage test case. By default, the `mettleci unittest test` command returns a non-zero (failure) result when either the command cannot complete or **when a unit test fails**. For many build orchestration systems this will cause the build to fail instantly and, most importantly, prevent the publication of the failed test’s associated [JUnit XML file](https://junit.org), making the process of diagnosing the test failure difficult.

The `mettleci unittest test -ignore-test-failures` option will prevent a failing unit test from being interpreted as a command failure by your build system, and consequently halting your CI/CD pipeline.


### Example

```bat
C:\> mettleci unittest test ^
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

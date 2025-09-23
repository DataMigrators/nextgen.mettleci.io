---
status: reviewed #Status can be draft, reviewed or published. 
owner: John McKeever
tags:
  - Pipeline
  - CLI
  - Asset Analysis
  - Tags
---
# asset-analysis namespace

The `asset-analysis` namespace contains commands for running MettleCI Asset Analysis Rules and Asset Queries from the command line.

## asset-analysis list tags

![asset-analysis list-tags syntax](../railroads/svgs/asset-analysis-list-tags.svg "aset-analysis list-tags syntax")

This command analyses a specified set of Asset Analysis Rules or Asset Analysis Queries and reports the tags defined for each.  Output is available in an easy-to-read tabulated for, or as a CSV for downstream processing. When no format option is specified the default is tabulated.

#### Parameters

  * -rules
      location of all the rule files
    -format
      output format, either 'table' or 'csv'
      Default: table

#### Example

This example shows how to list the tags of a directory of Compliance Rules in both tabulated and CSV formats:
      
```shell
# ####################################
# list-tags output in tabulated format
# ####################################
$> mcix asset-analysis list-tags -rules ~/Projects/bitbucket.org/compliance-rules -format table
MettleCI Command Line (build 174)
(C) 2018-2022 Data Migrators Pty Ltd
compliance list-tags (v2.2.x)
rules configuration discovered
included rule - 'Adjacent Transformers' (PARALLEL_JOB)
included rule - 'Adjacent Transformers' (SERVER_JOB)
... <SNIP> ...
included rule - 'Transformer With Unreferenced Stage Variable' (SERVER_JOB)
included rule - 'Unique Sort' (PARALLEL_JOB)
                                       Rule Name  Asset Type                 example  fail-ci  fail-upgrade  functionality  governance  maintainability  performance  portability  security  testability
================================================  =========================  =======  =======  ============  =============  ==========  ===============  ===========  ===========  ========  ===========
                           Adjacent Transformers  PARALLEL_JOB               -------  -------  ------------  -------------  ----------  maintainability  -----------  -----------  --------  -----------
                           Adjacent Transformers  SERVER_JOB                 -------  -------  ------------  -------------  ----------  maintainability  -----------  -----------  --------  -----------
                                Audit Annotation  PARALLEL_JOB               example  -------  ------------  -------------  ----------  maintainability  -----------  -----------  security  -----------
                                Audit Annotation  SEQUENCE_JOB               example  -------  ------------  -------------  ----------  maintainability  -----------  -----------  security  -----------
                                Audit Annotation  SERVER_JOB                 example  -------  ------------  -------------  ----------  maintainability  -----------  -----------  security  -----------
                                          <SNIP>  <SNIP>                     ...      ...      ...           ...            ...         ...              ...          ...          ...       ...
               Transformer Uses Abort After Rows  PARALLEL_JOB               -------  -------  ------------  functionality  ----------  ---------------  -----------  -----------  --------  -----------
               Transformer Uses Abort After Rows  PARALLEL_SHARED_CONTAINER  -------  -------  ------------  functionality  ----------  ---------------  -----------  -----------  --------  -----------
    Transformer With Unreferenced Stage Variable  PARALLEL_JOB               -------  -------  ------------  functionality  ----------  maintainability  -----------  -----------  --------  -----------
    Transformer With Unreferenced Stage Variable  SERVER_JOB                 -------  -------  ------------  functionality  ----------  maintainability  -----------  -----------  --------  -----------
                                     Unique Sort  PARALLEL_JOB               -------  -------  ------------  -------------  ----------  maintainability  -----------  -----------  --------  -----------
# ##############################
# list-tags output in CSV format
# ##############################
$> mcix asset-analysis list-tags -rules ~/Projects/bitbucket.org/compliance-rules -format csv
MettleCI Command Line (build 174)
(C) 2018-2022 Data Migrators Pty Ltd
compliance list-tags (v2.2-SNAPSHOT)
rules configuration discovered
... <SNIP> ...
Rule Name,Asset Type,example,fail-ci,fail-upgrade,functionality,governance,maintainability,performance,portability,security,testability
Adjacent Transformers,PARALLEL_JOB,,,,,,maintainability,,,,
Adjacent Transformers,SERVER_JOB,,,,,,maintainability,,,,
Audit Annotation,PARALLEL_JOB,example,,,,,maintainability,,,security,
Audit Annotation,SEQUENCE_JOB,example,,,,,maintainability,,,security,
Audit Annotation,SERVER_JOB,example,,,,,maintainability,,,security,
... <SNIP> ...
Transformer With Unreferenced Stage Variable,PARALLEL_JOB,,,,functionality,,maintainability,,,,
Transformer With Unreferenced Stage Variable,SERVER_JOB,,,,functionality,,maintainability,,,,
Unique Sort,PARALLEL_JOB,,,,,,maintainability,,,,
$>
```
 
---

## asset-analysis query
 
???+ info "This command is for running MettleCI Asset Queries"

    If you're looking for the **Compliance Rules** returned by DataStage flow analysis then see the [Compliance Test](#compliance-test-command) Command.

![asset-analysis query syntax](../railroads/svgs/asset-analysis-query.svg "asset-analysis query syntax")

The command line implementation of the Compliance Query functionality exposes the low-level mechanism to produce a report listing the results of the specified Asset Queries.

#### Parameters

  * ***-assets*** *(required)*

    Location of all json assets to query

  * ***-exclude-tag*** *(repeatable)*

    Tags of asset queries to exclude (case insensitive)

  * ***-include-tag*** *(repeatable)*

    Tags of asset queries to include (case insensitive), includes everything by default

  * ***-queries***

    Location of all the query files

  * ***-report***

    Report name (.csv)

  * ***-threads*** *(Default: 1)*

    Number of threads of execution



#### Example

This example demonstrates how to export  a set of ISX files and run Asset Queries against them. Note that asset paths specification in the export command uses the same wildcard rules as the istool command.

```shell
# ============================== 
# Export the required ISX assets
# ============================== 
C:\> mcix isx export ^
     -domain myteam-svcs.corp.com:59445 ^
     -username myuser -password mypassword ^
     -server myteam-engn.corp.com ^
     -project myproject ^
     -jobname .*LD_S.*
Exporting [.*LD_S.*] from repository...
Exporting DataStage assets...
 * Export 'test2-engn.datamigrators.io/myproject/Jobs/Load/LD_SUPPLIER.pjb' - COMPLETED
 * Export 'test2-engn.datamigrators.io/myproject/Jobs/Load/LD_STOCK_HOLDING.pjb' - COMPLETED
 * Export 'test2-engn.datamigrators.io/myproject/Jobs/Load/LD_STOCKITEM.pjb' - COMPLETED
 * Export 'test2-engn.datamigrators.io/myproject/Jobs/Load/LD_SALE.pjb' - COMPLETED
Export complete
# ================================================================
# Run the specified asset queries against the exported ISX assets
# ================================================================
C:\> mcix compliance query \
     -assets ./Jobs \
     -queries ./Queries \
     -report compliance.csv \
MettleCI Command Line (build 122)
(C) 2018-2020 Data Migrators Pty Ltd
 <SNIP>
# Done!
C:\>
```

---

## asset-analysis test

???+ info "This command is for running MettleCI Compliance Rules"

    If you're looking for the **Asset Queries** typically used in a MettleCI Report Card then please see the [Compliance Query](#compliance-query-command) Command.

![compliance test syntax](../railroads/svgs/compliance-test.svg "compliance test syntax")

The command line implementation of the Compliance Test functionality enables the production of a Compliance Results report of the specified assets against the specified set of MettleCI Compliance Rules.

For more information on using the `-project-cache` parameter see our [detailed explanation]().

#### Parameters

  * **-api-key**

      CP4D API key

  * **-exclude-tag**

    Tags of compliance rules to exclude (case insensitive)

  * **-ignore-test-failures** *(Default: false)*

    Returns zero when testing completes regardless of failures

  * **-include-job-in-test-name** *(Default: false)*

    Test case names will include the job name in the jUnit report

  * **-include-tag**

    Tags of compliance rules to include (case insensitive), includes everything by default

  * **-path**

    Location of project export directory or zip file

  * **-project**

    Project Name

  * **-project-cache**

    Project cache directory, enables incremental testing

  * **-report** *(requried)*

    Report name (.csv or .xml)

  * **-rules** *(required)*

    Location of all the rule files

  * **-test-suite**

    Name of test suite being run, only required if running this command multiple times for the same project

  * **-url**

    Base URL for CP4D instance

  * **-username**

    CP4D user name


#### Example

This example demonstrates how to export  a set of ISX files and run Compliance against them. Note that asset paths specification in the export command uses the same wildcard rules as the istool command.

```shell
# ============================== 
# Export the required ISX assets
# ============================== 
C:\MettleCI\cli\> mcix isx export ^
     -domain myteam-svcs.corp.com:59445 ^
     -username myuser -password mypassword  ^
     -server myteam-engn.corp.com  ^
     -project myproject  ^
     -location C:\shared\myproject\export  ^
     -include-binaries  ^
     -project-cache C:\shared\myproject\cache
Analyzing test2-engn.datamigrators.io/myproject
Attempting to identify changes with 4 working threads.
Inspecting DataStage assets for changes...
<SNIP>
Change identification complete
Inspecting ParameterSet definition changes...
ParameterSet definition change identification complete
Deleting assets...
<SNIP>
Deletion complete
Exporting DataStage assets...
<SNIP>
Export complete
Attempting to identify last change with 4 working threads.
Inspecting DataStage assets for last change...
<SNIP>
Last change identification complete
# ==================================================================
# Run the specified compliance rules against the exported ISX assets
# ==================================================================
$> mcix compliance test
  -rules compliance_rules
  -assets datastage
  -report compliance_report_warn.xml
  -junit
  -project-cache ./project-cache
  -test-suite warnings
  -ignore-test-failures
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

## References

For a discussion on the use of the `include-tags` and `exclude-tags` options see [Asset-Analysis Rule Tags]().









mcix>asset-analysis
Expected a command
Usage: asset-analysis [command] [command options]
  Commands:
    query      Query one or more Information Server assets
    test      Compliance test one or more Information Server assets
    console      Experimental REPL console
    unittest      Unit test compliance rules using DS Flows with expected
            results


mcix>asset-analysis test^[[C
Expected a command, got test
Usage: asset-analysis [command] [command options]
  Commands:
    query      Query one or more Information Server assets
    test      Compliance test one or more Information Server assets
    console      Experimental REPL console
    unittest      Unit test compliance rules using DS Flows with expected
            results



mcix>asset-analysis console
asset-analysis console
There was an error running command. It has been logged (ID 5f37a6e68e6b3e02).
mcix>asset-analysis unittest
The following options are required: [-specs], [-rules], [-report]
Usage: asset-analysis unittest [options]
  Options:
    -api-key
      CP4D API key
    -path
      location of project export zip files
    -project
      Project Name
  * -report
      report name (.xml)
  * -rules
      location of all the compliance rules to be tested
  * -specs
      location of all the compliance unit test specification files
    -url
      Base URL for CP4D instance
    -username
      CP4D user name

mcix>
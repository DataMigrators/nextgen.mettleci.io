---
status: draft #Status can be draft, reviewed or published.
owner: John McKeever
tags:
  - DataStage
  - Flow Analysis
  - Reference
---
# Supplied flow rules

## Adjacent Transformers

#### Summary
	
Identifies flow designs with adjacent Transformer stages.

#### Description

Although powerful, transformers contain embedded logic that's not immediately obvious when looking at the canvas and reduces a developers ability to immediately understand a flow's logic. Overuse of transformers when more 'verbose' stages could achieve the same outcome can result in greater maintenance overhead.

THe presence of Adjacent transformers can be a symptom of a single transformer that has become so complex that a developer has needed to split its logic across two transformers. When this occurs, developers should consider if they could adopt an alternative implementation strategy using multiple standard stages working in conjunction rather than performing all logic within one or more transformer stages.

Adjacent transformers can also be a symptom of defect fixes that are clumsily 'tacked on' to an existing job rather than understanding the existing job logic and refactoring accordingly. Making job changes without having to refactor the existing code will degrade job quality and increase maintenance costs over time.

#### Actions

Adjust your job design so that there are no adjacent transformers. Consider combining adjacent Transformer stages if possible.

---

## Aggregator Stage Not Preceded by Check Sort Stage

#### Summary

Aggregator Stage will only return the correct result if the keys are pre-sorted
In some organisation, the data are sourced from presorted dataset.

However, mistakes can happen. If the dataset isn't presorted, the output from Aggregator Stage will be incorrect. One way to ensure the accident would not happen, without impacting the performance is to include a check sort stage before Aggregator Stage.

#### Description

This rule perform the following checks:

1. The Aggregator stage is preceded by a Sort stage
2. The keys of the Aggregator Stage are a subset of those of the Sort Stage
3. The keys of the Sort Stage are set to either `(Previously Sorted)` or `(Previously Grouped)`

#### Actions

Add a Check Sort stage to before Aggregator stage.

---

## Audit Annotation

#### Summary

Identifies where sensitive information may be present in DataStage Job and Sequence annotations.

#### Description

This rule scans all annotations for instances of the words `hostname`, `password`, `organisation` (`en-UK` spelling) or `organization` (`en-US` spelling).

Note that it's impossible to use regular expressions to detect a password, host name, or organisation, but assuming one of these words is found the likelihood of the actual sensitive information being present is high.

Like all MettleCI Compliance Rules, this rule is provided as an example intended for you to adapt to suit your needs.

#### Actions

Remove the sensitive information from your Job or Sequence annotation.

---

## Connection Contains Parameter References

#### Summary

Identifies Connections created by the migration from legacy DataStage to NextGen that contain references to Flow parameters.

#### Description

https://www.ibm.com/docs/en/cloud-paks/cp-data/4.0?topic=datastage-migrating#reference_fbm_gww_yqb__post-mig__title__1

During the process of migrating legacy DataStage projects to NextGen, connection details and credentials are moved from the job into a separate Connection, which may be also used outside of a DataStage context. When the connection details are parameterised those parameter references are copied into the Connection object. These must then be replaced with real credentials so it can be tested and saved.

#### Actions

Replace the parameter references with actual connection details.

---

## Connection Not Using Secrets Vault

#### Summary

Identifies Connections that don't store their credentials to use secrets in a vault.

#### Description

Connections have the option of retrieving their credentials from a secret in a vault. If this option isn't taken the credential values are stored in plain text when the connection object is exported from the project, despite being displayed in the user interface as encrypted.

#### Actions

Update the connection, setting the Input Method as 'Use secrets from a vault' .

---

## DataSet Not Using Same Partition

#### Summary

Identifies Data Sets not using the 'Same' partitioning method

#### Description

This rule identifies Parallel Job Data Sets which don't use the 'Same' partitioning method.

This is an IBM development tip documented here: [Sorting data - IBM Documentation](https://www.ibm.com/docs/en/iis/11.7?topic=tips-sorting-data) 

#### Actions

When reading from Data Sets maintain your sort order by using ‘Same’ partitioning method.

---

## Database Connector Not Using Auto Generate SQL

#### Summary

Identifies database connections that don't use the `Auto Generate SQL` option.

#### Description

In InfoSphere Information Governance Catalog, the schema and database table name of the imported database must be the same as the schema and database table name in the stage.

You can generate default SQL statements to read from and write to data sources.
Alternatively, you can specify SQL statements manually that read from and write to data sources.
SQL that you specify might contain certain DBMS vendor-specific constructs that can't be parsed correctly in job lineage analysis.

As a result, the relationships between stages and data sources and between stages and other stages might be incorrect.

#### Actions

Update the connector to use Auto Generate SQL.

---

## Database Query From File

#### Summary

Ensures if Database Connectors and Stages reads SQL statement from file.

#### Description

Developers occasionally wants to keep the SQL statements flexible, and use external file for SQL statements.
However, SQL statements from external files don't go to the metadata repository where they can be used for 
job flow analysis. These SQL statements are also not included in operational metadata XML files.

This can make the job harder to maintain as it contains external objects, and failure when deploying to a different project of server.

It's recommended for developers to use parameters instead of an external file if they wish to benefit from the flexibility of using SQL statements.

#### Actions

Update the Connector to use the `Read select statement from file` property.

---

## Database Row Limit

#### Summary

Identifies Connectors Stages with a configured Database Row Limit.

#### Description

Row limits set on the Database stages are options developers might use during development and unit testing to allow faster development. Leaving these options set may have unintended consequences should the job be deployed into test and production environments.

#### Actions

Remove the configured row limit.

---

## Database Table References are Fully Qualified

#### Summary

Identifies where database table references aren't fully qualified.

#### Description

Database table references can sometimes cause problems when migrating from Development to downstream QA and Production environments as they will likely be communicating with different databases to those used in Development. Those databases may well have different configurations to those that were iused to develop the the Flow and there may arise some confusion about which schemas or other database objects are being referenced by the Flow.

#### Actions

Ensure all database object references used by your Flow are fully qualified. For example, `{schema}.{tablename}`

---

## Data Format in Annotation

#### Summary

Identify whether the a Flow annotation contains instances of particular arbitrary text.  This example rule looks for dates.

#### Description

Identify whether the a ‘Job Description’ annotation contains instances of particular arbitrary text. You can modify this rule to get it to seek out any text your team wants to prevent passing compliance.  This example rule looks for text matching the following date formats:

| Format                                         | Description                                      |
|------------------------------------------------|--------------------------------------------------|
| `YYYY-MM-DD`, `YYYY/MM/DD`, `YYYY MM DD`       | YYYY-MM-DD format with `/` or `-` as a delimiter |
| `YYYY-MMM-DD`, `YYYY/MMM/DD`, `YYYY MMM DD`    | Month format can be MM, MMM, MMMM, or MON        |
| `YYYY-MMMM-DD`, `YYYY/MMMM/DD`, `YYYY MMMM DD` | MMM and MMMM are Excel Syntax                    |
| `DD-MM-YYYY`                                   | Similar to YYYY-MM-DD                            |
| `MM-DD-YYYY`                                   | Similar to YYYY-MM-DD (common US date format)    |

#### Actions

Remove or alter the text that references a date.

---

## Db2 with No Non Recovery Load

#### Summary

Identify Db2 Stages using bulk load with Non Recovery Load set to 'No'.

#### Description

This rule warns developers using Db2 bulk load with Non Recovery Load set to 'No' which could require the restoration of the Db2 database if it crashes during the execution.

#### Actions

User dependent.

---

## Debug Row Limit

#### Summary

Identifies row limits in debug stages (Peek, Sample, Tail)

#### Description

Debug stages are options developers might use during development to enable debugging and testing. Leaving these options set may have unintended consequences should the job be deployed into test and production environments.

#### Actions

Remove either the Debug Row Limit setting, or remove the Stage within which it is set.

---

## Default Naming

#### Summary

Default Stage Names for Parallel Jobs, Server Jobs, and Job Sequences

#### Description

Stages should be given meaningful names, to improve readability and reduce bug-fixing effort. The use of default (DataStage-supplied) names (e.g. `Link123`) suggests that jobs might possibly be not quite finished.

#### Actions

Ensure that all Jobs, Sequences, Stages, and Links are given user-chosen names (not just defaults) which align with your naming standards. 

---

## Duplicate File References

#### Summary

Verifies that a sequential file is...
 - only referenced once in a DataStage Flow's Sequential File, Complex Flat File, or DataSet stages, and
 - not simlutaneously being read and written in the same DataStage Flow

#### Description

Sometimes developers will copy and paste stages rather than adding a new stage from the palette. In doing so there is a risk that the developer may not update the reference to the filename property which may result in incorrect processing being performed by the DataStage flow.

#### Actions

Ensure that a file is only referenced once in a DataStage flow.

---

## Duplicate Stage Names

#### Summary

Detect duplicate Stage names in a job.

#### Description

This can create issues with Unit Testing and potentially other Information Server tools. The chances of occurrence is rare, but not impossible, especially with assets imported from legacy DataStage instances.

#### Actions

Adjust your Job’s Stage names to remove duplicates.

---

## File Reference Missing Required Parameter

#### Summary

Ensures that all File Stages must use variables for determining paths

#### Description

Developers occasionally hard code file paths while debugging or developing. 
<!-- We're about to use the word 'Job' properly -->
<!-- vale Vale.Avoid = NO -->
These will cause job failures when deploying to a different project or server. 
<!-- vale Vale.Avoid = YES -->
This problem is usually solved by using a project-specific variable to define the base path for file based stages such as datasets. This compliance rule will identify hard coded file paths by checking that the pathname includes at least one predefined path parameter. 
You can customise the predefined path parameters (and the stages for which they can be used) by modifying the `pathParameters` variable.

#### Actions

Use a project-specific variable to define the base path for file based stages.

---

## File Row Limit

#### Summary

Identifies row limits in file-based stages (Sequential File, Complex Flat File).

#### Description

Row limits set on the file stages are options developers might use during development and unit testing to allow faster development. Leaving these options set may have unintended consequences should the flow be deployed into test and production environments.

#### Actions

Remove the row limit on identified Stages.

---

## Flow Naming

#### Summary

Checks whether the Flow name matches one of a list of prohibited name patterns.

#### Description

Developers will occasionally work on a copy or Work-In-Progress version of a Flow but forget to rename it before pushing it to Git. This simple compliance test makes these mistakes visible at check-in time by determining whether it matches a list of known prohibited name patterns (such as `CopyOf*`, for example.)

See the documentation on asset naming standards for the default list of naming signatures on the prohibited list.

#### Actions

Rename the Flow to align with your coding standards and remove ambiguity. 

---

## Flow Parameter Missing Default Value

#### Summary

Identify flow parameters within a default value.

#### Description

It is good practice to consider the use of default parameter values to protect flows from unintended behaviour when invoked without providing all required parameter values.

#### Actions

Ensure all your flow parameters have a default value.

---

## Flow Parameter Naming

#### Summary

Identifies where naming standards for Flow Parameters and Parameter Sets are breached.

#### Description

Identifies where naming standards for Flow Parameters Parameter Sets are breached 

#### Actions

Ensure your Flow Parameters and Parameter Sets are named according to your standards. 

---

## Flow Parameter Missing Default Value

#### Summary

Identify Flow Parameters that are not in a Parameter Set.

#### Description

It is good practice to consider the use of Parameter Sets to store Flow Parameters.  Parameter Sets help to make your jobs more flexible and reusable across environments.

#### Actions

Ensure all your Flow Parameters are included in a Parameter Set.

---

## Flow using random function

#### Summary

Identifies Transformers (or other stages) using DataStage functions which produce non-deterministic output.

#### Description

DataStage functions `Rand()`, `Random()` and `Srandom()` are examples of functions which produce non-deterministic output. Columns whose values are dependent upon these functions will produce unpredictable results which can't be used in MettleCI unit tests.

#### Actions

Parameterise your flow designs by specifying the required non-deterministic value as a flow parameter. This value will then be supplied with a fixed value at invocation time to guarantee a predictable unit test result.

---

## Flow using transformer surrogate key

#### Summary
	
Identifies flow designs that use the `NextSurrogateKey()` call in a Transformer stage.

#### Description

Although powerful, transformers contain embedded logic that's not immediately obvious when looking at the canvas and reduces a developers ability to immediately understand a flow's logic. Overuse of transformers when more 'verbose' stages could achieve the same outcome can result in greater maintenance overhead.

#### Actions

Adjust your flow design to use a Surrogate Key Generator stage instead.

---

## Hardcoded DB Credentials

#### Summary

Ensures that all Database Connectors must use variables for location and credentials

#### Description

Developers occasionally hard code database credentials into their jobs. These will cause job failures when deploying to a different project or server.

#### Actions

Parameterise the identified hard-coded values.

---

## Hardcoded File Paths

#### Summary

Ensures that all File Stages must use variables for determining paths

#### Description

Developers occasionally hard code file paths while debugging or developing. These will cause job failures when deploying to a different project or server. This problem is usually solved by using a project specific variable to define the base path for file based stages such as datasets. This compliance rule will identify hard coded file paths by checking that the pathname includes at least one predefined path parameter.

The predefined path parameters and the stages for which they can be used with can be customised by modifying the `pathParameters` variable.

#### Actions

Parameterise the identified hard-coded file paths.

---

## Join Partition vs Join Key

#### Summary

Reports Join stages where the join key does not match the partitioning of the input links.

#### Description

In the parallel DataStage engine, data is internal split into separate partitions in order to run a number of smaller operations concurrently. This results in faster and more efficient processing, especially when sorting and joining data.

For Hash, Range and Modulus partitioning methods, they use column values to determine the partition which partition each record is placed into. For Same, the actual partitioning method is propagatedfrom upstream, and so we need to traverse up to the preceding stages until a specific method is selected (or until we reach the data source and can go no further).

For a pair of records in the left and right links to join, they must both be placed in the same partition.

If the columns used to determine the partition allocation are not in alignment with the keys used to join the two sources of data, records that are supposed to join may be in different partitions, and therefore not join as expected.

| Join Key           | Join Partition     | Result    |
|--------------------|--------------------|-----------|
| key1               | key2               | fail      |
| key1, key2         | key2               | fail      |
| key1, key2         | key1, key2         | pass      |
| key1, key2         | key1               | pass      |
| key1               | key1               | pass      |

#### Actions

Ensure partitioning methods and columns are in alignment with selected join keys.

---

## Link Sort

#### Summary

Identifies link sorts.

#### Description

Developers where possible should utilise the sort stage rather than utilising the link sort facility. The sort stage allows more options for controlling the behaviour of the sort operation, appears in the job monitor as well as better communicating visually to other developers the main functions of the DataStage Flow.

This rule identifies Flows that utilise implicit sorts on a link which may prevent thedeveloper from taking advantqage of some opportunities for performance optimisation, and may reduce the easy maintainability of your Flows. Both link Sorts and explicit Sorts generate the same underlying orchestrate operators, however the explicit Sort stage offers the following options which are ot available on a link Sort:
 
- Sort Key Mode
- Create Cluster Key Change Column
- Create Key Change Column
- Output Statistics
- Sort Utility
- Restrict Memory Usage

#### Actions

Replace link sorts with an explicit Sort stage.

---

## Log Column Values

#### Summary

Identify Stages configured to Log column values on first row error

#### Description

The Log column values on first row error property is a feature used for debugging purpose. It outputs error rows in plain text to your DataStage Job log.

This creates the potential for error rows containing sensitive information to be divulged to unauthorised parties.

#### Actions

Disable the Log column values on first row error property.

---

## Lookup Failure

#### Summary

Identifies Lookup Stages with Lookup set to Fail.

#### Description

Lookup stages have a ‘Condition Not Met’ setting which describes what happens when a key lookup fails.  Options are:

**Continue** - The fields from that link are set to NULL if the field is nullable, or to a default value if not, and processing continues

**Drop** - Drops the row and continues with the next lookup

**Fail** - Causes the job to issue a fatal error and stop

**Reject** - Sends the row to the reject link

By default Lookup stages are configured to Fail should a key lookup fail. This unexpected job abort is, in most cases, not the behaviour the developer intended. These lookup fails should be handled gracefully in the ETL job.

#### Actions

Reconfigure your Lookup stage so that reference links are not set to abort the job should a key lookup fail.

---

## One Data flow

#### Summary

Verifies that there is only one data flow in a DataStage Flow.

#### Description

A DataStage Flow has no restrictions on the number of independent data flows that can be created. Ideally a DataStage Flow should be created for each data flow to allow the calling application to manage the execution order.

#### Actions

Split your Flow so that each separate data flow is defined within its own dedicated Flow. 

---

## Oracle Connector Not Using Partition Read

#### Summary

Identify Oracle Stages not configured to use partitioned reads.

#### Description

When an Oracle Connector Stage running in a Parallel Flow is configured to read data in parallel mode each node of the connector operator reads a distinct subset of data from the source table.  It achieves this by running a subtly modified `SELECT` statement on each node. The combined set of rows from all of the queries is the same set of rows that would be returned if the unmodified user-defined `SELECT` statement were run once on one node.  This approach requires that you configure your Oracle Connector Stage appropriately, and can deliver significant performance improvements over using a single-node read operation. 

#### Actions

Ensure that you [configure your Oracle Connector Stage](https://dataplatform.cloud.ibm.com/docs/content/dstage/dsnav/topics/oracle-opt-connector.html?#oracle-opt-connector__reading_partitioned) appropriately.

---

## Password Param Type Not Encrypted

#### Summary

Flow parameters with names that suggest they will be used for supplying passwords should be set to use the type "Encrypted".

#### Description

Job parameters with names that suggest they will be used for supplying passwords should be set to use the type Encrypted.  If they are not encrypted then their plain text contents could present a security risk.

#### Actions

Set Job parameters used for supplying passwords to use the type Encrypted.

---

## Watson Pipeline Calls DataStage Job with Hardcoded Parameter Values

#### Rationale:

In Watson Pipelines, Job Activity stages calling DataStage jobs with parameters should have those parameters 
populated from the pipeline itself, to ensure the pipelines and individual jobs operate conistently.

In Watson Pipelines, parameters may come from 1 of 5 sources, as displayed in the configuration window:

* Default job parameter configuration - the default source. This parameter is known as being "linked" to the child job
	* Note: As a key point of difference between Watson Pipelines and Sequence Jobs in DataStage Classic, these parameter references 
are not stored in the Watson Pipeline asset, and are therefore invisible to this model
* Enter Value - a hardcoded value passed in from the Watson Pipeline to the child DataStage job (known internally as 'SELECT_RESOURCE')
	* Select From Another Node - a property from another Watson Pipeline node, eg: return status, stand output, etc  ('SELECT_FROM_NODE')
* Assign Pipeline Parameter - allows the Pipeline to control the input of the childe DataStage job at runtime ('FLOW_PARAM')
* Enter Expression - Create a more complex input value, using a builder that offers a number of string, date/time and conversion functions ('EXPRESSION')

---

## Watson Pipeline Contains Unmigrated Job Routine

#### Summary

Identifies stages in a migrated Watson Pipeline that unresolved placeholders for Server Routine conversion

#### Description

Server Routines in DataStage Classic sequence jobs are not supported in Cloud Pak Data.
The migration process converts the Job Routine Activity stage into what looks like a Run Bash Script stage, but is actually just a placeholder.

Once a bash script has been entered into the UI, saving the job converts this stage into a normal CPD Run Bash Script stage.

---

## Watson Pipeline Not Restartable

#### Summary

Identifies Watson Pipeline jobs that are not "restartable", ie: if a job run partially succeeds before aboorting,
re-running the job will skip the initial successful stages and re-commence from the previous point of failure.

#### Rationale

The concept of restartability in Watson Pipelines is a little more complex than it was in DataStage Classic.
 
First, a job has to create a data cache, and then it has to decide to use the previously created cache.
The options and their associate behaviour is documented [here](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-orchestration-global-settings.html?context=wx&audience=wdp).

This rule identifies the following scenarios:

  - If the job default Cache Mode is set to `Never` this tells CPD to ignore previously created caches, 
    which forces it to run again from the beginning.
  - If every stage that has the option to create a cache either has it turned off, or has its Creation/Copy 
    Mode set to Overwrite, there are no checkpoints to use in the case of failure,
    which again will force a full run from the start of the Pipeline

---

## Prohibited Stages

#### Summary

Verifies that a job does not contain one or more prohibited stages.

#### Description
Some projects may wish to restrict certain stages from production ready jobs. For example, peek stages are usually included by developers as a debugging aid and therefore should be removed after initial development.

The list of prohibited stages is easily configurable, and is currently defined as:


    // File
       'PxzOSFile',                 // zOSFile
    // Packs
       'EssbaseConnectorPX',        // Essbase Connector
       'PS_HRYPX',                  // Hierarchy for PeopleSoft Enterprise
       'PeoplesoftOnePX',           // JD Edwards EnterpriseOne
       'ORAAppsPX',                 // Oracle Applications Direct Access
       'orahrchy_PX',               // Oracle Applications Hierarchy
       'SALESFORCEJCConnectorPX',   // Salesforce
       'Siebel_BCPX',               // Siebel BC Pack
       'Siebel_DAPX',               // Siebel DA Pack
       'Siebel_EIMPX',              // Siebel EIM Pack
    // Processing
       'PxSVTransformer'            // BASIC Transformer

#### Actions

- Redesign your job to avoid the use of prohibited stages, or
- Update the list of prohibited stages to permit stages you wish to permit.

---

## Range Lookup

#### Summary

Checks that range lookups are correctly configured.

#### Description

When setting up a [range lookup](https://www.ibm.com/docs/en/iis/11.7?topic=stage-range-lookups), DataStage will build the lookup table based on the primary key fields but not the range fields. If the range option is enabled on the reference link, this will result in duplicates being ignored and the range lookup won't work as expected.

This rule will check that range lookups have been configured to allow duplicates on the reference link and prevent unexpected results due to an incorrectly configured stage.

#### Actions

Ensure range lookups are configured to allow duplicates on the reference link.

---

## Redundant Sort

#### Summary

Identifies unnecessary sort opertions within Job designs.

#### Description

Sorting record data is the most expensive operation that can be performed by DataStage's Parallel Engine. While most experienced developers will arrange job logic to minimise the number of required sorts, there are valid patterns that use adjacent sort stages in conjunction with key change and cluster key flags.

This rule will identify adjacent sort stages which do not create key change, cluster key or have keys flagged as Don't Sort. Where adjacent sort stages are discovered, one will either be redundant and should be removed or a developer has introduced a logic error by not including a key change, cluster key or Don't sort flag.

#### Actions

Remove redundant sorts.

---

## SQL in DB Connectors

#### Summary

Identifies DB Connectors which use an SQL to filter source data

#### Description

Both legacy Enterprise Database Stages and Connector Stages provide a number of mechanisms for specifying the means of specifying the data they should retrieve:

| Query mode | Description | Behaviour | 
|——------———-|————————————-|———————————| 
| User Query 	| A custom query specified in the Stage properties	 				| Rule fails | 
| SQL Builder 	| Construct a custom SQL statement with a user interface 			| Rule fails | 
| SQL File 		| A file containing an SQL query is loaded and executed at runtime. | Rule fails | 
| Table Query 	| Select the name of the table to use from a drop-down list 		| Rule fails if SELECT or FILTER clauses specified 	| 
| Generated 	| Underlying SQL is generated by the Stage at runtime 				| Rule fails if WHERE or OTHER clauses specified 	|

This rule checks for the use of hardcoded SQL in properties of Database Enterprise Stages and Connector Stages. Development teams may choose to avoid using hardcoded SQL to filter data and instead opt to use downstream stages to process database output.

This rule only permits generated SQL where there are no other clauses specified in connector with that option. Any use-defined SQL, generated SQL with additional clauses or query file inputs will fail. 

#### Actions

Configure your Enterprise Database Stages and Connector Stages to use an approach which does not necessitate the use of hard-coded SQL.

---

## Schema Files

#### Summary

Detect use of Schema Files.

#### Description

In the Upgrade scenario, Schema Files are file system assets that need to be managed and migrated separately.  This rule identifies references to schema files which you will need to manage.

#### Actions

Ensure your schema files are governed in the same manner as your other DataStage assets. 

---

## "Select *" in Custom SQL

#### Summary
	
Identifies where "select *" syntax has been used in custom SQL code in database Connectors.

#### Description

Using Select * in custom SQL code may be indicative of:
	- SQL code that has been directly lifted from a SQL editor and inserted in to DataStage without further analysis or consideration
	- code that ignores future changes to the source and possibly produces misleading errors in the DataStage logs

#### Actions

Modify your Connector Stages' SELECT statements to use explicit column names. 

---

## Sequential File Read Using Same Partitioning

#### Summary

Avoid reading from Sequential Files using the 'Same' partitioning method.

#### Description

Avoid reading from sequential files using the 'Same' partitioning method.  Unless you have specified more than one source file this will result in the entire file being read into a single partition, making the entire downstream flow run sequentially unless you explicitly re-partition.

#### Actions

Configure your Sequential File Stage to use a partitioning method other than 'Same'.

---

## Sequential File With Reject Mode Not Set To Fail

#### Summary

Identifies Sequential Files with a Reject Mode not set to fail

#### Description

Some scenarios may require you to identify where an input Sequential File contains errors and cease processing.  In this case you would set your Sequential File’s Reject Mode to fail.  This rule assist this process by identifying when the Reject Mode is set to Continue or Save.

#### Actions

Set your Sequential File’s Reject Mode appropriate to your needs.

---

## Sort Post Join Stage

#### Summary

Identifies potentially redundant sorting (a sort stage or link sort) situated immediately after a Join stage

#### Description

Sorting is resource intensive, and when used excessively can impact performance.  This rule identifies Jobs that sort the output of a Join stage, which is a potentially redundant operation.

#### Actions

Review the Job design and remove the Sort if redundant.

---

## Stage Naming

#### Summary

Stage naming standards for DataStage flows and watson pipelines.

#### Description

Verifies that a Flow's stage names match the specified naming standards. All naming standards are based on example asset naming standards and are expected to be customised to customer requirements.

The supplied naming standards are designed to reduce the amount of effort required for developers to understand what a Flow is doing without needing to inspect each stage on the Flow canvas and to quickly identify Flow stages from text based messages such as logged errors and compliance rule failures.

In most cases, this is achieved by having a prefix that reflects the stage type. However, for stages such as joins and funnels, the stage names provide additional information which cannot be determined without inspecting the stage in question (ie. inner/left/right join).

#### Actions

Ensure your flow stages or Watson pipeline DataStage components are named according to your naming standards.

---

## System Time Dependency

#### Summary

Identifies the use of system time functions in the job

#### Description

Flows with date logic that reads from the system time make it difficult to perform repeatable/automated testing. Instead of using system date functions, it is recommended that the current date be passed in as a Flow parameter or derived from one of the `DSJobStart*` macros. During unit testing, the Flow parameter or `DSJobStart*` macro can be set to a fixed value. The actual job results can then be compared with the expected results without needing to account for differences due to system time.

#### Actions

Replace the reference to the system time or date with a Flow Parameter of the appropriate type.

---

## Too Many Stages

#### Summary

Identify whether a flow has too many stages.

#### Description

A flow design that contains too many stages becomes hard to maintain. 
Not only is it difficult to follow the logic but even physically moving around it and finding specific logic is hard.

This rule detects when a Flow or local Sub-flow exceeds a globally configurable stage limit. 
The default 'stageLimit' parameter is set to 25 but can be easily adjusted as required.  Stages contained in shared Subflows are excluded from the stage count.

#### Actions

Split your flow into multiple flows, or remove unnecessary Stages.

---

## Transformer Uses Abort After Rows

#### Summary

Detect an 'Abort after rows' greater than 0 setting in a Parallel Transformer.

#### Description

This rule detects Parallel Transformer with an 'Abort after rows' setting greater than 0. This could be considered bad practice in some organisations as rows unexpectedly appearing on a given link could be more gracefully handled by introducing an error-handling process which does not cause a job to abort.

#### Actions

Set the 'Abort after rows' value to 0 and provide downstream logic to report and handle the erroneous rows.

---

## Transformer With Unreferenced Stage Variable

#### Summary

Identifies Transformer Stage with an unreferenced Stage Variable (including Loop Variables).

#### Description

A Transformer can be resource intensive, and having an unreferenced (i.e. unused) Stage/Loop variable...

 - can be an unnecessary waste of resources,
 - can cause confusion to Flow maintainers, and
 - may present a security vulnerability.

This rule identifies forgotten/unreferenced Stage/Loop variables.


#### Actions

Remove the unreferenced Stage/Loop variable.

---

## Unencrypted database passwords

#### Summary

Identifies connector stages which do not use encrypted passwords

#### Description

Unencrypted passwords are a security risk and should be avoided. 

In DataStage all hardcoded password values are encrypted, and references to parameters are in plain text. This rule, therefore, simply needs to exclude:

- encrypted values, ie: `{dsnextenc}`
- a parameter that is set as 'encrypted'
- a reference to a parameterset, as the flow configuration does not store the details of parameters inside parametersets

---

## Unique Sort

#### Summary

Identifies unique sorts.

#### Description

Unique sorts are not visually represented on the DataStage canvas. Ideally the developer should use the Remove Duplicates stage so that this can be visually communicated with other developers. This rule will identify sort stages which have the `Allow Duplicates` property set to `false`.

#### Actions

Replace unique sorts with a Remove Duplicates stage.

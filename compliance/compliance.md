# MettleCI Cloud Pak Compliance Rule Reference

This page lists the example DataStage compliance rules suplied with MettleCI for IBM Cloud Pak for Data.

| Rule name | Description |
|-----------|-------------|
| [Adjacent Transformers](Adjacent\ Transformers.md) | Identifies flow designs with adjacent Transformer stages. |
| [Aggregator Stage Not Preceded by Check Sort Stage](Aggregator Stage Not Preceded by Check Sort Stage.md) | Aggregator Stage will only return the correct result if the keys are pre-sorted |
| [Audit Annotation](Audit Annotation.md) | Identifies where sensitive information may potentially be present in DataStage Job and Sequence Annotations. |
| [Connection Contains Parameter References](Connection Contains Parameter References.md) | Identifies Connections created by the migration from legacy Datastage to NextGen that contain references to |
| [Connection Not Using Secrets Vault](Connection Not Using Secrets Vault.md) | Identifies Connections that do not store their credentials to use secrets in a vault. |
| [DB Connector Not Auto Generate SQL](DB Connector Not Auto Generate SQL.md) | Identifies Connections that do not use Auto Generate SQL. |
| [DB Tables Referenced Are Fully Qualified](DB Tables Referenced Are Fully Qualified.md) | Identifies where database table references are not fully-qualified. |
| [DB2 with No Non Recovery Load](DB2 with No Non Recovery Load.md) | Identify Db2 Stages using bulk load with Non Recovery Load set to 'No'. |
| [DataSet Not Using Same Partition](DataSet Not Using Same Partition.md) | Identifies Data Sets not using the 'Same' partitioning method |
| [Database Query From File](Database Query From File.md) | Ensures if Database Connectors and Stages reads SQL statement from file. |
| [Database Row Limit](Database Row Limit.md) | Identifies Connectors Stages with a configured Database Row Limit. |
| [Date Format in Annotation](Date Format in Annotation.md) | Identify whether the a Flow annotation contains instances of particular arbitrary text.  This example rule looks for dates. |
| [Debug Row Limit](Debug Row Limit.md) | Identifies row limits in debug stages (Peek, Sample, Tail) |
| [Default Naming](Default Naming.md) | Default Stage Names for Parallel Jobs, Server Jobs, and Job Sequences |
| [Duplicate File References](Duplicate File References.md) | Verifies that a sequential file is... |
| [Duplicate Stage Names](Duplicate Stage Names.md) | Detect duplicate Stage names in a job. |
| [File Reference Missing Required Parameter](File Reference Missing Required Parameter.md) | Ensures that all File Stages must use variables for determining paths |
| [File Row Limit](File Row Limit.md) | Identifies row limits in file-based stages (Sequential File, Complex Flat File). |
| [Flow Naming](Flow Naming.md) | Checks the Flow name against a list of known prohibited name patterns. |
| [Flow Parameter Missing Default Value](Flow Parameter Missing Default Value.md) | Identify flow parameters within a default value. |
| [Flow Parameter Naming](Flow Parameter Naming.md) | Identifies where naming standards for Flow Parameters and Parameter Sets are breached. |
| [Flow Parameter Not In A Parameter Set](Flow Parameter Not In A Parameter Set.md) | Identify Flow Parameters that are not in a Parameter Set. |
| [Flow Using Random Function](Flow Using Random Function.md) | Identify Transformers (or other stages) using Random functions which produce non-deterministic output. |
| [Flow Using Transformer Surrogate Key](Flow Using Transformer Surrogate Key.md) | Identifies flow designs that use NextSurrogateKey() in a Transformer. |
| [Hardcoded DB Credentials](Hardcoded DB Credentials.md) | Ensures that all Database Connectors must use variables for location and credentials |
| [Hardcoded File Paths](Hardcoded File Paths.md) | Ensures that all File Stages must use variables for determining paths |
| [Join Partition vs Join Key](Join Partition vs Join Key.md) | Reports Join stages where the join key does not match the partitioning of the input links. |
| [Link Sort](Link Sort.md) | Identifies link sorts. |
| [Log Column Values](Log Column Values.md) | Identify Stages configured to Log column values on first row error |
| [Lookup Failure](Lookup Failure.md) | Identifies Lookup Stages with Lookup set to Fail. |
| [One Dataflow](One Dataflow.md) | Verifies that there is only one data flow in a DataStage Flow. |
| [Oracle Connector Not Using Partitioned Read](Oracle Connector Not Using Partitioned Read.md) | Identify Oracle Stages not configured to use partitioned reads. |
| [Password Parameter Type Not Encrypted](Password Parameter Type Not Encrypted.md) | Flow parameters with names that suggest they will be used for supplying passwords should be set to use the type "Encrypted". |
| [Prohibited Stages](Prohibited Stages.md) | Verifies that a job does not contain one or more prohibited stages. |
| [Range Lookup Incorrectly Configured](Range Lookup Incorrectly Configured.md) | Checks that range lookups are correctly configured. |
| [Redundant Sort](Redundant Sort.md) | Identifies unnecessary sort opertions witihn Job designs. |
| [SQL in DB Connectors](SQL in DB Connectors.md) | Ensures that all DB Connectors not using SQL Statement to filter source data |
| [Schema Files](Schema Files.md) | Detect use of Schema Files. |
| [Select All in Custom SQL](Select All in Custom SQL.md) | Identifies where "select *" syntax has been used in custom SQL code in database Connectors. |
| [Sequential File Read Using Same Partitioning](Sequential File Read Using Same Partitioning.md) | Avoid reading from Sequential Files using the 'Same' partitioning method. |
| [Sequential File With Reject Mode Not Set To Fail](Sequential File With Reject Mode Not Set To Fail.md) | Identifies Sequential Files with a Reject Mode not set to fail |
| [Sort Post Join Stage](Sort Post Join Stage.md) | Identifies potentially redundant sorting (a sort stage or link sort) situated immediately after a Join stage |
| [Stage Naming](Stage Naming.md) | Stage naming standards for DataStage flows and watson pipelines. |
| [System Time Dependency](System Time Dependency.md) | Identifies the use of system time functions in the job |
| [Too Many Stages](Too Many Stages.md) | Identify whether a flow has too many stages. |
| [Transformer Uses Abort After Rows](Transformer Uses Abort After Rows.md) | Detect an 'Abort after rows' greater than 0 setting in a Parallel Transformer. |
| [Transformer With Unreferenced Stage Variable](Transformer With Unreferenced Stage Variable.md) | Identifies Transformer Stage with an unreferenced Stage Variable (including Loop Variables). |
| [Unencrypted DB Passwords](Unencrypted DB Passwords.md) | Ensures that all Connectors must use encrypted Passwords |
| [Unique Sort](Unique Sort.md) | Identifies unique sorts. |

Page generated on Thu 14 Dec 2023 21:40:19 AEDT
&copy; 2023 Data Migrators Pty Ltd
[www.datamigrators.com](http://www.datamigrators.com)

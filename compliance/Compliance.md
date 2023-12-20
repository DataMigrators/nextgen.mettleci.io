---
layout: default
title: Compliance
has_children: true
has_toc: false
permalink: /compliance
---

# MettleCI Cloud Pak Compliance Rule Reference

This page lists the example DataStage compliance rules suplied with MettleCI for IBM Cloud Pak for Data.

| Rule name | Description |
|-----------|-------------|
| [Adjacent Transformers](compliance/Adjacent Transformers) | Identifies flow designs with adjacent Transformer stages. |
| [Aggregator Stage Not Preceded by Check Sort Stage](compliance/Aggregator Stage Not Preceded by Check Sort Stage) | Aggregator Stage will only return the correct result if the keys are pre-sorted |
| [Audit Annotation](compliance/Audit Annotation) | Identifies where sensitive information may potentially be present in DataStage Job and Sequence Annotations. |
| [Connection Contains Parameter References](compliance/Connection Contains Parameter References) | Identifies Connections created by the migration from legacy Datastage to NextGen that contain references to |
| [Connection Not Using Secrets Vault](compliance/Connection Not Using Secrets Vault) | Identifies Connections that do not store their credentials to use secrets in a vault. |
| [Database Query From File](compliance/Database Query From File) | Ensures if Database Connectors and Stages reads SQL statement from file. |
| [Database Row Limit](compliance/Database Row Limit) | Identifies Connectors Stages with a configured Database Row Limit. |
| [DataSet Not Using Same Partition](compliance/DataSet Not Using Same Partition) | Identifies Data Sets not using the 'Same' partitioning method |
| [Date Format in Annotation](compliance/Date Format in Annotation) | Identify whether the a Flow annotation contains instances of particular arbitrary text.  This example rule looks for dates. |
| [DB2 with No Non Recovery Load](compliance/DB2 with No Non Recovery Load) | Identify Db2 Stages using bulk load with Non Recovery Load set to 'No'. |
| [DB Connector Not Auto Generate SQL](compliance/DB Connector Not Auto Generate SQL) | Identifies Connections that do not use Auto Generate SQL. |
| [DB Tables Referenced Are Fully Qualified](compliance/DB Tables Referenced Are Fully Qualified) | Identifies where database table references are not fully-qualified. |
| [Debug Row Limit](compliance/Debug Row Limit) | Identifies row limits in debug stages (Peek, Sample, Tail) |
| [Default Naming](compliance/Default Naming) | Default Stage Names for Parallel Jobs, Server Jobs, and Job Sequences |
| [Duplicate File References](compliance/Duplicate File References) | Verifies that a sequential file is... |
| [Duplicate Stage Names](compliance/Duplicate Stage Names) | Detect duplicate Stage names in a job. |
| [File Reference Missing Required Parameter](compliance/File Reference Missing Required Parameter) | Ensures that all File Stages must use variables for determining paths |
| [File Row Limit](compliance/File Row Limit) | Identifies row limits in file-based stages (Sequential File, Complex Flat File). |
| [Flow Naming](compliance/Flow Naming) | Checks the Flow name against a list of known prohibited name patterns. |
| [Flow Parameter Missing Default Value](compliance/Flow Parameter Missing Default Value) | Identify flow parameters within a default value. |
| [Flow Parameter Naming](compliance/Flow Parameter Naming) | Identifies where naming standards for Flow Parameters and Parameter Sets are breached. |
| [Flow Parameter Not In A Parameter Set](compliance/Flow Parameter Not In A Parameter Set) | Identify Flow Parameters that are not in a Parameter Set. |
| [Flow Using Random Function](compliance/Flow Using Random Function) | Identify Transformers (or other stages) using Random functions which produce non-deterministic output. |
| [Flow Using Transformer Surrogate Key](compliance/Flow Using Transformer Surrogate Key) | Identifies flow designs that use NextSurrogateKey() in a Transformer. |
| [Hardcoded DB Credentials](compliance/Hardcoded DB Credentials) | Ensures that all Database Connectors must use variables for location and credentials |
| [Hardcoded File Paths](compliance/Hardcoded File Paths) | Ensures that all File Stages must use variables for determining paths |
| [Join Partition vs Join Key](compliance/Join Partition vs Join Key) | Reports Join stages where the join key does not match the partitioning of the input links. |
| [Link Sort](compliance/Link Sort) | Identifies link sorts. |
| [Log Column Values](compliance/Log Column Values) | Identify Stages configured to Log column values on first row error |
| [Lookup Failure](compliance/Lookup Failure) | Identifies Lookup Stages with Lookup set to Fail. |
| [One Dataflow](compliance/One Dataflow) | Verifies that there is only one data flow in a DataStage Flow. |
| [Oracle Connector Not Using Partitioned Read](compliance/Oracle Connector Not Using Partitioned Read) | Identify Oracle Stages not configured to use partitioned reads. |
| [Password Parameter Type Not Encrypted](compliance/Password Parameter Type Not Encrypted) | Flow parameters with names that suggest they will be used for supplying passwords should be set to use the type "Encrypted". |
| [Prohibited Stages](compliance/Prohibited Stages) | Verifies that a job does not contain one or more prohibited stages. |
| [Range Lookup Incorrectly Configured](compliance/Range Lookup Incorrectly Configured) | Checks that range lookups are correctly configured. |
| [Redundant Sort](compliance/Redundant Sort) | Identifies unnecessary sort opertions witihn Job designs. |
| [Schema Files](compliance/Schema Files) | Detect use of Schema Files. |
| [Select All in Custom SQL](compliance/Select All in Custom SQL) | Identifies where "select *" syntax has been used in custom SQL code in database Connectors. |
| [Sequential File Read Using Same Partitioning](compliance/Sequential File Read Using Same Partitioning) | Avoid reading from Sequential Files using the 'Same' partitioning method. |
| [Sequential File With Reject Mode Not Set To Fail](compliance/Sequential File With Reject Mode Not Set To Fail) | Identifies Sequential Files with a Reject Mode not set to fail |
| [Sort Post Join Stage](compliance/Sort Post Join Stage) | Identifies potentially redundant sorting (a sort stage or link sort) situated immediately after a Join stage |
| [SQL in DB Connectors](compliance/SQL in DB Connectors) | Identifies DB Connectors which use an SQL to filter source data |
| [Stage Naming](compliance/Stage Naming) | Stage naming standards for DataStage flows and watson pipelines. |
| [System Time Dependency](compliance/System Time Dependency) | Identifies the use of system time functions in the job |
| [Too Many Stages](compliance/Too Many Stages) | Identify whether a flow has too many stages. |
| [Transformer Uses Abort After Rows](compliance/Transformer Uses Abort After Rows) | Detect an 'Abort after rows' greater than 0 setting in a Parallel Transformer. |
| [Transformer With Unreferenced Stage Variable](compliance/Transformer With Unreferenced Stage Variable) | Identifies Transformer Stage with an unreferenced Stage Variable (including Loop Variables). |
| [Unencrypted DB Passwords](compliance/Unencrypted DB Passwords) | Identifies connector stages which do not use encrypted passwords |
| [Unique Sort](compliance/Unique Sort) | Identifies unique sorts. |

Page generated by on Wed Dec 20 12:51:21 AEDT 2023

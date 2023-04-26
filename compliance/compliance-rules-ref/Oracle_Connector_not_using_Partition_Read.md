---
layout: page
title: Oracle_Connector_not_using_Partition_Read
parent: .
---

# Oracle Connector not using Partition Read

|                  |                                                                |
|------------------|----------------------------------------------------------------|
| **Rule name**    | Oracle Connector Not Using Partition Read                      |
| **Parallel Job** | Yes                                                            |
| **Server Job**   | \-                                                             |
| **Job Sequence** | \-                                                             |
| **Description**  | Identify Oracle Stages not configured to use partitioned reads |

# Description

An Oracle Connector Stage running in a Parallel Job and configured to
read data in parallel mode, each node of the connector reads a distinct
subset of data from the source table. It achieves this by running a
slightly modified SELECT statement on each node. The combined set of
rows from all of the queries is the same set of rows that would be
returned if the unmodified user-defined SELECT statement were run once
on one node. This approach requires that you <a
href="https://www.ibm.com/docs/en/iis/11.7?topic=database-reading-partitioned-data"
rel="nofollow">configure your Oracle Connector Stage</a> appropriately,
and can deliver significant performance improvements over using a
single-node read operation.

# Actions

Ensure that you <a
href="https://www.ibm.com/docs/en/iis/11.7?topic=database-reading-partitioned-data"
rel="nofollow">configure your Oracle Connector Stage</a> appropriately.

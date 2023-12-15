---
layout: page
title: "Oracle Connector Not Using Partitioned Read"
parent: Compliance
nav_order: 2
---

# Oracle Connector Not Using Partition Read

## Summary

Identify Oracle Stages not configured to use partitioned reads.

## Description

When an Oracle Connector Stage running in a Parallel Flow is configured to read data in parallel mode each node of the connector operator reads a distinct subset of data from the source table.  It achieves this by running a subtly modified `SELECT` statement on each node. The combined set of rows from all of the queries is the same set of rows that would be returned if the unmodified user-defined `SELECT` statement were run once on one node.  This approach requires that you configure your Oracle Connector Stage appropriately, and can deliver significant performance improvements over using a single-node read operation. 

## Actions

Ensure that you [configure your Oracle Connector Stage](https://www.ibm.com/docs/en/iis/11.7?topic=database-reading-partitioned-data) appropriately.


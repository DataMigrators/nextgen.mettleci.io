---
layout: page
title: "DB Connector Not Auto Generate SQL"
parent: Compliance
nav_order: 2
---

# DB Connector Not Auto Generate SQL

## Summary

Identifies Connections that do not use Auto Generate SQL.

## Description

In InfoSphere Information Governance Catalog, the schema and database table name of the imported database 
must be the same as the schema and database table name in the stage. 

You can generate default SQL statements to read from and write to data sources. 
Alternatively, you can specify SQL statements manually that read from and write to data sources.     
SQL that you specify might contain certain DBMS-vendor-specific constructs that cannot be parsed correctly in job lineage analysis. 

As a result, the relationships between stages and data sources and between stages and other stages might be incorrect.

## Actions

Update the connector to use Auto Generate SQL.

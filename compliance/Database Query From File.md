---
layout: page
title: "Database Query From File"
parent: Compliance
---

# Database Query From File

## Summary

Ensures if Database Connectors and Stages reads SQL statement from file.

## Description

Developers occasionally wants to keep the SQL statements flexible, and use external file for SQL statements.
However, SQL statements from external files do not go to the metadata repository where they can be used for 
job flow analysis. These SQL statements are also not included in operational metadata XML files.

This can make the job harder to maintain as it contains external objects, and failure when deploying to a different project of server.

It is recommended for developer to use parameters instead of External file if they wish to maintain the flexibility of SQL statements


## Actions

Update the connector to not Reading Query From File.

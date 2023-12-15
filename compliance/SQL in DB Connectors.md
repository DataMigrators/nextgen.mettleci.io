---
layout: page
title: "SQL in DB Connectors"
parent: Compliance
nav_order: 2
---

# File Reference Missing Required Parameter

## Summary

Ensures that all DB Connectors not using SQL Statement to filter source data

## Description
Check for SQL usage on DB connectors. Developers should avoid using SQL to filter data and instead utilize Datastage's features

This currently only allows generated SQL where there are no other clauses specified in connector with that option. Any use-defined SQL, generated SQL with additional clauses or query file inputs will fail. 

## Actions

Use Generate SQL from Connector to source data, and dataStage stages to filter data.

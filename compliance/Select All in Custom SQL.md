---
layout: page
title: "Select All in Custom SQL"
parent: Compliance
nav_order: 2
---

# "Select *" in Custom SQL

## Summary
	
Identifies where "select *" syntax has been used in custom SQL code in database Connectors.

## Description

Using Select * in custom SQL code may be indicative of:
	- SQL code that has been directly lifted from a SQL editor and inserted in to DataStage without further analysis or consideration
	- code that ignores future changes to the source and possibly produces misleading errors in the DataStage logs

## Actions

Modify your Connector Stages' SELECT statements to use explicit column names. 
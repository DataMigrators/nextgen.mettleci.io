---
layout: page
title: "DB Tables Referenced Are Fully Qualified"
parent: Compliance
nav_order: 2
---

# DB Tables Reference are Fully Qualified

## Summary

Identifies where database table references are not fully-qualified.

## Description

Database table references can sometimes cause problems when migrating from Development to downstream QA and Production environments as they will likely be communicating with different databases to those used in Development. Those databases may well have different configurations to those against which the Job was developed, and there may arise some confusion about which schemas or other database objects are being referenced by the Job.

## Actions

Ensure all database object references used by your Job are fully qualified. For example, `{schema}.{tablename}`

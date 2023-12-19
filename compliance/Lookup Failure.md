---
layout: page
title: "Lookup Failure"
parent: Compliance
---

# Lookup Failure

## Summary

Identifies Lookup Stages with Lookup set to Fail.

## Description

Lookup stages have a ‘Condition Not Met’ setting which describes what happens when a key lookup fails.  Options are:

**Continue** - The fields from that link are set to NULL if the field is nullable, or to a default value if not, and processing continues

**Drop** - Drops the row and continues with the next lookup

**Fail** - Causes the job to issue a fatal error and stop

**Reject** - Sends the row to the reject link

By default Lookup stages are configured to Fail should a key lookup fail. This unexpected job abort is, in most cases, not the behaviour the developer intended. These lookup fails should be handled gracefully in the ETL job.

## Actions

Reconfigure your Lookup stage so that reference links are not set to abort the job should a key lookup fail.

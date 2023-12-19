---
layout: page
title: "File Row Limit"
parent: Compliance
---

# File Row Limit

## Summary

Identifies row limits in file-based stages (Sequential File, Complex Flat File).

## Description

Row limits set on the file stages are options developers might use during development and unit testing to allow faster development. Leaving these options set may have unintended consequences should the flow be deployed into test and production environments.

## Actions

Remove the row limit on identified Stages.

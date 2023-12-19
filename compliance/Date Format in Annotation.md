---
layout: page
title: "Date Format in Annotation"
parent: Compliance
---

# Data Format in Annotation

## Summary

Identify whether the a Flow annotation contains instances of particular arbitrary text.  This example rule looks for dates.

## Description

Identify whether the a ‘Job Description’ annotation contains instances of particular arbitrary text. You can modify this rule to get it to seek out any text your team wants to prevent passing compliance.  This example rule looks for text matching the following date formats:

| Format                                         | Description                                      |
|------------------------------------------------|--------------------------------------------------|
| `YYYY-MM-DD`, `YYYY/MM/DD`, `YYYY MM DD`       | YYYY-MM-DD format with `/` or `-` as a delimiter |
| `YYYY-MMM-DD`, `YYYY/MMM/DD`, `YYYY MMM DD`    | Month format can be MM, MMM, MMMM, or MON        |
| `YYYY-MMMM-DD`, `YYYY/MMMM/DD`, `YYYY MMMM DD` | MMM and MMMM are Excel Syntax                    |
| `DD-MM-YYYY`                                   | Similar to YYYY-MM-DD                            |
| `MM-DD-YYYY`                                   | Similar to YYYY-MM-DD (common US date format)    |

## Actions

Remove or alter the text that references a date.



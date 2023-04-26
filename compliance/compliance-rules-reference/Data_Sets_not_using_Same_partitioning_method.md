---
layout: page
title: Data_Sets_not_using_Same_partitioning_method
parent: .
---

# Data Sets not using 'Same' partitioning method

|                  |                                                               |
|------------------|---------------------------------------------------------------|
| **Rule name**    | Data Sets not using 'Same' partitioning method                |
| **Parallel Job** | Yes                                                           |
| **Server Job**   | \-                                                            |
| **Job Sequence** | \-                                                            |
| **Description**  | Identifies Data Sets not using the 'Same' partitioning method |

# Description

This rule identifies Parallel Job Data Sets which do not use the 'Same'
partitioning method.

This is an IBM development tip documented here:
<a href="https://www.ibm.com/docs/en/iis/11.7?topic=tips-sorting-data"
rel="nofollow">Sorting data - IBM Documentation</a>

# Actions

When reading from Data Sets maintain your sort order by using ‘Same’
partitioning method.

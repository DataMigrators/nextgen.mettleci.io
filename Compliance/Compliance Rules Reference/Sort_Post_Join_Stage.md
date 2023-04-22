---
layout: page
title: Sort_Post_Join_Stage
parent: .
---

# Sort Post Join Stage

|                    |                                                                                                              |
|--------------------|--------------------------------------------------------------------------------------------------------------|
| **Rule name**      | Sort Post Join Stage                                                                                         |
| **Parallel Job**   | Yes                                                                                                          |
| **Server Job**     | Yes                                                                                                          |
| **Job Sequence**   | \-                                                                                                           |
| **Workbench role** | WARN                                                                                                         |
| **DevOps role**    | WARN                                                                                                         |
| **Upgrade role**   | WARN                                                                                                         |
| **Description**    | Identifies potentially redundant sorting (a sort stage or link sort) situated immediately after a Join stage |

# Description

Sorting is resource intensive, and when used excessively can impact
performance. This rule identifies Jobs that sort the output of a Join
stage, which is a potentially redundant operation.

# Actions

Review the Job design and remove the Sort if redundant.

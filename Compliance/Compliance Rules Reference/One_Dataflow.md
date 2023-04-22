---
layout: page
title: One_Dataflow
parent: .
---

# One Dataflow

|                  |                                                              |
|------------------|--------------------------------------------------------------|
| **Rule name**    | One Dataflow                                                 |
| **Parallel Job** | Yes                                                          |
| **Server Job**   | Yes                                                          |
| **Job Sequence** | \-                                                           |
| **Description**  | Verifies that there is only one data flow in a DataStage job |

# Description

A DataStage job has no restrictions on the number of independent data
flows that can be created. Ideally a DataStage job should be created for
each data flow to allow the calling application to manage the execution
order.

# Actions

Split your Job so that each dataflow is defined within its own dedicated
Job.

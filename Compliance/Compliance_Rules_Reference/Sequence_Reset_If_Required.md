---
layout: page
title: Sequence_Reset_If_Required
parent: .
---

# Sequence Reset If Required

|                  |                                                                                     |
|------------------|-------------------------------------------------------------------------------------|
| **Rule name**    | Sequence Reset If Required                                                          |
| **Parallel Job** | \-                                                                                  |
| **Server Job**   | \-                                                                                  |
| **Job Sequence** | Yes                                                                                 |
| **Description**  | Identifies where a Job Activity Execution Action is not Reset if required, then run |

# Description

In the event of a Job failure the a Job Sequence’s Job Activity
Execution Action **Reset if required, then run** will reset its
associated Job before attempting re-execution. Without this you will
need to manually reset the Job.

# Actions

Set your Job Activity’s Execution Action to use **Reset if required,
then run**.

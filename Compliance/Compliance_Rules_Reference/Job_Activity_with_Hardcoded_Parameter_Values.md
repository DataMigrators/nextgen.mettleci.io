---
layout: page
title: Job_Activity_with_Hardcoded_Parameter_Values
parent: .
---

# Job Activity with Hardcoded Parameter Values

|                  |                                              |
|------------------|----------------------------------------------|
| **Rule name**    | Job Activity with Hardcoded Parameter Values |
| **Parallel Job** | \-                                           |
| **Server Job**   | \-                                           |
| **Job Sequence** | Yes                                          |
| **Description**  | Sequence Job with Hardcoded Parameter Values |

# Description

In Sequence jobs, Job Activity stages calling jobs with parameters
should have those parameters populated from the sequence job, to ensure
the sequences and individual jobs operate consistently. These hardcoded
values may be explicit values entered into the Job Activity stage, or
the Default Values gathered from the underlying job.

# Actions

Replace the hardcoded values with a reference to a Sequence Job
parameter.

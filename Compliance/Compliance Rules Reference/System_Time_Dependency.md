---
layout: page
title: System_Time_Dependency
parent: .
---

# System Time Dependency

|                  |                                              |
|------------------|----------------------------------------------|
| **Rule name**    | System Time Dependency                       |
| **Parallel Job** | Yes                                          |
| **Server Job**   | \-                                           |
| **Job Sequence** | \-                                           |
| **Description**  | Identifies the use of system time in the job |

# Description

Jobs with date logic that reads from the system time make it difficult
to perform repeatable/automated testing. Instead of using system date
functions, it is recommended that the current date be passed in as a job
parameter or derived from one of the `DSJobStart*` macros. During unit
testing, the job parameter or `DSJobStart*` macro can be set to a fixed
value. The actual job results can then be compared with the expected
results without needing to account for differences due to system time.

# Actions

Replace the reference to the system time or date with a Job Parameter of
the appropriate type.

---
layout: page
title: Too_Many_Stages
parent: .
---

# Too Many Stages

|                  |                                              |
|------------------|----------------------------------------------|
| **Rule name**    | Too Many Stages                              |
| **Parallel Job** | Yes                                          |
| **Server Job**   | Yes                                          |
| **Job Sequence** | \-                                           |
| **Description**  | Identifies whether a Job has too many Stages |

# Description

A job that contains too many stages becomes hard to maintain. Not only
is it difficult to follow the logic but even physically moving around it
and finding specific logic is hard.

This rule detects when a job or local container exceeds a globally
configurable stage limit. The default "stageLimit" parameter is set to
25 but can be easily adjusted as required.

# Actions

Split your Job into multiple Jobs, or remove unnecessary Stages.

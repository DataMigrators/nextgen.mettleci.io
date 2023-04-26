---
layout: page
title: Job_Sequence_Is_Restartable
parent: .
---

# Job Sequence Is Restartable

|                  |                                                   |
|------------------|---------------------------------------------------|
| **Rule name**    | Job Sequence Is Restartable                       |
| **Parallel Job** | \-                                                |
| **Server Job**   | \-                                                |
| **Job Sequence** | Yes                                               |
| **Description**  | Identifies Job Sequences that are not restartable |

# Description

Sequence jobs can be configured to record checkpoint information using
the **Add checkpoints so sequence is restartable** option. This enables
you to restart a failed sequence from the point at which it failed. You
can enable or disable checkpoint recording at a project-wide level, or
for individual sequence jobs. This compliance rule verifies that this
setting has been set for a specified job sequence.

# Actions

Enable your Sequence’s **Add checkpoints so sequence is restartable**
property.

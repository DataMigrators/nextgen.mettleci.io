---
layout: page
title: Transformer_Uses_Abort_after_rows_
parent: .
---

# Transformer Uses 'Abort after rows'

|                  |                                                                                |
|------------------|--------------------------------------------------------------------------------|
| **Rule name**    | Parallel Transformer uses 'Abort after rows'                                   |
| **Parallel Job** | Yes                                                                            |
| **Server Job**   | \-                                                                             |
| **Job Sequence** | \-                                                                             |
| **Description**  | Detect an 'Abort after rows' greater than 0 setting in a Parallel Transformer. |

# Description

This rule detects Parallel Transformer with an 'Abort after rows'
setting greater than 0. This *could* be considered bad practice in some
organisations as rows unexpectedly appearing on a given link could be
more gracefully handled by introducing an error-handling process which
does not cause a job to abort.

# Actions

Set the 'Abort after rows' value to 0 and provide downstream logic to
report and handle the erroneous rows.
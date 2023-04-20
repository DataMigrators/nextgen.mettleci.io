---
layout: page
title: Link_Sort
parent: .
---

# Link Sort

|                  |                       |
|------------------|-----------------------|
| **Rule name**    | Link Sort             |
| **Parallel Job** | Yes                   |
| **Server Job**   | \-                    |
| **Job Sequence** | \-                    |
| **Description**  | Identifies link sorts |

# Description

Developers where possible should utilise the sort stage rather than
utilising the link sort facility. The sort stage allows more options for
controlling the behaviour of the sort operation, appears in the job
monitor as well as better communicating visually to other developers the
main functions of the ETL job.

This rule identifies jobs that utilise implicit sorts on a link which
may miss some opportunities for performance optimisation, and may reduce
the easy maintainability of your jobs. Both link Sorts and explicit
Sorts generate the same underlying orchestrate operators, however the
explicit Sort stage offers the following options which are ot available
on a link Sort:

-   Sort Key Mode

-   Create Cluster Key Change Column

-   Create Key Change Column

-   Output Statistics

-   Sort Utility

-   Restrict Memory Usage

Additionally, the sort stage appears in the job monitor, so progress can
be tracked at any point, rather than the job monitor 'going dark' when
using a link sort.

# Actions

Replace the link sort with an explicit sort stage.

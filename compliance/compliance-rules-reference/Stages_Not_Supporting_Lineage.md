---
layout: page
title: Stages_Not_Supporting_Lineage
parent: .
---

# Stages Not Supporting Lineage

|                  |                                                                                           |
|------------------|-------------------------------------------------------------------------------------------|
| **Rule name**    | Stages Not Supporting Lineage                                                             |
| **Parallel Job** | Yes                                                                                       |
| **Server Job**   | Yes                                                                                       |
| **Job Sequence** | \-                                                                                        |
| **Description**  | This rule detects the use of stages in Parallel Jobs that don't support automatic lineage |

# Description

If a stage does not support lineage, IBM Information Governance Catalog
(IGC) cannot determine a complete set of dependencies by which MettleCI
builds its dependency tree.

# Actions

None.

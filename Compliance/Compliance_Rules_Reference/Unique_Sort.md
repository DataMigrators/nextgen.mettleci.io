---
layout: page
title: Unique_Sort
parent: .
---

# Unique Sort

|                  |                         |
|------------------|-------------------------|
| **Rule name**    | Unique Sort             |
| **Parallel Job** | Yes                     |
| **Server Job**   | Yes                     |
| **Job Sequence** | \-                      |
| **Description**  | Identifies unique sorts |

# Description

Unique sorts are not visually represented on the DataStage canvas.
Ideally the developer should use the Remove Duplicates stage so that
this can be visually communicated with other developers. This rule will
identify sort stages which have the **Allow Duplicates** property set to
**false**.

# Actions

Replace unique sorts with a Remove Duplicates stage.

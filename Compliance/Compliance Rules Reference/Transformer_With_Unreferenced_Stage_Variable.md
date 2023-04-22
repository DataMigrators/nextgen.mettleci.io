---
layout: page
title: Transformer_With_Unreferenced_Stage_Variable
parent: .
---

# Transformer With Unreferenced Stage Variable

|                  |                                                                                             |
|------------------|---------------------------------------------------------------------------------------------|
| **Rule name**    | Transformer With Unreferenced Stage Variable                                                |
| **Parallel Job** | Yes                                                                                         |
| **Server Job**   | Yes                                                                                         |
| **Job Sequence** | \-                                                                                          |
| **Description**  | Identifies Transformer Stage with an unreferenced Stage Variable (including Loop Variables) |

# Description

A Transformer can be resource intensive, and having unreferenced
Stage/Loop variable…

-   Can be an unnecessary waste of resources

-   Can cause confusion to Job maintainers

-   May present a security vulnerability

This rule identifies forgotten/unreferenced Stage/Loop variables.

# Actions

Remove the unreferenced Stage/Loop variable.

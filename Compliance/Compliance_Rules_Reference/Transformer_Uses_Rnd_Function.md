---
layout: page
title: Transformer_Uses_Rnd_Function
parent: .
---

# Transformer Uses 'Rnd()' Function

|                  |                                                                |
|------------------|----------------------------------------------------------------|
| **Rule name**    | Parallel Transformer uses Rnd() function                       |
| **Parallel Job** | Yes                                                            |
| **Server Job**   | \-                                                             |
| **Job Sequence** | \-                                                             |
| **Description**  | Identify the use of a Rnd() function in Parallel Transformers. |

# Description

This rule identifies the use of the `Rnd()` function in Parallel
Transformers. This function produces a different value for every Job
invocation, making the Job
<a href="https://en.wikipedia.org/wiki/Nondeterministic_algorithm"
rel="nofollow">non-deterministic</a>. This prevents the creation of a
Unit Test which includes any column whose output is affected by the
`Rnd()` function call.

# Actions

Replace the `Rnd()` call with a Job Parameter which is supplied, in
production scenarios, with a random value at runtime. This parameter can
then be supplied with a fixed value by a MettleCI Unit Test, resulting
in a repeatable (and hence testable) job output.

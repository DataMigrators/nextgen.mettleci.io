---
layout: page
title: Consider_Surrogate_Key_Generator_over_Transformer_Surrogate_Key
parent: .
---

# Consider Surrogate Key Generator over Transformer Surrogate Key

|                  |                                                                                                                  |
|------------------|------------------------------------------------------------------------------------------------------------------|
| **Rule name**    | Consider Surrogate Key Generator over Transformer Surrogate Key                                                  |
| **Parallel Job** | Yes                                                                                                              |
| **Server Job**   | \-                                                                                                               |
| **Job Sequence** | \-                                                                                                               |
| **Description**  | Recommends considering replacing a Transformer Stage using a Surrogate Key with a Surrogate Key Generator stage. |

# Description

This rule identifies <a
href="https://www.ibm.com/docs/en/iis/11.7?topic=page-transformer-stage-surrogate-key-tab"
rel="nofollow">Transformer Stages configured with Surrogate Key
functionality</a> (using a database/file to manage the surrogate key)
and suggests Developers consider whether the Job could be made more
maintainable using a Surrogate Key Generator stage instead.

# Actions

Replace the Transformer Stage's Surrogate Key functionality with a
Surrogate Key Generator stage.

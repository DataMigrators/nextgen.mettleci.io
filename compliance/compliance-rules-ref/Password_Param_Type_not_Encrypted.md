---
layout: page
title: Password_Param_Type_not_Encrypted
parent: .
---

# Password Param Type not Encrypted

|                  |                                                                |
|------------------|----------------------------------------------------------------|
| **Rule name**    | Password Param Type not Encrypted                              |
| **Parallel Job** | Yes                                                            |
| **Server Job**   | Yes                                                            |
| **Job Sequence** | \-                                                             |
| **Description**  | Identify unencrypted Job parameters used for storing passwords |

# Description

Job parameters with names that suggest they will be used for supplying
passwords should be set to use the type **Encrypted**. If they are not
encrypted then their plain text contents could present a security risk.

# Actions

Set Job parameters used for supplying passwords to use the type
**Encrypted**.

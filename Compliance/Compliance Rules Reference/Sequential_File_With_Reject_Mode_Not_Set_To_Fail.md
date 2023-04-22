---
layout: page
title: Sequential_File_With_Reject_Mode_Not_Set_To_Fail
parent: .
---

# Sequential File With Reject Mode Not Set To Fail

|                    |                                                                |
|--------------------|----------------------------------------------------------------|
| **Rule name**      | Sequential File With Reject Mode Not Set To Fail               |
| **Parallel Job**   | Yes                                                            |
| **Server Job**     | \-                                                             |
| **Job Sequence**   | \-                                                             |
| **Workbench role** | FAIL                                                           |
| **DevOps role**    | FAIL                                                           |
| **Upgrade role**   | FAIL                                                           |
| **Description**    | Identifies Sequential Files with a Reject Mode not set to fail |

# Description

Some scenarios may require you to identify where an input Sequential
File contains errors and cease processing. In this case you would set
your Sequential File’s **Reject Mode** to **fail**. This rule assist
this process by identifying when the Reject Mode is set to **Continue**
or **Output**.

# Actions

Set your Sequential File’s **Reject Mode** appropriate to your needs.

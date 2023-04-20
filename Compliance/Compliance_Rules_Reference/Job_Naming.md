---
layout: page
title: Job_Naming
parent: .
---

# Job Naming

|                  |                                                                            |
|------------------|----------------------------------------------------------------------------|
| **Rule name**    | Job Naming                                                                 |
| **Parallel Job** | Yes                                                                        |
| **Server Job**   | Yes                                                                        |
| **Job Sequence** | Yes                                                                        |
| **Description**  | Checks the job name against a blocklist of known bad names (e.g. CopyOf\*) |

# Description

As developers we will occasionally work on a copy or WIP (Work In
Progress) job but forget to rename it before checkin. This simple
compliance test is designed to make these mistakes visible at check-in
time.

See <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/706215949"
rel="nofollow">Data Migrators' asset naming standards</a> for the
default list of naming signatures on the <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/706215949/Compliance+Default+Asset+Naming+Standards#Blocklist"
rel="nofollow">blocklist</a>.

# Actions

Rename the Job to align with your coding standards and remove ambiguity.

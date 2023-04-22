---
layout: page
title: Stage_Naming
parent: .
---

# Stage Naming

|                  |                                                                       |
|------------------|-----------------------------------------------------------------------|
| **Rule name**    | Stage Naming                                                          |
| **Parallel Job** | Yes                                                                   |
| **Server Job**   | Yes                                                                   |
| **Job Sequence** | Yes                                                                   |
| **Description**  | Stage Naming Standards for Parallel and Server Jobs and Job Sequences |

# Description

Verifies that job stage names match the Data Migrators naming standards.
All naming standards are based on <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/706215949"
rel="nofollow">these example asset naming standards</a> and are expected
to be customised to customer requirements.

Our naming standards are designed to reduce the amount of effort
required for developers to understand what a job is doing without
needing to inspect each stage on the job canvas and to quickly identify
job stages from text based messages such as director errors and
compliance rule failures.

In most cases, this is achieved by having a prefix that reflects the
stage type. However, for stages such as joins and funnels, the stage
names provide additional information which cannot be determined without
inspecting the stage in question (ie. inner/left/right join).

Enforced naming standards of this nature also allows future IP to easily
determine stage types based on the name without needing to refer to IGC
or XMETA. Additionally, these naming standards help prevent trivial
feedback from external vendors during data migration/warehouse "audits".

# Actions

Ensure your Job Stages or Sequence Activities are named according to
your naming standards.

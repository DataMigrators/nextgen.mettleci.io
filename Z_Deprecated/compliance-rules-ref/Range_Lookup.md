---
layout: page
title: Range_Lookup
parent: .
---

# Range Lookup

|                  |                                                    |
|------------------|----------------------------------------------------|
| **Rule name**    | Range Lookup                                       |
| **Parallel Job** | Yes                                                |
| **Server Job**   | \-                                                 |
| **Job Sequence** | \-                                                 |
| **Description**  | Checks that range lookups are correctly configured |

# Description

When setting up a
<a href="https://www.ibm.com/docs/en/iis/11.7?topic=stage-range-lookups"
rel="nofollow">range lookup</a>, DataStage will build the lookup table
based on the primary key fields but not the range fields. If the range
option is enabled on the reference link, this will result in duplicates
being ignored and the range lookup won't work as expected.

This rule will check that range lookups have been configured to allow
duplicates on the reference link and prevent unexpected results due to
an incorrectly configured stage.

# Actions

Ensure range lookups are configured to allow duplicates on the reference
link.

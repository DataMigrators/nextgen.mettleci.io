---
layout: page
title: DB_tables_reference_are_fully_qualified
parent: .
---

# DB tables reference are fully qualified

|                  |                                                                    |
|------------------|--------------------------------------------------------------------|
| **Rule name**    | DB tables reference are fully qualified                            |
| **Parallel Job** | Yes                                                                |
| **Server Job**   | Yes                                                                |
| **Job Sequence** | \-                                                                 |
| **Description**  | Identifies where database table references are not fully-qualified |

# Description

Database table references can sometimes cause problems when migrating
from Development to downstream QA and Production environments as they
will likely be communicating with different databases to those used in
Development. Those databases may well have different configurations to
those against which the Job was developed, and there may arise some
confusion about which schemas or other database objects are being
referenced by the Job.

# Actions

Ensure all database object references used by your Job are fully
qualified (e.g. `{schema}.{tablename}`)

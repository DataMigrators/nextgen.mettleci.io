---
layout: page
title: Join_Partition_vs_Join_Key
parent: .
---

# Join Partition vs Join Key

|                  |                                                                               |
|------------------|-------------------------------------------------------------------------------|
| **Rule name**    | Join Partition vs Join Key                                                    |
| **Parallel Job** | Yes                                                                           |
| **Server Job**   | \-                                                                            |
| **Job Sequence** | \-                                                                            |
| **Description**  | Identifies Join stages where the join key does not match the partitioning key |

# Description

Parallel Join stages require that their input data are partitioned using
the same key(s) as those being used for the Join condition.

If this is not the case then data rows which fulfil the Join condition
may not be joined as they will be propagated along different partitions.

# Actions

Ensure the Join key and partition keys are aligned.

---
layout: page
title: Sequential_File_Read_Using_Same_Partitioning
parent: .
---

# Sequential File Read Using Same Partitioning

|                  |                                                                        |
|------------------|------------------------------------------------------------------------|
| **Rule name**    | Sequential File Read Using Same Partition                              |
| **Parallel Job** | Yes                                                                    |
| **Server Job**   | \-                                                                     |
| **Job Sequence** | \-                                                                     |
| **Description**  | Avoid Reading from Sequential Files Using the Same Partitioning Method |

# Description

Avoid reading from sequential files using the Same partitioning method.
Unless you have specified more than one source file this will result in
the entire file being read into a single partition, making the entire
downstream flow run sequentially unless you explicitly re-partition.

# Actions

Configure your Sequential File Stage to use a partitioning method other
than Same.

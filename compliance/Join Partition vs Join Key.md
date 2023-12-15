---
layout: page
title: "Join Partition vs Join Key"
parent: Compliance
nav_order: 2
---

# Join Partition vs Join Key

## Summary

Reports Join stages where the join key does not match the partitioning of the input links.

## Description

In the parallel DataStage engine, data is internal split into separate partitions in order to run a number of smaller operations concurrently. This results in faster and more efficient processing, especially when sorting and joining data.

For Hash, Range and Modulus partitioning methods, they use column values to determine the partition which partition each record is placed into. For Same, the actual partitioning method is propagatedfrom upstream, and so we need to traverse up to the preceding stages until a specific method is selected (or until we reach the data source and can go no further).

For a pair of records in the left and right links to join, they must both be placed in the same partition.

If the columns used to determine the partition allocation are not in alignment with the keys used to join the two sources of data, records that are supposed to join may be in different partitions, and therefore not join as expected.

| Join Key           | Join Partition     | Result    |
|--------------------|--------------------|-----------|
| key1               | key2               | fail      |
| key1, key2         | key2               | fail      |
| key1, key2         | key1, key2         | pass      |
| key1, key2         | key1               | pass      |
| key1               | key1               | pass      |

## Actions

Ensure partitioning methods and columns are in alignment with selected join keys.

---
layout: page
title: Aggregator_Not_Preceded_by_‘Check’_Sort
parent: .
---

---
layout: default
title: Aggregator Not Preceded by ‘Check’ Sort
nav_order: 3
permalink: /aggregator_not_preceded_by_check_sort
---

# Aggregator Not Preceded by ‘Check’ Sort

|                  |                                                                             |
|------------------|-----------------------------------------------------------------------------|
| **Rule name**    | Aggregator not preceded by a ‘Check’ Sort.                                  |
| **Parallel Job** | Yes                                                                         |
| **Server Job**   | \-                                                                          |
| **Job Sequence** | \-                                                                          |
| **Description**  | Identifies Parallel Aggregator Stages not preceded by a ‘Check’ Sort Stage. |

# Description

This rule identifies Parallel Aggregator Stages which are not preceded
by a ‘Check’ Sort Stage. A ‘check’ sort is a Sort Stage with all of its
sort keys having a **Sort Key Mode** property of **'Do not Sort
(Previously Sorted)'**.

The DataStage Parallel execution framework typically inserts sorts
before any stage that requires matched key values or ordered groupings
(Join, Merge, Remove Duplicates, and Aggregator). Sorts are only
inserted automatically when the Job does not explicitly define an input
sort. Though ensuring correct results, inserted sorts can have a
significant (and often unnecessary) performance impact. There are two
ways to prevent the Parallel framework from inserting an un-necessary
sort:

-   Insert an upstream Sort stage on each link, defining all sort key
    columns with the “Do not Sort (Previously Sorted)” Sort Mode key
    property, or

-   Set the environment variable `APT_SORT_INSERTION_CHECK_ONLY`. This
    verifies sort order but does not perform a sort, aborting the job if
    data is not in the required sort order.

This rule verifies you have adopted the former approach.

# Actions

Ensure a Parallel Aggregator Stage is preceded by a Sort stage will all
sort keys specified, and ensure all of those sort keys have a **Sort Key
Mode** property of **'Do not Sort (Previously Sorted)'**.

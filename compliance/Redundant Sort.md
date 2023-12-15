---
layout: page
title: "Redundant Sort"
parent: Compliance
nav_order: 2
---

# Redundant Sort

## Summary

Identifies unnecessary sort opertions witihn Job designs.

## Descrioption

Sorting record data is the most expensive operation that can be performed by DataStage's Parallel Engine. While most experienced developers will arrange job logic to minimise the number of required sorts, there are valid patterns that use adjacent sort stages in conjunction with key change and cluster key flags.

This rule will identify adjacent sort stages which do not create key change, cluster key or have keys flagged as Don't Sort. Where adjacent sort stages are discovered, one will either be redundant and should be removed or a developer has introduced a logic error by not including a key change, cluster key or Don't sort flag.

## Actions

Remove redundant sorts.
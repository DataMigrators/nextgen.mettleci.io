---
layout: page
title: "Aggregator Stage Not Preceded by Check Sort Stage"
parent: Compliance
---

# Aggregator Stage Not Preceded by Check Sort Stage

## Summary

Aggregator Stage will only return the correct result if the keys are pre-sorted
In some organisation, the data are sourced from presorted dataset.

However, mistake can happen. If the dataset isn't presorted, the output from Aggregator Stage will be incorrect. One way to ensure the accident would not happen, without impacting the performance is to include a check sort stage before Aggregator Stage.

## Description

This rule perform the following checks:

1. The Aggregator stage is preceded by a Sort stage
2. The keys of the Aggregator Stage are a subset of those of the Sort Stage
3. The keys of the Sort Stage are set to either `(Previously Sorted)` or `(Previously Grouped)`

## Actions

Add a Check Sort stage to before Aggregator stage.

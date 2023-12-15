---
layout: page
title: "Aggregator Stage Not Preceded by Check Sort Stage"
parent: Compliance
nav_order: 2
---

# Aggregator Stage Not Preceded by Check Sort Stage

## Summary

Aggregator Stage will only return the correct result if the keys are pre-sorted
In some organisation, the data are sourced from presorted dataset.

However, mistake can happen. If the dataset is not presorted, the output from Aggregator Stage will be incorrect. One way to ensure the accident would not happen, without impacting the performance is to include a check sort stage before Aggregator Stage.

## Description

This rule check that...

1. Aggregator Stage is preceded by a Sort Stage
2. The keys of Aggregator Stage is a subset of Sort Stage
3. The keys in Sort Stage is set to either (Prevously Sorted) or (Previously Grouped)

## Actions

Add a Check Sort Stage to before Aggregator Stage.

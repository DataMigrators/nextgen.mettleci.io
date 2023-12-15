---
layout: page
title: "Sequential File Read Using Same Partitioning"
parent: Compliance
nav_order: 2
---

# Sequential File Read Using Same Partitioning

## Summary

Avoid reading from Sequential Files using the 'Same' partitioning method.

## Description

Avoid reading from sequential files using the 'Same' partitioning method.  Unless you have specified more than one source file this will result in the entire file being read into a single partition, making the entire downstream flow run sequentially unless you explicitly re-partition.

## Actions

Configure your Sequential File Stage to use a partitioning method other than 'Same'.

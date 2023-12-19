---
layout: page
title: "DataSet Not Using Same Partition"
parent: Compliance
---

# DataSet Not Using Same Partition

## Summary

Identifies Data Sets not using the 'Same' partitioning method

## Description

This rule identifies Parallel Job Data Sets which do not use the 'Same' partitioning method.

This is an IBM development tip documented here: [Sorting data - IBM Documentation](https://www.ibm.com/docs/en/iis/11.7?topic=tips-sorting-data) 

## Actions

When reading from Data Sets maintain your sort order by using ‘Same’ partitioning method.




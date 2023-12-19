---
layout: page
title: "Flow Using Random Function"
parent: Compliance
---

# Flow Using Random Function

## Summary
	
Identify Transformers (or other stages) using Random functions which produce non-deterministic output.

## Description

`Rand()`, `Random()` and `Srandom()` are examples of functions which produce non-deterministic output. 
Output columns whose values are dependent upon these functions will produce unexpected results which cannot, therefore, be useed in MettleCI unit tests.

## Actions

Parameterise your flow designs so that the non-deterministic value you require is provided as a flow parameter.  This value can then be fixed for unit testing purposes.

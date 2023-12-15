---
layout: page
title: "Flow Using Random Function"
parent: Compliance
nav_order: 2
---

# Flow Using Random Function

## Summary
	
Identify Transformers (or other stages) using Random functions which produce non-deterministic output.

## Description

Rand(), Random() & Srandom() are functions which produce non-deterministic output. This will cause false positive in MettleCI Unit Testing results

## Actions

Parameterise your flow designs so that the non-deterministic value you require is provided as a flow parameter.  This value can then be fixed for unit testing purposes.

---
layout: page
title: "Link Sort"
parent: Compliance
nav_order: 2
---

# Link Sort

## Summary

Identifies link sorts.

## Description

Developers where possible should utilise the sort stage rather than utilising the link sort facility. The sort stage allows more options for controlling the behaviour of the sort operation, appears in the job monitor as well as better communicating visually to other developers the main functions of the DataStage Flow.

This rule identifies Flows that utilise implicit sorts on a link which may prevent thedeveloper from taking advantqage of some opportunities for performance optimisation, and may reduce the easy maintainability of your Flows. Both link Sorts and explicit Sorts generate the same underlying orchestrate operators, however the explicit Sort stage offers the following options which are ot available on a link Sort:
 
- Sort Key Mode
- Create Cluster Key Change Column
- Create Key Change Column
- Output Statistics
- Sort Utility
- Restrict Memory Usage

## Actions

Replace link sorts with an explicit Sort stage.

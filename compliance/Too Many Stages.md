---
layout: page
title: "Too Many Stages"
parent: Compliance
nav_order: 2
---

# Too Many Stages

## Summary

Identify whether a flow has too many stages.

## Description

A flow design that contains too many stages becomes hard to maintain. 
Not only is it difficult to follow the logic but even physically moving around it and finding specific logic is hard.

This rule detects when a Flow or local Sub-flow exceeds a globally configurable stage limit. 
The default 'stageLimit' parameter is set to 25 but can be easily adjusted as required.  Stages contained in shared Subflows are excluded from the stage count.

## Actions

Split your flow into multiple flows, or remove unnecessary Stages.

# One Dataflow

## Summary

Verifies that there is only one data flow in a DataStage Flow.

## Description

A DataStage Flow has no restrictions on the number of independent data flows that can be created. Ideally a DataStage Flow should be created for each data flow to allow the calling application to manage the execution order.

## Actions

Split your Flow so that each dataflow is defined within its own dedicated Job. 

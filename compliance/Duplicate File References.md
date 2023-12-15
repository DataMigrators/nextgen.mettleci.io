---
layout: page
title: "Duplicate File References"
parent: Compliance
nav_order: 2
---

# Duplicate File References

## Summary

Verifies that a sequential file is...
 - only referenced once in a DataStage Flow's Sequential File, Complex Flat File, or DataSet stages, and
 - not simlutaneously being read and written in the same DataStage Flow

## Description

Sometimes developers will copy and paste stages rather than adding a new stage from the palette. In doing so there is a risk that the developer may not update the reference to the filename property which may result in incorrect processing being performed by the DataStage flow.

## Actions

Ensure that a file is only referenced once in a DataStage flow.

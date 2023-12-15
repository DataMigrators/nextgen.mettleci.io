---
layout: page
title: "Unique Sort"
parent: Compliance
nav_order: 2
---

# Unique Sort

## Summary

Identifies unique sorts.

## Description

Unique sorts are not visually represented on the DataStage canvas. Ideally the developer should use the Remove Duplicates stage so that this can be visually communicated with other developers. This rule will identify sort stages which have the `Allow Duplicates` property set to `false`.

## Actions

Replace unique sorts with a Remove Duplicates stage.

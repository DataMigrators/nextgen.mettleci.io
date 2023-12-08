# Transformer With Unreferenced Stage Variable

## Summary

Identifies Transformer Stage with an unreferenced Stage Variable (including Loop Variables).

## Description

A Transformer can be resource intensive, and having an unreferenced (i.e. unused) Stage/Loop variable...

 - can be an unnecessary waste of resources,
 - can cause confusion to Flow maintainers, and
 - may present a security vulnerability.

This rule identifies forgotten/unreferenced Stage/Loop variables.


## Actions

Remove the unreferenced Stage/Loop variable.


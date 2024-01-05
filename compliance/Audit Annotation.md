---
layout: page
title: "Audit Annotation"
parent: Compliance
---

# Audit Annotation

## Summary

Identifies where sensitive information may be present in DataStage Job and Sequence annotations.

## Description

This rule scans all annotations for instances of the words `hostname`, `password`, `organisation` (`en-UK` spelling) or `organization` (`en-US` spelling).

Note that it's impossible to use regular expressions to detect a password, host name, or organisation, but assuming one of these words is found the likelihood of the actual sensitive information being present is high.

Like all MettleCI Compliance Rules, this rule is provided as an example intended for you to adapt to suit your needs.

## Actions

Remove the sensitive information from your Job or Sequence annotation.

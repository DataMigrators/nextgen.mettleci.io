---
layout: page
title: "Unencrypted DB Passwords"
parent: Compliance
nav_order: 2
---

# Unencrypted database passwords

## Summary

Identifies connector stages which do not use encrypted passwords

## Description

Unencrypted passwords are a security risk and should be avoided. 

In DataStage all hardcoded password values are encrypted, and references to parameters are in plain text. This rule, therefore, simply needs to exclude:

- encrypted values, ie: `{dsnextenc}`
- a parameter that is set as 'encrypted'
- a reference to a parameterset, as the flow configuration does not store the details of parameters inside parametersets

---
layout: page
title: "Unencrypted DB Passwords"
parent: Compliance
---

# Unencrypted database passwords

## Summary

Identifies connector stages which don't use encrypted passwords

## Description

Unencrypted passwords are a security risk and should be avoided. 

In DataStage all hard-coded password values are encrypted, and references to parameters are in plain text. This rule, therefore, simply needs to exclude:

- encrypted values, e.g.: `{dsnextenc}`
- a parameter that's set as 'encrypted'
- a reference to a parameter set, as the flow configuration doesn't store the details of parameters inside parameter sets

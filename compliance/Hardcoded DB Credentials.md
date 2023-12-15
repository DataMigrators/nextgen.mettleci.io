---
layout: page
title: "Hardcoded DB Credentials"
parent: Compliance
nav_order: 2
---

# Hardcoded DB Credentials

## Summary

Ensures that all Database Connectors must use variables for location and credentials

## Description

Developers occasionally hard code database credentials into their jobs. These will cause job failures when deploying to a different project or server.

## Actions

Parameterise the identified hard-coded values.

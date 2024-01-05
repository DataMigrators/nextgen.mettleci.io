---
layout: page
title: "Connection Not Using Secrets Vault"
parent: Compliance
---

# Connection Not Using Secrets Vault

## Summary

Identifies Connections that don't store their credentials to use secrets in a vault.

## Description

Connections have the option of retrieving their credentials from a secret in a vault. If this option isn't taken the credential values are stored in plain text when the connection object is exported from the project, despite being displayed in the user interface as encrypted.

## Actions

Update the connection, setting the Input Method as 'Use secrets from a vault' .

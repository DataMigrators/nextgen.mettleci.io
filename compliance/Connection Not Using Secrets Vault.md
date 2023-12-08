# Connection Not Using Secrets Vault

## Summary

Identifies Connections that do not store their credentials to use secrets in a vault.

## Description

Connections have the option of retrieving their credentials from a secret in a vault.
If this option is not taken, the credential values are stored in plain text when the connection object is exported from the project, in spite of being displayed in the UI as excrypted.

## Actions

Update the connection, setting the Input Method as 'Use secrets from a vault' .

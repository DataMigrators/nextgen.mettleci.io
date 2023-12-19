---
layout: page
title: "System Time Dependency"
parent: Compliance
---

# System Time Dependency

## Summary

Identifies the use of system time functions in the job

## Description

Flows with date logic that reads from the system time make it difficult to perform repeatable/automated testing. Instead of using system date functions, it is recommended that the current date be passed in as a Flow parameter or derived from one of the `DSJobStart*` macros. During unit testing, the Flow parameter or `DSJobStart*` macro can be set to a fixed value. The actual job results can then be compared with the expected results without needing to account for differences due to system time.

## Actions

Replace the reference to the system time or date with a Flow Parameter of the appropriate type.

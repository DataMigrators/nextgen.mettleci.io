---
layout: page
title: "Prohibited Stages"
parent: Compliance
---

# Prohibited Stages

## Summary

Verifies that a job does not contain one or more prohibited stages.

## Description
Some projects may wish to restrict certain stages from production ready jobs. For example, peek stages are usually included by developers as a debugging aid and therefore should be removed after initial development.

The list of prohibited stages is easily configurable, and is currently defined as:


    // File
       'PxzOSFile',                 // zOSFile
    // Packs
       'EssbaseConnectorPX',        // Essbase Connector
       'PS_HRYPX',                  // Hierarchy for PeopleSoft Enterprise
       'PeoplesoftOnePX',           // JD Edwards EnterpriseOne
       'ORAAppsPX',                 // Oracle Applications Direct Access
       'orahrchy_PX',               // Oracle Applications Hierarchy
       'SALESFORCEJCConnectorPX',   // Salesforce
       'Siebel_BCPX',               // Siebel BC Pack
       'Siebel_DAPX',               // Siebel DA Pack
       'Siebel_EIMPX',              // Siebel EIM Pack
    // Processing
       'PxSVTransformer'            // BASIC Transformer

## Actions

- Redesign your job to avoid the use of prohibited stages, or
- Update the list of prohibited stages to permit stages you wish to permit.

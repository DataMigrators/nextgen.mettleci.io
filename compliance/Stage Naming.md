# Stage Naming

## Sumnmary

Stage Naming Standards for Parallel Flows and Watson Pipelines.

## Description

Verifies that a Flow's stage names match the specified naming standards. All naming standards are based on example asset naming standards and are expected to be customised to customer requirements.

The supplied naming standards are designed to reduce the amount of effort required for developers to understand what a Flow is doing without needing to inspect each stage on the Flow canvas and to quickly identify Flow stages from text based messages such as logged errors and compliance rule failures.

In most cases, this is achieved by having a prefix that reflects the stage type. However, for stages such as joins and funnels, the stage names provide additional information which cannot be determined without inspecting the stage in question (ie. inner/left/right join).

## Actions

Ensure your Flow Stages or Watson Pipeline DataStage components are named according to your naming standards.

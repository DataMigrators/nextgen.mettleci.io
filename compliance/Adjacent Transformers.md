---
layout: page
title: "Adjacent Transformers"
parent: Compliance
---

# Adjacent Transformers

## Summary
	
Identifies flow designs with adjacent Transformer stages.

## Description

Although powerful, transformers contain embedded logic that's not immediately obvious when looking at the canvas and reduces a developers ability to immediately understand a flow's logic. Overuse of transformers when more 'verbose' stages could achieve the same outcome can result in greater maintenance overhead.

THe presence of Adjacent transformers can be a symptom of a single transformer that has become so complex that a developer has needed to split its logic across two transformers. When this occurs, developers should consider if they could adopt an alternative implementation strategy using multiple standard stages working in conjunction rather than performing all logic within one or more transformer stages.

Adjacent transformers can also be a symptom of defect fixes that are clumsily 'tacked on' to an existing job rather than understanding the existing job logic and refactoring accordingly. Making job changes without having to refactor the existing code will degrade job quality and increase maintenance costs over time.

## Actions

Adjust your job design so that there are no adjacent transformers. Consider combining adjacent Transformer stages if possible.



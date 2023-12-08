# Job Using Transformer Surrogate Key

## Summary
	
Identifies flow designs that use NextSurrogateKey() in a Transformer.

## Description

Although powerful, transformers contain embedded logic that is not immediately obvious when looking at the canvas and reduces a developers ability to immediately understand a flow's logic. Overuse of transformers when more 'verbose' stages could achieve the same outcome can result in greater maintenance overhead.


## Actions

Adjust your flow design to use a Surrogate Key Generator stage instead.



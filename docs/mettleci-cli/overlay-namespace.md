---
status: reviewed #Status can be draft, reviewed or published. 
owner: John McKeever
tags:
  - Pipeline
  - CLI
---
# overlay namespace

The `overlay` namespace contains commands wich enable you to define and apply changes to DataStage assets in order to modify their behavior or configuration without altering the original asset directly. This is particularly useful in scenarios where you want to maintain different configurations for different environments (e.g., development, testing, production) or when you want to apply temporary changes for specific use cases.

## overlay apply

![overlay apply](../railroads/svgs/overlay-apply.svg "overlay apply syntax")

This command applies changes - defined in a [json5-formatted](https://json5.org/) overlay file - to one or more specified DataStage assets supplied in a directory or `.zip` file.

#### Parameters

- **-assets** *(Required)*
    - Path to DataStage export zip file or directory
- **-output** *(Required)*
    - Zip file or directory to write updated assets
- **-overlay** *(Required, repeatable)*
    - Directory containing asset overlays. Each overlay will be applied in specified order when providing multiple (e.g., `-overlay dir1 -overlay dir2`)
- **-properties**
    - Properties file with replacement values

#### Example
      
The format of the command looks like this...

```shell
$> mcix overlay apply \
   -assets /path/to/datastage-export.zip \
   -overlay /path/to/overlay-directory \
   -output /path/to/updated-assets.zip \
   -properties /path/to/properties-file.properties
```

Here's a practical example:

```shell
$> cat /overlays/ci/parameter_set/my-parameterset.json5
{
   param1: "value1",
   param2: "value2"
}

$> mcix overlay apply \
   -assets /datastage/datastage-export.zip \
   -overlay /overlays/ci/parameter_set/my-parameterset.json5 \
   -output ~/updated-assets.zip \
   -properties /path/to/properties-file.properties

MettleCI Command Line (build 1.0-SNAPSHOT)
(C) 2018-2025 Data Migrators Pty Ltd
overlay apply (1.0-SNAPSHOT)

.....

``` 

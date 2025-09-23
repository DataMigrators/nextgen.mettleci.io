---
status: reviewed #Status can be draft, reviewed or published. 
owner: John McKeever
tags:
  - Pipeline
  - CLI
---
# overlay namespace

The `overlay` namespace contains commands for ...

## overlay apply

![overlay apply](../railroads/svgs/overlay-apply.svg "overlay apply syntax")

This command ...

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
      
```shell
$> mcix overlay apply \
   -assets /path/to/datastage-export.zip \
   -overlay /path/to/overlay-directory \
   -output /path/to/updated-assets.zip \
   -properties /path/to/properties-file.properties

MettleCI Command Line (build 1.0-SNAPSHOT)
(C) 2018-2025 Data Migrators Pty Ltd
overlay apply (1.0-SNAPSHOT)

.....

``` 

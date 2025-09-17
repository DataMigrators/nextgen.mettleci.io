---
status: reviewed #Status can be draft, reviewed or published. 
owner: John McKeever
tags:
  - Pipeline
  - CLI
---
# System namespace

The `system` namespace contains commands for understanding, diagnosing, and customising your MettleCI CLI environment.

## system version

![system version](../railroads/svgs/system-version.svg "system version syntax")

This command displays.
- The MettleCI CLI [command shell[(command-shell)] version number
- Your OS versdion and architecture,
- Your username and language/locale settings, and
- A list of MettleCI CLI plugins loaded from your `plugins` folder.

#### Example
      
```shell
mcix>system version
system version (1.0-SNAPSHOT)
Mac OS X 26.0 (aarch64)
johnmckeever, English (Australia)

Loaded plugins:
 * MettleCI CP4D Asset-Analysis Plugin (1.0-SNAPSHOT)
 * MettleCI CP4D Compilation Plugin (1.0-SNAPSHOT)
 * MettleCI CP4D Import Plugin (1.0-SNAPSHOT)
 * MettleCI CP4D Overlays Plugin (1.0-SNAPSHOT)
 $>
``` 

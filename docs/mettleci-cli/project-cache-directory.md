---
classification: confidential #Remove this line if it's not IBM Confidential.
status: draft #Status can be draft, reviewed or published. 
owner: Add the main page authors
tags:
  - CLI
---
# The CLI 'project-cache' directory

The `-project-cache` parameter, which refers to a filesystem directory, is used with some MettleCI CLI commands to enable **incremental** operations. The directory supplied to the `-project-cache` option is the location where the CLI will read/write state information (sometimes referred to as **asset fingerprints**) used for performing incremental operations.  This directory should exist wherever the MettleCI CLI executes a command which relies on incremental behaviour, which normally occurs on the MettleCI Agent host under the instruction of your build agent.

In the sample pipelines shipped with MettleCI the incremental MettleCI CLI commands, assume the use of a locally-stored project cache and refer to the following project cache location:

```
%AGENTMETTLEHOME%\cache\%IISENGINENAME%\%DATASTAGE_PROJECT%
```

... which will normally translate to something similar to ...

```
C:\MettleCI\CLI\cache\MY.ENGINE.HOSTNAME\MyDataStageProject\
```

???+ info "Note"

    The project cache will always be a Windows-style filesystem reference (using backslashes), as many of the MettleCI CLI commands required in a CI/CD pipeline for pre-NextGen DataStage rely on Windows-only DataStage Client utilities.

There are a few things which need to be considered when deciding the location of project cache directories:

* The directory must be unique to a DataStage project

* It must be directly accessible from the CLI (i.e.. You can't specify an engine path if the CLI is running on a Client)

* ADVANCED: If multiple instances of the CLI are to be used for incremental operations (and hence multiple independent CLI instances need to share a common view of the incremental environment’s status) then the -project-cache needs to be available and synchronised across all of those CLI instances.  This is normally achieved using shared storage.

## Using multiple CLI environments

The last point becomes important if you are running a ‘pool’ of agents on the CI/CD pipeline.  If they were to all maintain their own independent copies of the -project-cache files then incremental fingerprints will differ between CLI instances, resulting in a significant drop in the performance benefits delivered by the incremental approach.

As an example of what could happen if a mettleci datastage deploy  command deploys to the same DataStage project with two different -project-cache directories:

1. Initial Deployment using MyCache
    1. Command mettleci datastage deploy ... -project-cache MyCache is invoked.
    1. This imports and compiles all ISX files as MyCache does not currently contain any stage information.
    1. This initially expensive process will always be required to establish. the initial contents of the project cache.
1. First Deployed Change using OtherCache
    1. Job MyFirstJob is checked in.
    1. Command mettleci datastage deploy ... -project-cache OtherCache is invoked.
    1. This imports and compiles all ISX files as OtherCache does not currently contain any stage information.
1. Second Deployed Change using MyCache
    1. Command mettleci datastage deploy ... -project-cache MyCache is run.
    1. This compares the Git codebase to the target DataStage environment and sees that all fingerprints are misaligned.  The command consequently re-imports and re-compiles all ISX files as MyCache contains state information which is not aligned with the target.  This could have been avoided using the proper project cache.

Alternatively you can use you agent labelling strategy to ensure that only a single CLI instance is used by your pipeline which eliminates the need to coordinate the project-cache amongst multiple environments.  In these cases a locally-stored project cache can be used.  If you subsequently decide to horizontally scale your agent capability then you will need to…

1. move your project cache to shared storage, and 
1. Modify your build pipelines to refer to that new shared location.


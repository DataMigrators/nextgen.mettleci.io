---
status: draft #Status can be draft, reviewed or published. 
owner: John McKeever
tags:
  - Pipelines
---

# Asset Overlays

## What are Overlays?

Assets in your Development environment typically contain 'hard wired' references other development-specific assets and configurations. Some examples of these are:

- Local parameters - Environment variables and User-specified parameters
- DataStage Parameter Sets - Environment variables and User-specified parameters. Also uncluding ...
  - Value Sets
  - Value Set Files
- Connection objects - Database references, credentials, file locations, etc.
   - Note that Data Connections in NextGen don't support parameter sets like those in DataStage Classic (CHECK!) as its values are 'baked in' at compilcation time, so adapting Connection Objects for different environments requires an unavoidable re-compilation. 
- NextGen Jobs, including ...
   - Execution engine,
   - Runtime priority queue (NAME?),
   - etc.

Deploying these assets into QA and Production environments can be challenging as the deployment process requires adapting these Development-specific refefences to those appropriate the the target environment before the asset an be executed in that environment.  This process of adaption needs to be automated to make it fast, accurate, repeatable, and traceable.  This is the role of the Overlays feature in DataStage NextGen.

## How Overlays work

Principles: We want deployments to be automated and traceable.  We don’t want people deploying Development-specific code to a test or production environment and making manual changes to adapt that development code to the new environment.

The ideal scenario is that you commit your Development-specific assets from your development environment and build a single software configuration (‘release’) to which environment-specific changes can be applied. 

When you deploy this development-specific release to a different environment, the mcix overlays feature will reference a set of values you have defined and apply them to the relevant assets in your release to dynamically generate a new, target environment-specific version of that release.  

This can also include environment runtime parameters, such as the name of the DataStage engine and workload queue upon which the jobs should be executed.

The environment-specific assets you supply are the ‘overlays’ which are simple text files (format below) which should idealy be themselves stored in Git

## Where to use Overlays

As part of a build and deployment pipeline implemented in your chosen CI/CD tool (Jenkins, GitHub Actions, Azure DevOps, etc.) 
This will use the ‘mcix overlay apply’ command (or, in supported build tools, the ‘mcix overlay apply’ build action/task – REFERENCE HERE)

For example, a typical CI process will respond to a Git commit by triggering a pipeline which will take the repository contents, move it into a working directory and running ‘mcix overlay apply’ for a nominated target environment (‘CI’, in this case).  The ‘mcix overlay apply’ command will look for the relevant overlay files defined in your repository and apply them by substituting the specified values in the specified assets. This modified set of assets will then be deployed to the relevant CI project after which your CI pipeline’s other processes will be performed - typically running flow analysis and unit tests.

Once CI has completed successfully you can then invoke (either manually, or automatically) a subsequent deployment process for another environment (testing or production) which will also use the ‘mcix overlay apply’ command to perform the same asset customisation process using a set of overlays files for that target environment.


## Project Structure

A typical MCIX project is organized into two main sections:

- DataStage assets: Contains the base DataStage assets committed by developers or it could be a project export zip, and
- Overlay Directories: Contains environment-specific folders where you can adjust the base DataStage assets using additional configuration files.

Here's an example directory structure:

```
└── datastage/
    ├── connection/
    │   └── database.json
    ├── data_intg_flow/
    │   ├── extract.json
    │   ├── transform.json
    │   └── load.json
    ├── job/
    │   ├── extract.DataStage job.json
    │   ├── transform.DataStage job.json
    │   └── load.DataStage job.json
    ├── orchestration_flow/
    │   └── batch.json
    ├── parameter_set/
    │   └── common_parameters.json
    └── DataStage-README.json
        └── overlays/
            ├── test/
            ├── qa/
            └── prod/
```

### DataStage Assets

DataStage assets contain exported CPD assets that are included in a release. This can be a directory
structure containing assets committed from CPD into a Git repository or a whole project export zip.
When defining these assets, they can be committed/exported directly from their source CPD project,
no environment-specific settings like database host and user names need to be modified. These
assets provide the “base” of your release, to which overlays are applied, producing an environment-
specific variation which is then deployed.

### Overlays

An overlay is a directory containing configuration files which are used to update DataStage assets
with environment-specific settings. For example, changing Parameter Set values or Job parameters.

The following asset types can be updated using overlays

- Parameter Sets
- Connections
- Jobs

All overlay configuration files are in JSON5 format (https://json5.org/), which is essentially JSON but with additional support for comments and optional quoting for property names.

Overlay files can be stored in any location you wish, however a good convention (and the convention employed by ) would be to store overlay files in a top-level folder structure which mirrors, somewhat, the structure of your top level `datastage` folder. i.e. 

```
{repository_root} / overlays / {environment} / {asset-type} / {asset_name}.json5
```

For example, the following file in your Git repository ...

`myProject/datastage/parameter_set/common_parameters.json`

... would be modified by the values in the following overlay file when being deployed to your CI project:
  
`myProject/overlays/ci/parameter_set/common_parameters.json5`

... and by the values in this overlay file when deployed to your PROD project:

`myProject/overlays/prod/parameter_set/common_parameters.json5`

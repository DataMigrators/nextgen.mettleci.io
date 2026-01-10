---
status: draft #Status can be draft, reviewed or published. 
owner: John McKeever
tags:
  - Pipelines
---

# Asset Overlays in DataStage NextGen

## The problem solved by Overlays

Development assets typically contain 'hard wired' references development-specific assets and configurations. Some examples of these are:

- Local parameters - Environment variables and User-specified parameters
- DataStage Parameter Sets - Environment variables and User-specified parameters. Also uncluding ...
   - Value Sets
   - Value Set Files
- Connection objects - Database references, credentials, file locations, etc.
    - Note that Data Connections in NextGen don't support parameter sets like those in DataStage Classic (CHECK!) as its values are 'baked in' at compilcation time, so adapting Connection Objects for different environments requires an unavoidable re-compilation. 
- NextGen Jobs, including
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

## Where, when, and how do I invoke this ‘overlays’ process?

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

## Example: Test environment

In the test overlay, you may want to change the common_parameters parameter set so that the
default inputDir and outputDir parameter values to refer to the correct directories for testing.
Add a common_parameters configuration file to the overlays/test/ directory:

```
└── overlays/
    ├── test/
    │   └── parameter_set/
    │       └── common_parameters.json5
    ├── qa/
    └── prod/
```

In the newly created common_parameters.json5 file, define the updated values for inputDir
and outputDir :

```
{
inputDir: "/test/input",
outputDir: "/test/output",
}
```

In this case our Overlay configuration file does not need to define an entry for every parameter in the
common_parameters parameter set – you only need to define the parameters which are being
updated by this overlay. 

## Example: Quality Assurance environment

In addition to setting QA specific parameter set parameters, the QA environment may also need
updating with different Database credentials. This is done by adding a database configuration
file to the overlays/qa/ directory:

```
└── overlays/
    ├── test/
    │   └── parameter_set/
    │       └── common_parameters.json5
    ├── qa/
    │   ├── connection/
    │   │   └── database.json5
    │   └── parameter_set/
    │   └── common_parameters.json5
    └── prod/
```

Along side a QA specific version of common_parameters.json5 , define the following
database.json5 to update the connection details of the database connection:

```
{
oracle_db_host: "qa.database.local",
oracle_service_name: "qa",
username: "scott",
password: "${DATABASE_PASSWORD}",
}
```

The connection properties that can be set using an overlay depends on the type of connection being
used. This example changes the database host, instance and credentials for a DataStage Oracle
Connection. Variables such as `${DATABASE_PASSWORD}` are substituted from either environment
variables or a separate property file passed to the mcix overlay command. Substitutions like this
allows parameters to be provided externally from your CI/CD Pipeline or setting sensitive credentials
without needing to store them in Git.

5.3 Example: Production environment
In Prod, you may want to customize both the parameter set and connection details as described for
the previous overlays but you might also need to further configure properties used when running
Jobs. For example, changing the warning limit to 0 so that transform.DataStage job fails if
there are any warnings and setting an environment variable parameter for the Flow requires a new
transform.DataStage job.json5 configuration file to be created in the overlays/prod/
directory:


```
└── overlays/
    ├── test/
    │   └── parameter_set/
    │   └── common_parameters.json5
    ├── qa/
    │   ├── connection/
    │   │ └── database.json5
    │   └── parameter_set/
    │   └── common_parameters.json5
    └── prod/
        ├── connection/
        │   └── database.json5
        ├── job/
        │   └── transform.DataStage job.json5
        └── parameter_set/
            └── common_parameters.json5
```

The job configuration file includes additional sections allowing overlays to change both the job
configuration as well as parameter values:

```
{
    configuration: {
        flow_limits: {
            warn_limit: 0
        }
        job_parameters: {
            "$APT_RECORD_COUNTS": true
            },
    }
}
````
## Adding, modifying and removing Parameter Set Value files

Overlays are not limited to updating the values in default parameter set values. They can also be used to modify or
even add new parameter set value files. 

For example, to modify an existing parameter set value file called
unit_testing for the common_parameters parameter set in the test overlay, add a new
unit_testing.json5 file in the /overlays/test/parameter_set/common_parameters/
folder:

└── overlays/
├── test/
│ └── parameter_set/
│ ├── common_parameters/
│ │ └── unit_testing.json5
│ └── common_parameters.json5

Like the previous examples, the unit_testing.json5 file contains just the entries that you wish to change within the unit_testing value file.

To add a new parameter set value file called performance_testing.json5 , follow the same
procedure but ensure the configuration file contains every non-default parameter:
└── overlays/
├── test/
│ └── parameter_set/
│ ├── common_parameters/
│ │ ├── performance_testing.json5
│ │ └── unit_testing.json5
│ └── common_parameters.json5
The unit_testing value file for common_parameters might be included as part of DataStage
assets export files in /datastage/ but you may want to remove it when deploying to production.
This can be configured by adding a unit_testing.json5 file to /overlays/prod/
parameter_set/common_parameters/ :
└── overlays/
├── test/
│ └── parameter_set/
│ ├── common_parameters/
│ │ ├── performance_testing.json5
│ │ └── unit_testing.json5
│ └── common_parameters.json5
├── qa/
│ ├── connection/
Adding, modifying and removing Parameter Set Value files – 10John McKeever – DataStage NextGen Overlays
│ │ └── database.json5
│ └── parameter_set/
│ └── common_parameters.json5
└── prod/
└── parameter_set/
├── common_parameters/
│ └── unit_testing.json5
└── common_parameters.json5
Instead of configuring /overlays/prod/parameter_set/common_parameters/
unit_testing.json5 with the parameters you want changed for your production environment,
set its content to null as shown below:
null
When applying this overlay configuration, the removed entirely.
unit_testing parameter set value file will be


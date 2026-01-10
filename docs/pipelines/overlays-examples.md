---
status: draft #Status can be draft, reviewed or published. 
owner: John McKeever
tags:
  - Pipelines
---

# Overlay examples

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

## Example: Production environment

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
```
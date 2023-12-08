# Connection Contains Parameter References

## Summary

Identifies Connections created by the migration from legacy Datastage to NextGen that contain references to
Flow Parameters.

## Description

https://www.ibm.com/docs/en/cloud-paks/cp-data/4.0?topic=datastage-migrating#reference_fbm_gww_yqb__post-mig__title__1

During the process of migrating legacy Datastage projects to NextGen, connection details and credentials
are moved from the job into a separate Connection, which may be also used outside of a DataStage context. However, when the connection details are parametereized, those parameter references are copied into the Connection object. These must be replaced with actual details so it can be tested and saved.


## Actions

Replace the parameter references with actual connection details.



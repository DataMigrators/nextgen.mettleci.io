---
layout: page
title: ICP4D_Unsupported_Stages
parent: .
---

# ICP4D Unsupported Stages

|                  |                                                                        |
|------------------|------------------------------------------------------------------------|
| **Rule name**    | ICP4D Unsupported Stages                                               |
| **Parallel Job** | Yes                                                                    |
| **Server Job**   | Yes                                                                    |
| **Job Sequence** | \-                                                                     |
| **Description**  | Identifies stages that are not yet supported by IBM Cloud Pak for Data |

# Description

Based on the IBM documentation:

-   <a
    href="https://docs-icpdata.mybluemix.net/transform/com.ibm.icpdata.doc/dfd/c_stages.html"
    rel="nofollow">https://docs-icpdata.mybluemix.net/transform/com.ibm.icpdata.doc/dfd/c_stages.html</a>

-   <a
    href="https://docs-icpdata.mybluemix.net/transform/com.ibm.icpdata.doc/dfd/c_supported_conn_stgs.html"
    rel="nofollow">https://docs-icpdata.mybluemix.net/transform/com.ibm.icpdata.doc/dfd/c_supported_conn_stgs.html</a>

Note that ALL server job stages are reported as incompatible with ICP4D,
as DataStage Server technology is not (nor will ever likely be)
supported on that platform.

# Actions

Options

-   Redesign your job to avoid the use of the incompatible stage

-   Speak to your IBM representative about potential forthcoming
    compatibility for the stage(s) in question

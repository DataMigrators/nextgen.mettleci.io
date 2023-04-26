# Nothing happens when I run a Server Job in Unit Testing mode

## Problem

If you start a Server Job Unit Test execution and the job status never
changes to the Queued/Running state, or the 'Starting Job...' message
does not appear in the job log, then it is likely that the preparation
phase of Unit Testing failed and the job execution never started.

## Diagnostics

Errors can be diagnosed by looking at the Unit Testing log which is
written to `<Project Root Directory>/&PH&/DSU.STUB.log` on the DataStage
engine where `<Project Root Directory>` is
usually `$DSHOME/../Projects/<Project Name>/`.

If the error in `DSU.STUB.log` is related to `authentication` and
`UniSessionException` you will see an entry like this:

``` java
2022-05-11 10:36:26,201 FATAL [TestServerJob] Error running unit testing
com.ascential.uo4j.uniobjects.UniSessionException: The user name provided is incorrect
    at com.ascential.uo4j.uniobjects.UniSession.connect(UniSession.java:261)
    at com.datamigrators.mettle.uv.Bootstrap.universeConnect(Bootstrap.java:265)
    at com.datamigrators.mettle.uv.Bootstrap.main(Bootstrap.java:170)
```

## Solution

A common error is that customers forget to <a
href="https://www.ibm.com/docs/en/iis/9.1?topic=mapping-defining-default-credentials"
rel="nofollow">add Default Credentials to the engine mapping</a> (the
installation step described <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/455737424/Installing+or+Upgrading+the+Server+Job+Unit+Test+Harness#Enable-Unit-Testing-of-Server-Jobs"
rel="nofollow">here</a>). Without these the Java Unit Test Harness can't
authenticate with Universe.

The credentials don't need to be `dsadm` but that is a common choice.

For other errors, the customer will need to verify that they have <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/455737424/Installing+or+Upgrading+the+Server+Job+Unit+Test+Harness#Enable-Unit-Testing-of-Server-Jobs"
rel="nofollow">enabled Unit Testing of Server Jobs</a> correctly, and
DataStage has permission to read to the
`dm-unittest-harness-<x.x-xxx>.jar`.

## Related articles

-   Page:

    <a
    href="/wiki/spaces/MCIDOC/pages/684523521/Enabling+extended+logging+for+MettleCI+Workbench"
    data-linked-resource-id="684523521" data-linked-resource-type="page"
    data-linked-resource-version="11">Enabling extended logging for MettleCI
    Workbench</a>

-   Page:

    <a
    href="/wiki/spaces/MCIDOC/pages/415432812/Nothing+happens+when+I+run+a+Server+Job+in+Unit+Testing+mode"
    data-linked-resource-id="415432812" data-linked-resource-type="page"
    data-linked-resource-version="11">Nothing happens when I run a Server
    Job in Unit Testing mode</a>

-   Page:

    <a
    href="/wiki/spaces/MCIDOC/pages/689897487/Enabling+extended+logging+in+Atlassian+Bamboo"
    data-linked-resource-id="689897487" data-linked-resource-type="page"
    data-linked-resource-version="6">Enabling extended logging in Atlassian
    Bamboo</a>

  

  

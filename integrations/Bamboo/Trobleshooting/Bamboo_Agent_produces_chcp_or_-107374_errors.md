# Bamboo Agent produces chcp or -107374 errors

## Problem

Atlassian Bamboo Remote Agents running on Windows (**before** Bamboo
v6.10) may produce a couple of errors:

-   'chcp' is not recognized as an internal or external command,
    operable program or batch file.

-   the Return Code -1073741515

If you encounter these symptoms you may need to implement the workaround
described below. This Bamboo defect is <a
href="https://confluence.atlassian.com/bamkb/bamboo-or-remote-agent-does-not-pick-up-the-path-environment-variable-correctly-when-running-as-a-windows-service-323982768.html"
rel="nofollow">documented here</a> and the status of the Atlassian fix
is <a
href="https://jira.atlassian.com/browse/BAM-16205?_ga=2.64634735.17192666.1547599188-2066070865.1384855247"
rel="nofollow">described here</a>.

If you need to run the MettleCI `dm-ccmigrate-plugin` via a Remote agent
you will need to use the following workaround

## Solution

Follow these steps to work around this Bamboo bug:

1.  Configure Bamboo Remote Agent to run as an application user (via
    Windows Services)

2.  Add the following 2 paths to the application user path (**not** the
    system path!)

    -   `%SystemRoot%\system32`

    -   `<DataStage Client Installation Path>\ASBNode\apps\proxy\cpp\vc60\MT_dll\bin`

<img src="attachments/458260491/458260506.png" class="image-center"
data-image-src="https://datamigrators.atlassian.net/wiki/download/attachments/458260491/ccmigrate-path.png?version=1&amp;modificationDate=1571877220709&amp;cacheVersion=1&amp;api=v2"
loading="lazy" width="226" />

If another, similar error code appears (e.g. -1073741819) we recommend
you copy the value of the system `PATH` environment variable and append
it to the local user `PATH` environment variable that is configured to
run the Bamboo remote agent service.

## Related articles

-   Page:

    <a
    href="/wiki/spaces/MCIDOC/pages/458457095/Bamboo+Agent+produces+chcp+or+-107374+errors"
    data-linked-resource-id="458457095" data-linked-resource-type="page"
    data-linked-resource-version="4">Bamboo Agent produces chcp or -107374
    errors</a>

-   Page:

    <a
    href="/wiki/spaces/MCIDOC/pages/733675552/MettleCI+System+Integrations"
    data-linked-resource-id="733675552" data-linked-resource-type="page"
    data-linked-resource-version="43">MettleCI System Integrations</a>

-   Page:

    <a href="/wiki/spaces/MCIDOC/pages/272138252"
    data-linked-resource-id="272138252" data-linked-resource-type="page"
    data-linked-resource-version="6">How does MettleCI work with HP ALM?</a>

-   Page:

    <a
    href="/wiki/spaces/MCIDOC/pages/116525745/Bamboo+DataStage+Capability"
    data-linked-resource-id="116525745" data-linked-resource-type="page"
    data-linked-resource-version="14">Bamboo DataStage Capability</a>

-   Page:

    <a
    href="/wiki/spaces/MCIDOC/pages/415465568/Failing+to+Read+Assets+from+the+DataStage+Repository"
    data-linked-resource-id="415465568" data-linked-resource-type="page"
    data-linked-resource-version="6">Failing to Read Assets from the
    DataStage Repository</a>

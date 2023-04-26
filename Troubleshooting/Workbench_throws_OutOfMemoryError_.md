# Workbench throws 'OutOfMemoryError'

## Problem

If the Workbench server is constrained for resources, there is a
possibility that Workbench will show errors in workbench log file
`mci.log` soon after startup.

## Solution

The JAVA_OPTS environment variable can be set to modify the resource
usage of Java. More specifically, you can halve the Java Stack Size from
2MB to 1MB.

e.g. `$JAVA_OPTS=-Xss1024K`

## Related articles

-   Page:

    <a
    href="/wiki/spaces/MCIDOC/pages/684523521/Enabling+extended+logging+for+MettleCI+Workbench"
    data-linked-resource-id="684523521" data-linked-resource-type="page"
    data-linked-resource-version="11">Enabling extended logging for MettleCI
    Workbench</a>

-   Page:

    <a href="/wiki/spaces/MCIDOC/pages/2396487711/SSH+Configuration"
    data-linked-resource-id="2396487711" data-linked-resource-type="page"
    data-linked-resource-version="8">SSH Configuration</a>

-   Page:

    <a
    href="/wiki/spaces/MCIDOC/pages/2396487681/MettleCI+CLI+produces+%27Failed+to+connect+to+host%27+error"
    data-linked-resource-id="2396487681" data-linked-resource-type="page"
    data-linked-resource-version="4">MettleCI CLI produces 'Failed to
    connect to host' error</a>

-   Page:

    <a
    href="/wiki/spaces/MCIDOC/pages/2386231418/Can%27t+upload+a+license+file+to+the+MettleCI+Setup+Wizard"
    data-linked-resource-id="2386231418" data-linked-resource-type="page"
    data-linked-resource-version="4">Can't upload a license file to the
    MettleCI Setup Wizard</a>

-   Page:

    <a
    href="/wiki/spaces/MCIDOC/pages/1165590529/Install+and+Configure+a+Jenkins+Agent"
    data-linked-resource-id="1165590529" data-linked-resource-type="page"
    data-linked-resource-version="23">Install and Configure a Jenkins
    Agent</a>

  

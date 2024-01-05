# Jira admin session timing out when setting up an App Link with Workbench

## Problem

While trying to set up a generic Application Link in Jira to allow
MettleCI Workbench to look up Jira items, Jira might start forcing you
to re-authenticate with Jira administrator credentials at every step.
This can prevent the user from completing the integration process.

If you:

-   have more than one Atlassian application installed on the server
    that Jira is hosted on; and

-   the applications (including Jira) are using the same URL except for
    the port number to differentiate between them…

…then they might be interfering with each other’s session information,
thereby causing this behaviour.

## Solution

The simplest solution is to modify each application’s *context path*
which results in a more application-specific URL.

The following pages describe the steps for the Atlassian applications
that are typically installed together when a MettleCI customer doesn’t
have their own applications to fulfill the usual application life-cycle
management (ALM) roles:

-   https://confluence.atlassian.com/jirakb/change-the-context-path-used-to-access-jira-server-225119408.html

<!-- -->

-   https://confluence.atlassian.com/bitbucketserver/moving-bitbucket-server-to-a-different-context-path-776640153.html

<!-- -->

-   https://confluence.atlassian.com/bamboo/changing-bamboo-s-root-context-path-396300360.html

MettleCI can work with many different vendors' ALM tools, not just
Atlassian’s suite.

## Related articles

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

    <a href="/wiki/spaces/MCIDOC/pages/2361917459"
    data-linked-resource-id="2361917459" data-linked-resource-type="page"
    data-linked-resource-version="1">🔒 Troubleshooting Template</a>

-   Page:

    <a
    href="/wiki/spaces/MCIDOC/pages/458850547/MettleCI+Command+Line+Reference"
    data-linked-resource-id="458850547" data-linked-resource-type="page"
    data-linked-resource-version="58">MettleCI Command Line Reference</a>

-   Page:

    <a href="/wiki/spaces/MCIDOC/pages/2224128037/Git"
    data-linked-resource-id="2224128037" data-linked-resource-type="page"
    data-linked-resource-version="7">Git</a>

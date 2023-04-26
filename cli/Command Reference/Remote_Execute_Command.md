# Remote Execute Command

# Purpose

Execute a specified script on a target host.

Note that the `-privateKey` parameter is the name of a private key file
accessible your `mettleci remote execute` command. If used as part of a
CI/CD pipeline then the build agent process running the command will
need access to the specified private key file.

# Syntax

See the examples below.

# Examples

``` bash
$> mettleci remote execute \
   -host my-engine.my-org.com \
   -username myusername \
   -password mypassword \
   -script "config/deploy.sh"
MettleCI Command Line (build 128)
(C) 2018-2022 Data Migrators Pty Ltd
Connecting to my-engine.my-org.com on port 22

Status code = 0 
exit code = 0
$>
```

# See Also

-   Page:

    <a href="/wiki/spaces/MCIDOC/pages/2412904449"
    data-linked-resource-id="2412904449" data-linked-resource-type="page"
    data-linked-resource-version="8">Workbench operations return ‘Could not
    find specified assets’</a>

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
    href="/wiki/spaces/MCIDOC/pages/2169307137/Build+Pipeline+SFTP+operations+fail+due+to+DataStage+Engine+name"
    data-linked-resource-id="2169307137" data-linked-resource-type="page"
    data-linked-resource-version="5">Build Pipeline SFTP operations fail due
    to DataStage Engine name</a>

  

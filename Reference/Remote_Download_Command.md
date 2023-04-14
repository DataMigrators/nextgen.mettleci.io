# Remote Download Command

# Purpose

This command transfers files from a target host to the host where the
command is being executed. This is typically used to download files from
a DataStage Engine to a <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/1770520622/A+Summary+of+MettleCI+Components#MettleCI-Agent-Host"
rel="nofollow">MettleCI Agent Host</a> as part of a MettleCI-enabled
build pipeline. This command…

-   uses the
    <a href="https://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol"
    rel="nofollow">SFTP protocol</a>,

-   authenticates using either a username/password or SSH Private Key,
    and

-   uses
    <a href="Ant_File_Patterns" data-linked-resource-id="2310307841"
    data-linked-resource-version="8" data-linked-resource-type="page">ANT
    File Patterns</a>

Note that all directories matched by transfer patterns are created in
the `-destination` folder.

Note that the `-privateKey` parameter is the name of a private key file
accessible your `mettleci remote execute` command. If used as part of a
CI/CD pipeline then the build agent process running the command will
need access to the specified private key file.

# Syntax

See the examples below.

# Examples

``` bash
$> mettleci remote download \
    -host my-engine.my-org.com \
    -username mci-user \ 
    -privateKey ~/.ssh/MyPrivateKey.pem \
    -source /source-dir \
    -destination /target-dir \ 
    -transferPattern DSParams

MettleCI Command Line (build 128)
(C) 2018-2022 Data Migrators Pty Ltd
Connecting to my-engine.my-org.com on port 22
Downloading 'DSParams' from remote directory '/source-dir' to local directory '/target-dir':
  DSParams - SUCCESS
Done. 1 file transferred.
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

# Remote Upload Command

# Purpose

The Remote Upload command provides a platform-agnostic mechanism to
upload files from your build system to a target host. This command…

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

# Examples

Successful upload

``` bash
$> mettleci remote upload 
   -host remote_host \
   -username myuser \
   -password mypassword \
   -source "C:\source-dir/." \
   -destination target-dir \
   -transferPattern "filesystem/**/*,config/*"

MettleCI Command Line (build 128)
(C) 2018-2022 Data Migrators Pty Ltd
Connecting to remote_host on port 22
Uploading 'filesystem/**/*,config/*' from local directory 'C:/source-dir/' to remote directory '/home/myuser/target-dir/':
        config\cleanup.sh - SUCCESS
        config\cleanup_unittest.sh - SUCCESS
        config\deploy.sh - SUCCESS
        config\DSParams - SUCCESS
        filesystem\deploy.sh - SUCCESS
Done. 5 files transferred.
```

Failed upload

``` java
$> mettleci remote upload 
-host remote_host 
-username myuser 
-password mypassword 
-source "C:\source-dir/." 
-destination target-dir 
-transferPattern "bad_pattern/*"

MettleCI Command Line (build 128)
(C) 2018-2022 Data Migrators Pty Ltd
Connecting to remote_host on port 22
Uploading 'bad_pattern/*' from local directory from local directory 'C:/source-dir/' to remote directory '/home/myuser/target-dir/':
Done. 0 files transferred.
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

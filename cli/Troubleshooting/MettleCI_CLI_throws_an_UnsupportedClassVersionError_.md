# MettleCI CLI throws an 'UnsupportedClassVersionError'

## Problem

When invoking the MettleCI command shell you receive the following error
message:

``` java
C:\Users\Developer>mettleci.cmd
Exception in thread "main" java.lang.UnsupportedClassVersionError: JVMCFRE003 bad major version; class=com/datamigrators/mettle/shell/MainClass, offset=6
        at java.lang.ClassLoader.defineClassImpl(Native Method)
        at java.lang.ClassLoader.defineClass(ClassLoader.java:331)
        at java.security.SecureClassLoader.defineClass(SecureClassLoader.java:155)
        etc.
```

… or you see this in the Workbench `mci.log` file:

``` java
Exception in thread "main" java.lang.UnsupportedClassVersionError: JVMCFRE003 bad major version; class=com/datamigrators/mettle/MettleApplication, offset=6
    at java.lang.ClassLoader.defineClassImpl(Native Method)
    at java.lang.ClassLoader.defineClass(ClassLoader.java:331)
    at java.security.SecureClassLoader.defineClass(SecureClassLoader.java:155)
    at java.net.URLClassLoader.defineClass(URLClassLoader.java:714)
    etc.
```

## Solution

This error is unavoidably produced when you invoke the MettleCI Command
Line, or attempt to start the Workbench service, in an environment which
is not running Java v1.8 or greater. In particular, the MettleCI Command
Line cannot work with the IBM-specific version of Java typically shipped
with DataStage. To confirm this is the issue login to the relevant host
as the `mciworkb` user and run `java -version` to verify the java
version.

To resolve this error please ensure you follow the first step in the <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/488898631/Installing+the+MettleCI+Command+Shell"
rel="nofollow">Command Line installation guide</a> which requests you to
<a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/488800406/Prerequisite+Java+Installation"
data-linked-resource-id="488800406" data-linked-resource-version="24"
data-linked-resource-type="page">install a more recent version of
Java</a>.

## Related articles

-   Page:

    <a href="/wiki/spaces/MCIDOC/pages/423952410/DataStage+Deploy+Command"
    data-linked-resource-id="423952410" data-linked-resource-type="page"
    data-linked-resource-version="30">DataStage Deploy Command</a>

-   Page:

    <a href="/wiki/spaces/MCIDOC/pages/716603405/Remote+Upload+Command"
    data-linked-resource-id="716603405" data-linked-resource-type="page"
    data-linked-resource-version="27">Remote Upload Command</a>

-   Page:

    <a
    href="/wiki/spaces/MCIDOC/pages/410681364/DataStage+Connector+Migration+Command"
    data-linked-resource-id="410681364" data-linked-resource-type="page"
    data-linked-resource-version="23">DataStage Connector Migration
    Command</a>

-   Page:

    <a
    href="/wiki/spaces/MCIDOC/pages/458850547/MettleCI+Command+Line+Reference"
    data-linked-resource-id="458850547" data-linked-resource-type="page"
    data-linked-resource-version="58">MettleCI Command Line Reference</a>

-   Page:

    <a href="/wiki/spaces/MCIDOC/pages/2309029939"
    data-linked-resource-id="2309029939" data-linked-resource-type="page"
    data-linked-resource-version="2">MettleCI CLI produces error of the form
    'Cannot run program "XXX"'</a>

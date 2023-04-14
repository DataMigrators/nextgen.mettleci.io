# ISX Cat Command

# Purpose

The `isx cat` command concatenates the specified ISX files into a single
ISX output file.

# Syntax

<img src="attachments/458784837/2280980483.png?width=353"
class="image-center" loading="lazy"
data-image-src="attachments/458784837/2280980483.png" data-height="181"
data-width="889" data-unresolved-comment-count="0"
data-linked-resource-id="2280980483" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20220816-092015.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="458784837"
data-linked-resource-container-version="24"
data-media-id="1ffd195f-a52b-4dac-905d-e45705d62f62"
data-media-type="file" width="353" />

## Using the `-pattern` option

Ensure you use single quotes (') around the specified pattern, or your
command shell will expand the pattern before passing it to the MettleCI
command line!

For example, let’s assume we have three ISX files:

``` java
$> ls -l *.isx
-rw-r--r--@ 1 johnmckeever  staff   5.5M 10 Aug 12:46 jm_one.isx
-rw-r--r--@ 1 johnmckeever  staff   4.7M 10 Aug 12:46 jm_three.isx
-rw-r--r--@ 1 johnmckeever  staff   6.2M 10 Aug 12:46 jm_two.isx
```

The command…

``` java
$> mettleci isx cat \
   -isx out.isx \
   -pattern ‘jm_*.isx’
```

…will successfully concatenate your three files, but…

``` java
$> mettleci isx cat \
   -isx out.isx \
   -pattern jm_*.isx
```

…will not work, as `jm_*.isx` will expand to
`jm_one.isx jm_three.isx jm_two.isx` which is syntactically incorrect.

## Using a single `-pattern` option

Note that a single `-pattern` option will take multiple patterns
delimited by a comma. For example…

``` java
$> mettleci isx cat \
   -isx out.isx \
   -pattern 'jm_o*.isx,jm_t*.isx'
```

… will process files `jm_one.isx`, `jm_two.isx`, and `jm_three.isx`.

## Example

``` java
$> mettleci isx cat \
   -isx cat_test2.isx \
   -pattern ‘assets/CleanUser*.isx’ \
   -pattern ‘assets/ConnectorTest*.isx’
loaded "assets\CleanUserDataHC.isx
        added "TEST1-ENGN.DATAMIGRATORS.IO/dstage1/Jobs/CleanUserDataHC.pjb"
loaded "assets\ConnectorTest.isx
        added "TEST1-ENGN.DATAMIGRATORS.IO/dstage1/Jobs/ConnectorTest.pjb"
loaded "assets\CleanUserDataFC.isx
        added "TEST1-ENGN.DATAMIGRATORS.IO/dstage1/Jobs/CleanUserDataFC.pjb"
loaded "assets\ConnectorTest2.isx
        added "TEST1-ENGN.DATAMIGRATORS.IO/dstage1/Jobs/ConnectorTest2.pjb"
loaded "assets\CleanUserData2.isx
        added "TEST1-ENGN.DATAMIGRATORS.IO/dstage1/Jobs/CleanUserData2.pjb"
loaded "assets\CleanUserData.isx
        added "TEST1-ENGN.DATAMIGRATORS.IO/dstage1/Jobs/CleanUserData.pjb"
loaded "assets\CleanUserData3.isx
        added "TEST1-ENGN.DATAMIGRATORS.IO/dstage1/Jobs/CleanUserData3.pjb"
isx cat complete.
```

  

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220816-092015.png](attachments/458784837/2280980483.png)
(image/png)  

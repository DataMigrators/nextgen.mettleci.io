# DSParams Diff Command

# Purpose

Compares two DSParams files and generates a new file containing
differences which can later be re-applied using the
<a href="DSParams_Merge_Command" data-linked-resource-id="458556064"
data-linked-resource-version="17"
data-linked-resource-type="page">DSParams Merge Command</a> or deleted
using the
<a href="DSParams_Delete_Command" data-linked-resource-id="458556054"
data-linked-resource-version="14"
data-linked-resource-type="page">DSParams Delete Command</a>.

# Syntax

<img src="attachments/458785100/2280685622.png?width=340"
class="image-center" loading="lazy"
data-image-src="attachments/458785100/2280685622.png" data-height="211"
data-width="723" data-unresolved-comment-count="0"
data-linked-resource-id="2280685622" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20220816-095532.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="458785100"
data-linked-resource-container-version="16"
data-media-id="26f17261-7091-4897-8c27-ad9fe69c876a"
data-media-type="file" width="340" />

# Examples

``` bash
$> mettleci dsparams diff \
   -before ./DSParams_old
   -after ./DSParams_new
   -diff ./DSParams_diff

MettleCI Command Line (build ${buildNumber})
(C) 2018-2020 Data Migrators Pty Ltd
Identfying differences in ./DSParams_new (-after) compared to ./DSParams_old (-before):
Identification complete.
Differences:
[EnvVarDefns]
APT_CONFIG_FILE\Parallel\3\FilePath/u01/prod/app/IBM/InformationServer870/Server/Configurations/default.apt\3\Project\Configuration file\The Parallel job configuration file.
APT_ORCHHOME\Parallel\3\DirPath/u01/prod/app/IBM/InformationServer870/Server/P…
"APT_NO_SORT_INSERTION"\1"1"
"QSM_DISABLE_DISTRIBUTE_COMPONENT"\1"1"
"TMPDIR"\1"/var/tmp"
[AUTO-PURGE]
PurgeEnabled=1
DaysOld=3
PrevRuns=0
$>
```

  

``` java
$> mettleci dsparams diff \
   -before ./DSParams_new
   -after ./DSParams_new
   -diff ./DSParams_diff

MettleCI Command Line (build ${buildNumber})
(C) 2018-2020 Data Migrators Pty Ltd
Identfying differences in ./DSParams_new (-after) compared to ./DSParams_new (-before):
Identification complete.
No differences identified.
%>
```

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220816-095532.png](attachments/458785100/2280685622.png)
(image/png)  

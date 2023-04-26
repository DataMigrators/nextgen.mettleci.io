# Workbench commit failed with java.lang.ArrayIndexOutOfBoundsException

## Problem

`MettleCI Workbench` throwing `java.lang.ArrayIndexOutOfBoundsException`
when committing asset(s)

<img src="attachments/2250276889/2250604553.png" class="image-center"
loading="lazy" data-image-src="attachments/2250276889/2250604553.png"
data-height="643" data-width="969" data-unresolved-comment-count="0"
data-linked-resource-id="2250604553" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="MettleCI_Workbench_-_Check_In_Error.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="2250276889"
data-linked-resource-container-version="4"
data-media-id="16c7e271-7351-4e43-ae5b-22fe033feb9f"
data-media-type="file" />

## Cause

IBM `istool` has a permission issue with `org.eclipse.osgi`

Run `istool` with the`-preview` option, and you should see problem rows
in line 4 and 5

``` java
Beginning Export Preview
 [1/1] ENGINE/DEV/Jobs/sj_mrt_subject.pjb
Previewed 1 assets
<title>Invalid Configuration Location</title>Locking is not possible in the directory "/opt/IBM/InformationServer/Clients/istools/cli/configuration/org.eclipse.osgi". A common reason is that the file system or Runtime Environment does not support file locking for that location. Please choose a different location, or disable file locking passing "-Dosgi.locking=none" as a VM argument.
ReliableFile is corrupt
```

## Solution

The solution is to change the permissions of the files that need to be
locked… Assuming istool is located under
`/opt/IBM/InformationServer/Clients/istool`

``` java
cd /opt/IBM/InformationServer/Clients/istools/cli/configuration/org.eclipse.osgi/.manager
chmod go+r .fileTable*
```

This will resolve the `istool` permission issue, and Workbench commit
issue.  

Note that the solution suggested in the error message (of passing
`"-Dosgi.locking=none" ` as a VM argument) does not always solve the
issue without the permissions change, and with the permissions change,
that argument is not needed.

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[MettleCI_Workbench\_-\_Check_In_Error.png](attachments/2250276889/2250604553.png)
(image/png)  

# Bamboo 'Unable to open file' errors on Windows

## Problem

Running a MettleCI Task in Bamboo results in an error message similar to

`Unable to open file C:\Windows\system32\config\systemprofile\AppData\Local\Temp\mci9115423909078010390.auth`.

The temporary directory (`%temp%`) for the current user is in a sub
directory of the `%windir%\System32` directory, usually caused by
running Bamboo or a remote agent Service using the `Local System`
account. When a 32bit Windows applications (ie. some DataStage clients)
are executed on a 64bit Operating System, Windows will redirect the file
system path from `%windir%\System32` to `%windir%\SysWOW64`. This will
prevent DataStage clients from accessing temporary files created by
MettleCI.

For more information about the Windows File System Redirector, please
refer to the Microsoft’s <a
href="https://docs.microsoft.com/en-us/windows/win32/winprog64/file-system-redirector"
rel="nofollow">documentation</a>.

## Solution

This problem usually occurs when Bamboo or a Bamboo Remote Agent are
running as a Windows Service using the `Local System` account.

There are two options for resolving this issue.

**Option 1**: Create a dedicated Windows Account and change the Bamboo
or Bamboo Remote Agent services to run under that account as follows:

1.  Locate the Bamboo Remote Agent in the Windows Services settings,
    right click and select “Properties”.  

    <img src="attachments/464683045/464453692.png" class="image-center"
    loading="lazy" data-image-src="attachments/464683045/464453692.png"
    data-height="293" data-width="955" data-unresolved-comment-count="0"
    data-linked-resource-id="464453692" data-linked-resource-version="1"
    data-linked-resource-type="attachment"
    data-linked-resource-default-alias="image-20191122-020319.png"
    data-base-url="https://datamigrators.atlassian.net/wiki"
    data-linked-resource-content-type="image/png"
    data-linked-resource-container-id="464683045"
    data-linked-resource-container-version="8"
    data-media-id="53df43aa-1345-45ef-87f7-3b316daa04eb"
    data-media-type="file" />

2.  Click the “Log On” tab, Select “This account” and click the
    “Browse…” button.

    <img src="attachments/464683045/465600689.png" class="image-center"
    loading="lazy" data-image-src="attachments/464683045/465600689.png"
    data-height="470" data-width="406" data-unresolved-comment-count="0"
    data-linked-resource-id="465600689" data-linked-resource-version="1"
    data-linked-resource-type="attachment"
    data-linked-resource-default-alias="image-20191202-214106.png"
    data-base-url="https://datamigrators.atlassian.net/wiki"
    data-linked-resource-content-type="image/png"
    data-linked-resource-container-id="464683045"
    data-linked-resource-container-version="8"
    data-media-id="5c98242f-a2cf-4ea1-a3bd-7035072ff1f4"
    data-media-type="file" />

3.  Enter the username of that account you wish to use in the textbox
    and click “Check Names”

    <img src="attachments/464683045/465535140.png" class="image-center"
    loading="lazy" data-image-src="attachments/464683045/465535140.png"
    data-height="255" data-width="460" data-unresolved-comment-count="0"
    data-linked-resource-id="465535140" data-linked-resource-version="1"
    data-linked-resource-type="attachment"
    data-linked-resource-default-alias="image-20191202-214252.png"
    data-base-url="https://datamigrators.atlassian.net/wiki"
    data-linked-resource-content-type="image/png"
    data-linked-resource-container-id="464683045"
    data-linked-resource-container-version="8"
    data-media-id="ec5a8d6f-f2bd-44df-826e-991a49b38fc9"
    data-media-type="file" />

    If your username is not found after clicking “Check Names”, click
    the “Locations…” button and select “Entire Directory”.

4.  Save changes and restart the Bamboo Remote Agent Service.

**Option 2**: Override Java’s temporary directory location to a
directory that is not a sub directory of the `%windir%\System32`
directory:

1.  Edit `<bamboo agent directory>\conf\wrapper.conf` where
    `<bamboo agent directory>` is the directory that your Bamboo remote
    agent was installed in.

2.  Add `wrapper.java.additional.3=-Djava.io.tmpdir=../temp` after the
    line starting with `wrapper.java.additional.2`.

3.  Save the file and restart the Bamboo Remote Agent Service.

It is strongly recommended that **Option 1** is applied where possible -
running services under the **Local System** account can cause problems
during DataStage compilation. See
<a href="The_MettleCI_Bamboo_Plugin_Fails_When_Compiling_a_Job"
data-linked-resource-id="465797125" data-linked-resource-version="5"
data-linked-resource-type="page">MettleCI never completes job
compilation</a> for details.

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20191122-020319.png](attachments/464683045/464453692.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20191122-020452.png](attachments/464683045/464551988.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20191202-214106.png](attachments/464683045/465600689.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20191202-214252.png](attachments/464683045/465535140.png)
(image/png)  

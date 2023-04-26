# MettleCI IBM OEM Release 1.0

# Package Summary

|                               |              |
|-------------------------------|--------------|
| **Package name**              | MettleCI 1.0 |
| **Release Date (yyyy-mm-dd)** | 2021-03-23   |

## Package Contents

<table class="confluenceTable" data-layout="default"
data-local-id="2acf7ff5-62d1-45b6-a6cb-4095b88fa3ae">
<tbody>
<tr class="odd">
<td class="confluenceTd"
data-highlight-colour="#f0f0f0"><p><strong>Function</strong></p></td>
<td class="confluenceTd"
data-highlight-colour="#f0f0f0"><p><strong>File</strong></p></td>
<td class="confluenceTd"
data-highlight-colour="#f0f0f0"><p><strong>Timestamp</strong></p></td>
<td class="confluenceTd"
data-highlight-colour="#f0f0f0"><p><strong>Size</strong></p></td>
<td class="confluenceTd"
data-highlight-colour="#f0f0f0"><p><strong>Type</strong></p></td>
<td class="confluenceTd"
data-highlight-colour="#f0f0f0"><p><strong>Notes</strong></p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>Command Shell</p></td>
<td
class="confluenceTd"><p><code>dm-mettleci-command-shell-1.1-162-dist.zip</code> WINDOWS</p>
<p><code>dm-mettleci-command-shell-1.1-162.noarch.rpm</code> UNIX</p></td>
<td class="confluenceTd"><p>2021-02-24 09:48:55</p>
<p>2021-02-24 09:48:46</p></td>
<td class="confluenceTd"><p>163.3 MB</p>
<p>159.3 MB</p></td>
<td class="confluenceTd"><p>ZIP</p>
<p>RPM</p></td>
<td class="confluenceTd"><p>These Command Shell distributions each
include a full set of the latest versions of all MettleCI CLI plugins
(commands).</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>Workbench</p></td>
<td
class="confluenceTd"><p><code>dm-mettleci-workbench-1.0-1165-setup.exe</code> WINDOWS</p>
<p><code>dm-mettleci-workbench-1.0-1165.noarch.rpm</code> UNIX</p></td>
<td class="confluenceTd"><p>2021-03-10 00:22:37</p>
<p>2021-03-10 00:22:24</p></td>
<td class="confluenceTd"><p>57.1 MB</p>
<p>56.9 MB</p></td>
<td class="confluenceTd"><p>EXE</p>
<p>RPM</p></td>
<td class="confluenceTd"></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>Compliance Rules</p></td>
<td
class="confluenceTd"><p><code>dm-compliance-rules-159m.zip</code></p></td>
<td class="confluenceTd"><p>2021-03-10 17:17:00</p></td>
<td class="confluenceTd"><p>357.4 kB</p></td>
<td class="confluenceTd"><p>ZIP</p></td>
<td class="confluenceTd"><p>A ready-to-use Git repository
folder</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>Sample Build Pipelines</p></td>
<td class="confluenceTd"><p><code>mettleci-azure-template.zip</code></p>
<p><code>mettleci-gitlab-template.zip</code></p>
<p><code>mettleci-jenkins-template.zip</code></p></td>
<td class="confluenceTd"><p>2020-10-30 12:30:17</p>
<p>2020-10-30 12:29:01</p>
<p>2020-10-30 12:29:45</p></td>
<td class="confluenceTd"><p>21.0 kB</p>
<p>19.5 kB</p>
<p>20.2 kB</p></td>
<td class="confluenceTd"><p>ZIP</p>
<p>ZIP</p>
<p>ZIP</p></td>
<td class="confluenceTd"></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>Parallel Unit Test Harness</p></td>
<td
class="confluenceTd"><p><code>dm-unittest-harness-1.0-319-setup.exe</code> WINDOWS</p>
<p><code>dm-unittest-harness-1.0-319.noarch.rpm</code> UNIX</p></td>
<td class="confluenceTd"><p>2021-03-05 16:06:45</p>
<p>2021-03-05 16:06:38</p></td>
<td class="confluenceTd"><p>13.8 MB</p>
<p>12.1 MB</p></td>
<td class="confluenceTd"><p>EXE</p>
<p>RPM</p></td>
<td class="confluenceTd"></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>Server Unit Test Harness</p></td>
<td
class="confluenceTd"><p><code>dm-server-unit-test-harness-1.0-001.zip</code>
 WINDOWS  UNIX</p></td>
<td class="confluenceTd"><p>2021-03-23 22:59:00</p></td>
<td class="confluenceTd"><p>4 kB</p></td>
<td class="confluenceTd"><p>ZIP</p></td>
<td class="confluenceTd"><p>This provides a Server interface to the
capabilities provided by the Parallel test harness which must also be
installed to provide unit test functionality.</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>License</p></td>
<td class="confluenceTd"><p><code>license.txt</code></p>
<p><code>properties.txt</code></p></td>
<td class="confluenceTd"><p>2021-03-10 00:18:00</p>
<p>2021-03-10 00:18:00</p></td>
<td class="confluenceTd"><p>1 kB</p>
<p>98 Bytes</p></td>
<td class="confluenceTd"><p>TXT</p>
<p>TXT</p></td>
<td class="confluenceTd"><p>The license file, valid from 2021-03-10 to
2099-12-31</p>
<p>A human-readable file describing the constraints within the supplied
license</p></td>
</tr>
</tbody>
</table>

**Important notes about** `license.txt`

-   This MettleCI Release 1.0 package is currently the only place that
    you will find a MettleCI license file

-   Since this initial release we have standardised on `mettleci.lic` as
    the name of the license file, which you will need to deploy to
    enable your MettleCI Workbench and MettleCI CLI instances.
    **Consequently you should rename** `license.txt` **to**
    `mettleci.lic` **after unpacking this distribution media.**

# Change Log

-   MettleCI Workbench

    -   Initial release

-   MettleCI Unit Test Harness

    -   Initial release

-   MettleCI Command Line Interface

    -   Initial release

-   MettleCI Compliance Rules Repository

    -   Initial release

# Notes

For documentation please visit <a href="http://docs.mettleci.io"
rel="nofollow"><u>http://docs.mettleci.io</u></a>

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[dm-mettleci-workbench-1.0-1425.noarch.rpm](attachments/2245033985/2245034001.rpm)
(application/x-rpm)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[dm-mettleci-workbench-1.0-1425-setup.exe](attachments/2245033985/2245034004.exe)
(application/x-msdownload)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[dm-s2px-analysis-plugin-1.0-46.jar](attachments/2245033985/2245034007.jar)
(application/java-archive)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[dm-s2px-conversion-plugin-1.0-436.jar](attachments/2245033985/2245034010.jar)
(application/java-archive)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[command-shell-1.1-133-dist.zip](attachments/2245033985/2245034013.zip)
(application/zip)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[dm-unittest-harness-1.0-350-setup.exe](attachments/2245033985/2245034016.exe)
(application/x-msdownload)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[dm-unittest-harness-1.0-350.noarch.rpm](attachments/2245033985/2245034019.rpm)
(application/x-rpm)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[dm-server-unit-test-harness-routine-1.0-350.zip](attachments/2245033985/2245034022.zip)
(application/zip)  

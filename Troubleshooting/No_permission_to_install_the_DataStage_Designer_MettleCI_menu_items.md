# No permission to install the DataStage Designer MettleCI menu items

# Problem

The MettleCI Workbench provides a <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/454623235/Integrating+MettleCI+Workbench+and+DataStage+Designer+on+Windows"
data-linked-resource-id="454623235" data-linked-resource-version="15"
data-linked-resource-type="page">facility to install custom MettleCI
menu items</a> in your DataStage Designer client application. When you
click the **Integrate withe DataStage Client** button on the front page
of the MettleCI Workbench your browser will attempt to download a
Windows EXE (executable) file which will automatically install the menu
items for you by modifying your Windows registry. Some users, however,
may not possess the permissions necessary to download and.or execute the
necessary `.exe` file from the MettleCI Workbench application.

# Solution

If your users do not have permission to run the EXE installer then users
can configure their MettleCI Custom menu items themselves. To do this,
open your DataStage Designer client and select the **Tools → Custom →
Customize** menu item. This presents a dialog which enables you to
create custom menu items

<img src="attachments/745078910/2062450689.png?width=217"
class="image-center" loading="lazy"
data-image-src="attachments/745078910/2062450689.png" data-height="830"
data-width="1110" data-unresolved-comment-count="0"
data-linked-resource-id="2062450689" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20211028-234600.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="745078910"
data-linked-resource-container-version="12"
data-media-id="e19ee4fd-27fe-4f5f-a4f7-c677dfafaa2d"
data-media-type="file" width="217" />

Create the required MettleCI menu items using the values detailed below:

|                                    |              |                                                                              |                                                 |
|------------------------------------|--------------|------------------------------------------------------------------------------|-------------------------------------------------|
| **Menu text**                      | **Command**  | **Arguments**                                                                | **Status bar**                                  |
| MettleCI - Check Compliance        | explorer.exe | "http://%Host:8080/#/compliance/run?project=%ProjectName&job=%JobName"       | Check job compliance with standards             |
| MettleCI - Unit Test Specification | explorer.exe | "http://%Host:8080/#/unittest/spec?project=%ProjectName&job=%JobName"        | View of modify job unit test specification      |
| MettleCI - Unit Test Results       | explorer.exe | "http://%Host:8080/#/unittest/result?project=%ProjectName&job=%JobName"      | View job unit test results                      |
| MettleCI - Commit Asset            | explorer.exe | "http://%Host:8080/#/checkin?engine=%Host&project=%ProjectName&job=%JobName" | Commit job or other asset(s) to version control |

**Notes**

-   The **explorer.exe** command will invoke your Windows system-default
    web browser

-   Make sure you include the double quotes in the 'Arguments’ value

If you have configured your MettleCI Workbench to communicate over HTTPS
then ensure the protocol specifier (**HTTPS**) and port (e.g., **8443**)
are appropriately adjusted.

For example, a MettleCI Workbench using HTTPS over port 8443 the
**Commit Asset** entry would look like:

“https://%Host:8443/#/checkin?engine=%Host&project=%ProjectName&job=%JobName"

Describe the detailed steps the user needs to take to resolve the
problem, where possible. If the steps are described elsewhere in the
documentation then link to those pages rather than repeat those details
here.

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200514-134005.png](attachments/745078910/747929622.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20211028-234600.png](attachments/745078910/2062450689.png)
(image/png)  

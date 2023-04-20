---
layout: page
title: Starting_Stopping_the_Monitoring_MettleCI_Workbench_Service
parent: .
---

# Starting, Stopping the Monitoring MettleCI Workbench Service

-   [Unix](#Starting,StoppingtheMonitoringMettleCIWorkbenchService-Unix)
    -   [Starting](#Starting,StoppingtheMonitoringMettleCIWorkbenchService-Starting)
    -   [Stopping](#Starting,StoppingtheMonitoringMettleCIWorkbenchService-Stopping)
    -   [Checking
        Status](#Starting,StoppingtheMonitoringMettleCIWorkbenchService-CheckingStatus)
-   [Windows](#Starting,StoppingtheMonitoringMettleCIWorkbenchService-Windows)
    -   [Starting](#Starting,StoppingtheMonitoringMettleCIWorkbenchService-Starting.1)
    -   [Stopping](#Starting,StoppingtheMonitoringMettleCIWorkbenchService-Stopping.1)
    -   [Checking
        Status](#Starting,StoppingtheMonitoringMettleCIWorkbenchService-CheckingStatus.1)

In all instances a **Restart** of the MettleCI Workbench involves simply
following the steps for **Stop** followed by **Start**.

# Unix

## Starting

Start the MettleCI Workbench service using the following command

``` java
$> sudo service dm-mettleci-workbench start
$> # or for AIX...
$> mciworkbench.rc start
```

## Stopping

Stop the MettleCI Workbench service using the following command

``` java
$> sudo service dm-mettleci-workbench stop
$> # or for AIX...
$> mciworkbench.rc start
```

## Checking Status

Verify your Workbench service is running:

``` java
$> sudo service dm-mettleci-workbench status
$> # or for AIX...
$> mciworkbench.rc status
```

# Windows

<img src="attachments/1954578453/1953955861.png?width=380"
class="image-left" loading="lazy"
data-image-src="attachments/1954578453/1953955861.png" data-height="50"
data-width="737" data-unresolved-comment-count="0"
data-linked-resource-id="1953955861" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="Screen Shot 2019-11-20 at 4.11.01 pm.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="1954578453"
data-linked-resource-container-version="4"
data-media-id="812c9e1f-798a-4611-bbb5-9f821917397d"
data-media-type="file" width="380" />

## Starting

1.  Open the **Services** application.

2.  Double-click the **MettleCI Workbench** service.

3.  Click the **Start** button.

4.  Click the **Apply** button.

5.  Click the **OK** button.

## Stopping

1.  Open the **Services** application.

2.  Double-click the **MettleCI Workbench** service.

3.  Click the **Stop** button.

4.  Click the **Apply** button.

5.  Click the **OK** button.

## Checking Status

1.  Open the Services application.

2.  Verify that the **MettleCI Workbench** service has the Status
    **Running**.

3.  Verify that the **MettleCI Workbench** service has Startup Type
    **Automatic**.

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [Screen
Shot 2019-11-20 at 4.11.01
pm.png](attachments/1954578453/1953955861.png) (image/png)  

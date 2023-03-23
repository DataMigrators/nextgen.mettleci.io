---
layout: page
title: Configuring_MettleCI_Workbench_to_use_Custom_App_and_Data_Directories
parent: Configuration
---

# Configuring MettleCI Workbench to use Custom App and Data Directories

In the event that there are constraints which prevent using the usual
Mettle Home directory `/opt/dm/mci` for storage, it is possible to move
the ‘MettleHome’ directory to a different location residing in a data
area. For example, this would be useful in a grid environment where
`/opt/dm/mci` is not on shared storage but the data area is on shared
storage.

Steps for moving ‘MettleHome' to `/data/mci` are as follows:

1.  Shutdown the workbench service

2.  Edit `/opt/dm/mci/config.yml` and change `mettleHome` to `/data/mci`

3.  Move files in `/opt/dm/mci/` to `/data/mci` but leave the following
    files in place:-

    -   `config.yml`

    -   `dm-mettleci-workbench`

    -   `mci.log`

    -   `mettle-ui-x.x-xxx.jar`

    -   `METTLE_UI.pid`

    -   `start-mettleci.sh`

4.  Ensure that permissions on `/data/mci` match those of `/opt/dm/mci`.
    By default this is `mciworkb:dstage`

5.  Start the workbench service

6.  Edit `/opt/IBM/InformationServer/Server/PXEngine/bin/osh-dm` and
    change `export DM_METTLE_HOME` to `/data/mci`

Workbench and unit testing will now work fine. You don’t need to bounce
DataStage for changes to take effect.

Installing an update to the Unit Test harness will overwrite `osh-dm`,
so…

-   When upgrading the Parallel Unit Test Harness you ***must***
    re-apply Step 6

-   When upgrading the Workbench you will ***not*** need to re-apply
    Step 6.

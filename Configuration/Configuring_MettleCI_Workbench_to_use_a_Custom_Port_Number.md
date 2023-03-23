---
layout: page
title: Configuring_MettleCI_Workbench_to_use_a_Custom_Port_Number
parent: Configuration
---

# Configuring MettleCI Workbench to use a Custom Port Number

## Using a custom port while running the MettleCI Setup Wizard

Create a file `/opt/dm/mci/setupEnv.sh` containing a line of the
following format:

``` java
export JAVA_OPTS=-Ddw.server.applicationConnectors[0].port=<port-number>
```

Ensure the file is owned by `mciworb` and has permissions 755
(`-rwxr-xr-x`). For example,

``` java
$> sudo chmod 755 /opt/dm/mci/setupEnv.sh

$> sudo chown mciworkb /opt/dm/mci/setupEnv.sh

$> ls -l /opt/dm/mci/setupEnv.sh
-rwxr-xr-x 1 mciworkb dstage 64 Sep 30 09:02 /opt/dm/mci/setupEnv.sh

$> cat /opt/dm/mci/setupEnv.sh
export JAVA_OPTS=-Ddw.server.applicationConnectors[0].port=5678

$>
```

Once `/opt/dm/mci/setupEnv.sh` has been created restart your Workbench
service using the Service Manager utility on Windows, or this command on
Unix:

``` bash
$> sudo service dm-mettleci-workbench restart
```

The MettleCI Setup wizard discover this file and will now be accessible
via the specified port number (`5678` in the example above).

Once the MettleCI Setup Wizard is complete, delete the `setupEnv.sh`
file and complete the steps in the following section.

## Changing ports after completing the MettleCI Setup wizard

You can request Workbench to operate on any ports you like by updating
the following section in your `<METTLECI-HOME-DIRECTORY>/config.yml`
file. This example exposes Workbench over HTTP on port 9090:

``` java
server:
  applicationConnectors:
    - type: http
      port: 9090
```

When <a href="Configuring_MettleCI_Workbench_to_use_HTTPS"
data-linked-resource-id="458556297" data-linked-resource-version="56"
data-linked-resource-type="page">HTTPS has been configured</a>, the
`applicationConnector` type will be `HTTPS` and the server section will
contain additional HTTPS-specific properties. You should only update the
HTTPS `port` property, leaving the other values unchanged.

Once you’ve made your changes restart your Workbench service using the
Service Manager utility on Windows, or this command on Unix: .

``` bash
$> sudo service dm-mettleci-workbench restart
```

Verify Workbench is up and running on the appropriate ports for HTTP
and/or HTTPS by navigating to `https://<host-url>:<http-port>` and
`http://<host-url>:<https-port>` in your browser, as appropriate.

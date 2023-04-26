# The Workbench is unreachable, or the Workbench service won't start

# Problem

The Workbench URL cannot be reached (e.g. returns a 404 error) and/or
the service appears to not be running. Common symptoms for each
operating system are:

<img src="images/icons/grey_arrow_down.png" class="expand-control-image"
style="vertical-align:middle;" />Windows

<img src="attachments/518979607/772964353.png" class="image-center"
loading="lazy" data-image-src="attachments/518979607/772964353.png"
data-height="215" data-width="492" data-unresolved-comment-count="0"
data-linked-resource-id="772964353" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20200526-233641.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="518979607"
data-linked-resource-container-version="23"
data-media-id="5c1d90e2-eaa4-4424-9a9e-8d7d2c5fe745"
data-media-type="file" />

<img src="images/icons/grey_arrow_down.png" class="expand-control-image"
style="vertical-align:middle;" />Unix

``` java
$> sudo service dm-mettleci-workbench start
MettleCI Workbench is not running
Starting MettleCI Workbench ...
MettleCI Workbench has been started
$> sudo service dm-mettleci-workbench status
/opt/dm/mci/METTLE_UI.pid dead but pidfile exist
```

# Diagnostics

There are a number of diagnostic steps you can take to help understand
and resolve your particular Workbench issue:

### Ensure you’re using a correct, unblocked URL for the MCI Workbench

The Workbench is most typically installed on your DataStage Engine tier,
in which case you would use…

-   `http://[your-engine-tier-URL]:8080`, and/or

-   `https://[your-engine-tier-URL]:8443` (if you've <a
    href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/458556297/Configuring+Workbench+to+use+HTTPS"
    rel="nofollow">configured Workbench to use HTTPS</a>)

Ensure that your MettleCI Workbench menu items are configured to use the
correct URL’s.

### Ensure that the relevant ports are available

By default, MettleCI uses ports 8080 / 8443 (for the end-user UI) and
8081 (for the low-level diagnostics UI). There are two port-related
scenarios that can cause Workbench to be unavailable:

1.  The port for the UI you are trying to access is blocked by
    network-level or operating-system-level firewall rules. Time to talk
    to your friendly network administrator.

2.  Either port is taken by other processes (e.g. a popular virus
    scanning application on Microsoft Windows often uses port 8081).

    -   Workbench may appear to start but the browser will fail to get a
        response when you go to http://localhost:8080.

    -   You will need to change the conflicting port in Workbench's
        config.yml file in the MettleCI home directory.

    -   If this situation arises at the point that you are installing
        Workbench, its configuration wizard will be unavailable and you
        will need to configure Workbench manually. In this case, contact
        MettleCI Support and you will be provided with a template
        config.yml file and further instructions.

### Find out which ports are already in use

Sometimes an old execution of Workbench from a previous installation may
still be running and keeping the port open. Alternatively, a different
application definitely requires use of that port. Find out what is
already connected to the relevant port using the following methods:-

<img src="images/icons/grey_arrow_down.png" class="expand-control-image"
style="vertical-align:middle;" />Windows

Execute Powershell and run this command (replace 8080 which the
appropriate Port Number):-

``` powershell
PS C:\Users\Administrator> Get-Process -Id (Get-NetTCPConnection -LocalPort 8080).OwningProcess

Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName
-------  ------    -----      -----     ------     --  -- -----------
    431      43   793404     185376       7.45   2200   0 java
```

Note: ProcessName ‘java’ indicates MettleCI Workbench is probably
running.

<img src="images/icons/grey_arrow_down.png" class="expand-control-image"
style="vertical-align:middle;" />Unix

Execute the following `netstat` command (replace 8080 which the
appropriate Port Number). Then use `ps -ef` to find what process is
running as that pid:-

``` bash
$> sudo netstat -tulpn | grep LISTEN | grep 8080
tcp6       0      0 :::8080                 :::*                    LISTEN      2018/java
$> ps -ef | grep 2018
mciworkb  2018     1  0 04:31 ?        00:00:54 /bin/java -jar /opt/dm/mci/mettle-ui-1.0-1432.jar server /opt/dm/mci/config.yml
root     31582 31469  0 14:19 pts/2    00:00:00 grep --color=auto 2018
$>
```

### Check the status of the workbench service

<img src="images/icons/grey_arrow_down.png" class="expand-control-image"
style="vertical-align:middle;" />Windows

Open the Services application and verify that the Workbench service has
been installed, has been configured to start automatically, and is
running:

<img src="attachments/518979607/772931646.png" class="image-center"
loading="lazy" data-image-src="attachments/518979607/772931646.png"
data-height="50" data-width="737" data-unresolved-comment-count="0"
data-linked-resource-id="772931646" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="Screen Shot 2019-11-20 at 4.11.01 pm.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="518979607"
data-linked-resource-container-version="23"
data-media-id="881db233-e08c-4750-a900-719a5540675d"
data-media-type="file" />

<img src="images/icons/grey_arrow_down.png" class="expand-control-image"
style="vertical-align:middle;" />Unix

``` java
[user@host]$> sudo service dm-mettleci-workbench status        # You'll receive either

MettleCI Workbench is not running                              # This message, if the workbench service is running, or
/opt/dm/mci/METTLE_UI.pid dead but pidfile exists              # This message, if it's failed for some reason
```

### Verify your Service settings (Windows)

<img src="images/icons/grey_arrow_down.png" class="expand-control-image"
style="vertical-align:middle;" />Windows

Open a Windows Command window and run the `NSSM` tool shipped with your
MettleCI installation:

``` java
C:\> cd C:\dm\mci\nssm\win64
C:\dm\mci\nssm\win64> nssm edit "MettleCI Workbench"
```

This will display a dialog which will enable you to inspect and modify
the settings for your Window MettleCI Workbench service. Use this tool
to verify the values you provided at installation time.

<img src="attachments/518979607/1485668371.png" class="image-center"
loading="lazy" data-image-src="attachments/518979607/1485668371.png"
data-height="244" data-width="445" data-unresolved-comment-count="0"
data-linked-resource-id="1485668371" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20200212-115128.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="518979607"
data-linked-resource-container-version="23"
data-media-id="13ade786-a90e-446c-9474-ed7911639b2d"
data-media-type="file" />

If you need to make any changes click ‘Edit service’ to make them
permanent, then try restarting your MettleCI Workbench service:

<img src="attachments/518979607/1485668377.png" class="image-center"
loading="lazy" data-image-src="attachments/518979607/1485668377.png"
data-height="171" data-width="385" data-unresolved-comment-count="0"
data-linked-resource-id="1485668377" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20200212-115402.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="518979607"
data-linked-resource-container-version="23"
data-media-id="8a23bd4e-3aa2-4691-a3c3-090a906742e2"
data-media-type="file" />

### Check the MettleCI log

Inspect the contents of `/opt/dm/mci/mci.log` UNIX or
`D:\dm\mci\mci.log` WINDOWS . This may contain log messages which
provide guidance on what is going wrong.

### Verify your license file

Ensure your MettleCI license file is…

-   named correctly, and in the correct directory
    (`<METTLECI-HOME>/mettleci.lic`)

-   configured with permissions appropriate to make it readable by the
    account used to execute the service

-   referenced correctly in your `<METTLECI-HOME>/config.yaml` file

-   valid. Refer to the details in the email which provided you with
    your license file. Specifically…

    -   Has your license expired? Check the effective dates.

    -   Are other license constraints valid? e.g. does the MAC address
        of the host on which you are running the Workbench service match
        that embedded in your license?

### Verify your MettleCI configuration file

Run the following commands to verify your `config.yml` file, and then
try to start the Workbench service manually to provide further
opportunities for diagnostic output:

<img src="images/icons/grey_arrow_down.png" class="expand-control-image"
style="vertical-align:middle;" />Windows

``` java
# Where xxxx is your version of MettleCI Workbench...
C:\> java -jar <METTLE-HOME-DIRECTORY>\mettle-ui-1.0-xxxx.jar check <METTLE-HOME-DIRECTORY>\config.yml

then...

C:\> java -jar mettle-ui-1.0-SNAPSHOT.jar server <METTLE-HOME-DIRECTORY>\config.yml
```

<img src="images/icons/grey_arrow_down.png" class="expand-control-image"
style="vertical-align:middle;" />Unix

``` java
# Where xxxx is your version of MettleCI Workbench...
[user@host]$> java -jar <METTLE-HOME-DIRECTORY>/mettle-ui-1.0-xxxx.jar check <METTLE-HOME-DIRECTORY>/config.yml

then...

[user@host]$> java -jar <METTLE-HOME-DIRECTORY>/mettle-ui-1.0-xxxx.jar server <METTLE-HOME-DIRECTORY>/config.yml
```

### Manually run the Workbench Java application

If you have been unable to diagnose the issue with your Workbench
service, you can manually run the java command to start Workbench to
check if any of the output from the java command can help you identify
the issue.

The command should look something like this:

``` java
java -jar [WORKBENCH_JAR] server [WORKBENCH_CONFIG_FILE]
```

We recommend running this command as the user that usually would run the
Workbench service to recreate the same conditions and to avoid any
permissions issues in the future.

This is an example of what this will look like and what the output would
be if the port configured in the Workbench config file was already in
use:

``` java
[root@test1-engn mci]# java -jar mettle-ui-1.0-1234.jar server config.yml
java.lang.RuntimeException: java.io.IOException: Failed to bind to 0.0.0.0/0.0.0.0:8080
    at org.eclipse.jetty.setuid.SetUIDListener.lifeCycleStarting(SetUIDListener.java:229)
    at org.eclipse.jetty.util.component.AbstractLifeCycle.setStarting(AbstractLifeCycle.java:205)
    at org.eclipse.jetty.util.component.AbstractLifeCycle.start(AbstractLifeCycle.java:72)
    at io.dropwizard.cli.ServerCommand.run(ServerCommand.java:53)
    at io.dropwizard.cli.EnvironmentCommand.run(EnvironmentCommand.java:45)
    at io.dropwizard.cli.ConfiguredCommand.run(ConfiguredCommand.java:87)
    at com.datamigrators.mettle.setup.StartServerCommand.run(StartServerCommand.java:41)
    at io.dropwizard.cli.Cli.run(Cli.java:78)
    at io.dropwizard.Application.run(Application.java:94)
    at com.datamigrators.mettle.MettleApplication.main(MettleApplication.java:66)
Caused by: java.io.IOException: Failed to bind to 0.0.0.0/0.0.0.0:8080
    at org.eclipse.jetty.server.ServerConnector.openAcceptChannel(ServerConnector.java:349)
    at org.eclipse.jetty.server.ServerConnector.open(ServerConnector.java:310)
    at org.eclipse.jetty.setuid.SetUIDListener.lifeCycleStarting(SetUIDListener.java:216)
    ... 9 more
Caused by: java.net.BindException: Address already in use
    at sun.nio.ch.Net.bind0(Native Method)
    at sun.nio.ch.Net.bind(Net.java:433)
    at sun.nio.ch.Net.bind(Net.java:425)
    at sun.nio.ch.ServerSocketChannelImpl.bind(ServerSocketChannelImpl.java:223)
    at sun.nio.ch.ServerSocketAdaptor.bind(ServerSocketAdaptor.java:74)
    at org.eclipse.jetty.server.ServerConnector.openAcceptChannel(ServerConnector.java:345)
    ... 11 more
```

## Related articles

-   Page:

    <a
    href="/wiki/spaces/MCIDOC/pages/2116517897/The+MettleCI+Service+doesn%27t+automatically+start+after+a+reboot"
    data-linked-resource-id="2116517897" data-linked-resource-type="page"
    data-linked-resource-version="5">The MettleCI Service doesn't
    automatically start after a reboot</a>

-   Page:

    <a
    href="/wiki/spaces/MCIDOC/pages/518979607/The+Workbench+is+unreachable%2C+or+the+Workbench+service+won%27t+start"
    data-linked-resource-id="518979607" data-linked-resource-type="page"
    data-linked-resource-version="23">The Workbench is unreachable, or the
    Workbench service won't start</a>

-   Page:

    <a
    href="/wiki/spaces/MCIDOC/pages/745078910/No+permission+to+install+the+DataStage+Designer+MettleCI+menu+items"
    data-linked-resource-id="745078910" data-linked-resource-type="page"
    data-linked-resource-version="12">No permission to install the DataStage
    Designer MettleCI menu items</a>

-   Page:

    <a
    href="/wiki/spaces/MCIDOC/pages/488800735/A+Workbench+update+doesn%27t+appear+to+have+installed"
    data-linked-resource-id="488800735" data-linked-resource-type="page"
    data-linked-resource-version="5">A Workbench update doesn't appear to
    have installed</a>

-   Page:

    <a
    href="/wiki/spaces/MCIDOC/pages/2110357519/Force+Refreshing+your+Browser"
    data-linked-resource-id="2110357519" data-linked-resource-type="page"
    data-linked-resource-version="1">Force Refreshing your Browser</a>

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200526-233641.png](attachments/518979607/772964353.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" /> [Screen
Shot 2019-11-20 at 4.11.01 pm.png](attachments/518979607/772931646.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200212-115128.png](attachments/518979607/1485668371.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200212-115402.png](attachments/518979607/1485668377.png)
(image/png)  

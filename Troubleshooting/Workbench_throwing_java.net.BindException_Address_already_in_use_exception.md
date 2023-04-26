# Workbench throwing java.net.BindException: Address already in use exception

## Problem

Workbench is not able to start, and `java.net.BindException` is found in
`mci.log`

``` java
java.lang.RuntimeException: java.io.IOException: Failed to bind to 0.0.0.0/0.0.0.0:8080
    at org.eclipse.jetty.setuid.SetUIDListener.lifeCycleStarting(SetUIDListener.java:229)
    at org.eclipse.jetty.util.component.AbstractLifeCycle.setStarting(AbstractLifeCycle.java:205)
    at org.eclipse.jetty.util.component.AbstractLifeCycle.start(AbstractLifeCycle.java:72)
    at com.datamigrators.mettle.setup.SetupServerCommand$SetupImpl.run(SetupServerCommand.java:175)
    at com.datamigrators.mettle.setup.SetupServerCommand.run(SetupServerCommand.java:99)
    at com.datamigrators.mettle.setup.SetupServerCommand.run(SetupServerCommand.java:71)
    at com.datamigrators.mettle.setup.StartServerCommand.run(StartServerCommand.java:35)
    at io.dropwizard.cli.Cli.run(Cli.java:78)
    at io.dropwizard.Application.run(Application.java:94)
    at com.datamigrators.mettle.MettleApplication.main(MettleApplication.java:69)
Caused by: java.io.IOException: Failed to bind to 0.0.0.0/0.0.0.0:8080
    at org.eclipse.jetty.server.ServerConnector.openAcceptChannel(ServerConnector.java:349)
    at org.eclipse.jetty.server.ServerConnector.open(ServerConnector.java:310)
    at org.eclipse.jetty.setuid.SetUIDListener.lifeCycleStarting(SetUIDListener.java:216)
    ... 9 more
Caused by: java.net.BindException: Address already in use
    at sun.nio.ch.Net.bind0(Native Method)
    at sun.nio.ch.Net.bind(Net.java:461)
    at sun.nio.ch.Net.bind(Net.java:453)
    at sun.nio.ch.ServerSocketChannelImpl.bind(ServerSocketChannelImpl.java:222)
    at sun.nio.ch.ServerSocketAdaptor.bind(ServerSocketAdaptor.java:85)
    at org.eclipse.jetty.server.ServerConnector.openAcceptChannel(ServerConnector.java:344)
    ... 11 more
```

## Cause

The default port of workbench is 8080/8081, when a conflict in port is
found, the `java.net.BindException` will be thrown

## Resolution

Identify the ports used, and look for other processes that are using the
same port with netstat

``` java
sudo netstat -plten | grep 8080
```

(the sudo may or may not be required depending on whether your ID can
run netstat)

This will return results like

``` java
tcp6       0      0 :::8080                 :::*                    LISTEN      0          31457      1396/java
```

You can find out which process is using the same port by searching the
running processes via ps

``` java
ps -ef | grep 1396
```

You can either change the port of the conflicted process or change the
ports of workbench to resolve the `java.net.BindException`

To change the port of Workbench, refer to <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/588972035/Configuring+MettleCI+Workbench+to+use+a+Custom+Port+Number?src=search"
data-card-appearance="inline"
rel="nofollow">https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/588972035/Configuring+MettleCI+Workbench+to+use+a+Custom+Port+Number?src=search</a>

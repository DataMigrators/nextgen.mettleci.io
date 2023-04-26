# MettleCI CLI produces 'Failed to connect to host' error

# Symptom

Running a MettleCI CLI command (typically on a Windows client) which
attempts to connect to a DataStage Engine tier produces an error of the
following form:

``` java
Failed to connect to host
net.schmizz.sshj.userauth.UserAuthException: Exhausted available authentication methods
        at net.schmizz.sshj.SSHClient.auth(SourceFile:230)
        at net.schmizz.sshj.SSHClient.authPublickey(SourceFile:345)
        at net.schmizz.sshj.SSHClient.authPublickey(SourceFile:363)
        at com.datamigrators.mettle.sftp.commands.BaseRemoteCommand.execute(SourceFile:72)
        at com.datamigrators.mettle.shell.Shell.executeCommand(Shell.java:183)
        at com.datamigrators.mettle.shell.Shell.run(Shell.java:48)
        at com.datamigrators.mettle.shell.MainClass.main(MainClass.java:174)
Command failed.
```

# Cause

You don’t have the correct files and/or permissions in place for correct
SSH operation.

# Solution

See the guidance on SSH configuration on <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/2396487711/SSH+Configuration"
data-linked-resource-id="2396487711" data-linked-resource-version="8"
data-linked-resource-type="page">this page</a>.

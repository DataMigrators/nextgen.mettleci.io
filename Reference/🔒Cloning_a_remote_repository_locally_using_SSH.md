# 🔒Cloning a remote repository locally using SSH

When first configuring a MettleCI environments you will need to
initialise one or more Git repositories from repository templates
supplied with MettleCI. Some Git systems allow you to initialise a
repository by uploading a supplied zip file, or by uploading a zip
file’s contents directly using the Git system’s user interface. Many
systems, however, require you to initialise a repository by creating a
local clone of a remote repository and committing and pushing your
changes.

These remote repositories are typically accessed using either HTTP or
SSH. Some organizations may prohibit remote Git repositories from being
accessed using HTTP for security reasons. In these cases you will need
to configure your local Git client to use an SSH reference to the remote
repository. This page describes how to configure your local Git client
to use this SSH-based process.

You don’t need to do this when accessing a remote repository using SSH
from MettleCI Workbench!

Workbench will use the SSH key files specified in `config.yml` to
communicate with your Git instance. The `ssh-agent` does not feature in
this exchange.

# What is the SSH Agent?

`ssh-agent` is an SSH key manager which stores your SSH keys and
certificates in memory, unencrypted, ready for use by `ssh`. It saves
you from typing a passphrase every time you connect to a server and is
essential when SSH connections need to occur without human intervention.
The `ssh-agent` process runs in the background, separately from `ssh`,
and usually starts up the first time you run `ssh` after a reboot.

The SSH agent keeps private keys safe because:

-   It doesn’t write any key information to disk.

-   It doesn’t allow your private keys to be exported.

Private keys stored in the agent can only be used for one purpose:
signing a message.

# The SSH Add Command

The `ssh-add` command is your interface to the SSH agent, and is used to
add your private SSH key identities (typically from your `~/.ssh`
directory) to `ssh-agent` . When you run `ssh-add` without any
parameters it scans your home (`~`) directory for SSH keys with
recognised names and adds them to your agent. By default it looks for:

-   `~/.ssh/id_rsa`

-   `~/.ssh/id_ed25519`

-   `~/.ssh/id_dsa`

-   `~/.ssh/id_ecdsa`

Once you add keys, they will be used automatically by `ssh`.

#### `ssh-agent` and the macOS Keychain

The `ssh-agent` that ships with macOS can store the passphrase for keys
in the macOS Keychain which makes it even easier to re-add keys to the
agent after a reboot. Depending on your Keychain settings, you still may
need to unlock the keychain after a reboot. To store key passphrases in
the Keychain, run `ssh-add -K [key filename]`. Passphrases are usually
stored in the “Local Items” keychain. `ssh-agent` will use these stored
passphrases automatically as needed.

# Using the SSH Agent with MettleCI Workbench

The MettleCI Workbench installation process generates an SSH key pair
(`workbench.key` and `workbench.key.pub`) in your $**METTLE_HOME**
directory which can be used to authenticate Workbench against third
party hosts/services. To do this you need to execute two steps:

1.  Register the Workbench private key with your ssh-agent, and

2.  Register the Workbench public key with your destination (such as a
    Git Repository)

Note that you can generate and use your own SSH keys. MettleCI just
generates the `workbench` key pair for you as a convenience.

Before adding your key you should ensure that the relevant files and
directories have the correct file permissions

-   `.ssh` directory: `700 (drwx------)`

-   public key ( `workbench.key.pub` file): `644 (-rw-r--r--)`

-   private key ( `workbench.key` file): `600 (-rw-------)`

-   Your home directory (`~`) should not be writeable by the group or
    others - at most `755 (drwxr-xr-x)`

# Adding your SSH Key

To enable the following for Workbench, login as the user that runs the
MettleCI Workbench service (defined by the `DM_WORKBENCH_USER`
environment variable - typically set to `mciworkb`)

``` bash
# Start SSH Agent if it's not already running
$> eval "$(ssh-agent -s)"
Agent pid 34160

# Add your key to SSH Agent
$> ssh-add /opt/dm/mci/workbench.key
Identity added: /opt/dm/mci/workbench.key (/opt/dm/mci/workbench.key)

# List the keys currently managed by SSH Agent
$> ssh-add -l
4096 SHA256:E02/hedtoisN95mPnr4mZHugWpuq6gd6HSkg4lUGzfk /opt/dm/mci/workbench.key (RSA)
```

Note that if the permissions of your SSH key are too open you will
receive an error message:

``` bash
$> ssh-add /opt/dm/mci/workbench.key
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0644 for '/opt/dm/mci/workbench.key' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
$>
```

# Automating the use of ssh-agent

These instructions are for Unix-based DataStage Engines

## Automate `ssh-agent` startup

To enable the following for Workbench, login as the user that runs the
MettleCI Workbench service (defined by the `DM_WORKBENCH_USER`
environment variable - typically set to `mciworkb`)

If it’s not already there, add the following line to your startup script
(e.g. `~/.profile`):

``` java
[ -z "$SSH_AUTH_SOCK" ] && eval "$(ssh-agent -s)"
```

## Automate adding the keys

To enable the following for Workbench, login as the user that runs the
MettleCI Workbench service (defined by the `DM_WORKBENCH_USER`
environment variable - typically set to `mciworkb`)

SSH keys can also be automatically added upon their first usage by
adding the following line to your `~/.ssh/config` file:-

``` java
AddKeysToAgent yes
```

For more information on `~/.ssh/config` type `man ssh_config`.

# Testing Git Access for Workbench

Workbench will execute some or all of the following `git` commands as
part of it's operation, so the SSH Keys will be automatically added and
loaded:-

`git clone ssh://git@server:7999/as/repo.git`

`git push ssh://git@server:7999/as/repo.git`

`git pull ssh://git@server:7999/as/repo.git`

To test git access for Workbench, perform a `git clone` to a temporary
directory from the command line.

Login as the user that runs the MettleCI Workbench service (defined by
the `DM_WORKBENCH_USER` environment variable - typically set to
`mciworkb`)

Ensure that the Git Repository Server is reachable on Port 7999.

``` java
[root@test1171-engn ~]# su - mciworkb
Last login: Tue Jun  7 20:02:58 AEST 2022 on pts/0
Agent pid 6917
[mciworkb@test1171-engn ~]$ ll
total 0
drwxrwxr-x 2 mciworkb dstage  6 Jun  7 20:33 ds_logs
drwxrwxr-x 3 mciworkb dstage 23 Jun  7 20:18 istool_workspace
[mciworkb@test1171-engn ~]$
[mciworkb@test1171-engn ~]$ ssh-add /opt/dm/mci/workbench.key
Identity added: /opt/dm/mci/workbench.key (/opt/dm/mci/workbench.key)
[mciworkb@test1171-engn ~]$ ssh-add -l
4096 SHA256:E02/hedtoisN95mPnr4mZHugWpuq6gd6HSkg4lUGzfk /opt/dm/mci/workbench.key (RSA)
[mciworkb@test1171-engn ~]$ git clone ssh://git@testing.mettleci.io:7999/as/alan-sandbox.git
Cloning into 'alan-sandbox'...
remote: Enumerating objects: 13, done.
remote: Counting objects: 100% (13/13), done.
remote: Compressing objects: 100% (7/7), done.
remote: Total 13 (delta 1), reused 0 (delta 0)
Receiving objects: 100% (13/13), 21.12 KiB | 0 bytes/s, done.
Resolving deltas: 100% (1/1), done.
[mciworkb@test1171-engn ~]$ ll
total 0
drwxr-xr-x 4 mciworkb dstage 52 Jun  8 11:20 alan-sandbox
drwxrwxr-x 2 mciworkb dstage  6 Jun  7 20:33 ds_logs
drwxrwxr-x 3 mciworkb dstage 23 Jun  7 20:18 istool_workspace
[mciworkb@test1171-engn ~]$ rm -rf alan-sandbox/
[mciworkb@test1171-engn ~]$
```

If the above commands complete without error, then Git Access is
correctly configured.

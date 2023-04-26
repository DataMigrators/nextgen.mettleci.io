# Creating SSH keys manually

SSH (**S**ecure **SH**ell) is a generic term for a software package or
command which implements the
<a href="https://www.ssh.com/ssh/protocol/" rel="nofollow"><u>SSH
communications protocol</u></a> to enable secure system administration
and file transfers over insecure networks. It is used in nearly every
datacenter, in every larger enterprise.

An <a href="https://www.ssh.com/ssh/key/" rel="nofollow">SSH key</a> is
an access credential that fulfils a similar function to that of user
names and passwords. The keys are primarily used for automated processes
and for implementing single sign-on by system administrators and power
users. A key comes as a pair of files: a Public key (also known as an
Authorized key) and a private key (also know as an Identity key) .

Public keys are analogous to locks that the corresponding private key
can open. Private keys are used by an SSH client to authenticate itself
when logging into an SSH server and are analogous to physical keys that
can open one or more locks (Public keys).

Many components of MettleCI are integrated to third party systems using
SSH to avoid the need for various software components to repeatedly
prompt users for authentication credentials. Note that SSH keys RSA by
default, but can be generated using a number of different encryption
algorithms. The algorithm you choose will depending upon the system with
which you are trying to connect.

On 15th March 2022, for example, GitHub stoped accepting RSA and DSA
keys so you should generate a ECDSA key (demonstrated below).

------------------------------------------------------------------------

# Instructions - Windows

The easiest way to generate an SSH key on Window is to install a Git
client and use Git Bash to follow the same instructions as for Unix.

<img src="attachments/457900052/2298183726.png?width=210"
class="image-center" loading="lazy"
data-image-src="attachments/457900052/2298183726.png" data-height="472"
data-width="546" data-unresolved-comment-count="0"
data-linked-resource-id="2298183726" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20220905-112702.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="457900052"
data-linked-resource-container-version="13"
data-media-id="12cf6dbf-1c38-4692-9966-11022bf408b2"
data-media-type="file" width="210" />

------------------------------------------------------------------------

# Instructions - Unix

Here’s an example of creating and deploying an SSH key to avoid a
username/password prompt when connecting from one host (`localhost`, in
this example) to another (`remotehost`).

If you already have an SSH key, you can skip this step. DOn’t enter a
pass phrase if you want to use this key with third party systems like
Azure or GitHub.

``` java
# Generate a 2048-bit RSA key (Will NOT work with GitHub!)
$> ssh-keygen -t rsa -b 2048 -f mykey.rsa.key
Generating public/private rsa key pair.
# (blah blah blah)

# Or
# Generate a 521-bit RSA key (WILL work with GitHub!)
# Yes - 521-bytes (not 512) because (2^521)-1 is a prime number 
# See https://en.wikipedia.org/wiki/Elliptic-curve_cryptography
$> ssh-keygen -t ecdsa -b 521 -f mykey.ecdsa.key
Generating public/private ecdsa key pair.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in mykey.ecdsa.key
Your public key has been saved in mykey.ecdsa.key.pub
The key fingerprint is:
SHA256:mri4SXfnLwf77L8UmzFf4DOW0e/LODuV/cixmDOw7+Q johnmckeever@localhsot
The key's randomart image is:
+---[ECDSA 521]---+
|                 |
|                 |
|              .  |
|             . . |
|       S  .   = +|
|    . o.  o . .@o|
| . o + .o =.= ==+|
| . + o oo.*o=+B +|
|  +..   .B*=E*=o |
+----[SHA256]-----+

# Copy the public key of your computer to the trusted keys of the target server
localhost:~$ ssh-copy-id -i .ssh/mykey.ecdsa user@remotehost
user@remotehost's password: ••••••••
```

Note that the following steps are not required when using the generated
key with MettleCI Workbench.

Now try logging into the machine, with `ssh 'user@remotehost'` to verify
the keys we’ve added:

``` java
# Create the .ssh directory:
localhost:~$ mkdir ~/.ssh

# Set the right permissions:
localhost:~$ chmod 700 ~/.ssh

# Create the authorized_keys file:
localhost:~$ touch ~/.ssh/authorized_keys

# Set the right permissions:
localhost:~$ chmod 600 ~/.ssh/authorized_keys

# Verify
localhost:~$ ls ~/.ssh/authorized_keys
```

Finally check you can log in using your new key…

``` java
localhost:~$ ssh id@server
user@remotehost:~$ 
```

## Related articles

-   Page:

    <a
    href="/wiki/spaces/MCIDOC/pages/1035730972/Integrating+Azure+DevOps+Work+Item+Lookup+with+MettleCI+Workbench"
    data-linked-resource-id="1035730972" data-linked-resource-type="page"
    data-linked-resource-version="15">Integrating Azure DevOps Work Item
    Lookup with MettleCI Workbench</a>

-   Page:

    <a href="/wiki/spaces/MCIDOC/pages/716603405/Remote+Upload+Command"
    data-linked-resource-id="716603405" data-linked-resource-type="page"
    data-linked-resource-version="27">Remote Upload Command</a>

-   Page:

    <a href="/wiki/spaces/MCIDOC/pages/1109524556"
    data-linked-resource-id="1109524556" data-linked-resource-type="page"
    data-linked-resource-version="8">Workbench login error 'The URL is
    incorrect or is not trusted'</a>

-   Page:

    <a
    href="/wiki/spaces/MCIDOC/pages/458556297/Configuring+MettleCI+Workbench+to+use+HTTPS"
    data-linked-resource-id="458556297" data-linked-resource-type="page"
    data-linked-resource-version="56">Configuring MettleCI Workbench to use
    HTTPS</a>

-   Page:

    <a href="/wiki/spaces/MCIDOC/pages/784367633/Remote+Execute+Command"
    data-linked-resource-id="784367633" data-linked-resource-type="page"
    data-linked-resource-version="20">Remote Execute Command</a>

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200612-014247.png](attachments/457900052/805044233.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200612-014711.png](attachments/457900052/805109767.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200612-014818.png](attachments/457900052/805044243.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200612-015022.png](attachments/457900052/802422879.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200612-015402.png](attachments/457900052/805044249.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200612-015648.png](attachments/457900052/802422885.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220905-112702.png](attachments/457900052/2298183726.png)
(image/png)  

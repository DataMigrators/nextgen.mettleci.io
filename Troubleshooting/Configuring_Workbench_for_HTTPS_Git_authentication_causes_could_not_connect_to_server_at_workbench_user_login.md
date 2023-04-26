# Configuring Workbench for HTTPS Git authentication causes "could not connect to server" at workbench user login

# Symptom

When using Oracle Java and switching Workbench to use HTTPS Git
authentication from the standard SSH authentication, after changing the
config.yml to set httpsEnabled: true in the gitAuthentication section
(as follows)…

``` java
gitAuthentication:
  sshKey: "/opt/dm/mci/workbench.key"
  httpsProvider: "SunJSSE"
  httpsEnabled: true  
  httpsCredentialsStore:    
    type: "PKCS12"
    path: "/opt/dm/mci/.secrets/git-credentials.p12"    
    password: ${file:UTF-8:/opt/dm/mci/.secrets/git-credentials-keystore-password}
```

…then restarting Workbench, Workbench starts normally but fails to
authorise the user with a “Could not connect to server” message when
valid DataStage credentials are presented (login with invalid
credentials works as expected, the credentials are validated as failed
and logon is denied)  

<img src="attachments/2057666582/2057732109.png" class="image-left"
loading="lazy" data-image-src="attachments/2057666582/2057732109.png"
data-height="413" data-width="363" data-unresolved-comment-count="0"
data-linked-resource-id="2057732109" data-linked-resource-version="2"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="CouldNotConnectToServer.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="2057666582"
data-linked-resource-container-version="7"
data-media-id="d7b0219b-04ea-4e25-a8f7-245c4b8180fb"
data-media-type="file" />

Examining the log shows an error of the form

``` java
ERROR [2021-10-20 17:13:11,239] io.dropwizard.jersey.errors.LoggingExceptionMapper: Error handling a request: 748a1e294871f1f5
! java.security.InvalidKeyException: Illegal key size
! at javax.crypto.Cipher.checkCryptoPerm(Cipher.java:1039)
! at javax.crypto.Cipher.implInit(Cipher.java:805)
! at javax.crypto.Cipher.chooseProvider(Cipher.java:864)
! at javax.crypto.Cipher.init(Cipher.java:1396)
! at javax.crypto.Cipher.init(Cipher.java:1327)
! at com.datamigrators.mettle.utils.EncryptionHelper.encrypt(EncryptionHelper.java:50)
! at com.datamigrators.mettle.auth.AuthTokenFactory.buildSignature(AuthTokenFactory.java:71)
! ... 71 common frames omitted
! Causing: java.lang.RuntimeException: Failed to encrypt user secret key
! at com.datamigrators.mettle.auth.AuthTokenFactory.buildSignature(AuthTokenFactory.java:79)
! at com.datamigrators.mettle.auth.AuthTokenFactory.create(AuthTokenFactory.java:42)
! at com.datamigrators.mettle.resources.AuthenticationResource.doLogin(AuthenticationResource.java:78)
```

Switching back to httpEnabled: false resolves the login error but does
not allow non ssh access to git

# Cause

When Workbench is set up via the wizard, we create an encrypted keystore
to securely house each users credentials (user ID and password or PAT)
for the Git system, should the Workbench be configured to use https or
http. This keystore is described in the httpsCredentialsStore section of
the config.yml as seen above. The store is protected with an encryption
key that we save in a protected location. Oracle Java is not capable of
decrypting the store as we encrypt it with modern strength cyphers, but
Oracle Java by default has only weaker versions available.

# Solution

Switch Workbench from using Oracle Java to AdoptOpenJDK. AdoptOpenJDK
has more modern encryption and is compatible with the key strength we
use. See <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/488800406/Prerequisite+Java+Installation"
data-linked-resource-id="488800406" data-linked-resource-version="24"
data-linked-resource-type="page">Prerequisite Java Installation</a> for
instructions.  
  

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[CouldNotConnectToServer.png](attachments/2057666582/2057732119.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[CouldNotConnectToServer.png](attachments/2057666582/2057732109.png)
(image/png)  

---
layout: page
title: Configuring_MettleCI_Workbench_to_use_HTTPS
parent: Configuration
---

# Configuring MettleCI Workbench to use HTTPS

-   [Creating a Java KeyStore and SSL
    certificate](#ConfiguringMettleCIWorkbenchtouseHTTPS-CreatingaJavaKeyStoreandSSLcertificate)
    -   [Regenerating
        keys](#ConfiguringMettleCIWorkbenchtouseHTTPS-Regeneratingkeys)
-   [Enabling HTTPS support in the MettleCI Workbench
    config.yml](#ConfiguringMettleCIWorkbenchtouseHTTPS-EnablingHTTPSsupportintheMettleCIWorkbenchconfig.yml)
-   [Trusting your
    certificate](#ConfiguringMettleCIWorkbenchtouseHTTPS-Trustingyourcertificate)
    -   [Inspecting your
        certificate](#ConfiguringMettleCIWorkbenchtouseHTTPS-Inspectingyourcertificate)
    -   [Installing your
        certificate](#ConfiguringMettleCIWorkbenchtouseHTTPS-Installingyourcertificate)

# Creating a Java KeyStore and SSL certificate

MettleCI Workbench can be configured to expose ports over HTTP, HTTPS,
or both simultaneously at separate ports. Before configuring Workbench
to use HTTPS, a <a href="https://en.wikipedia.org/wiki/Java_KeyStore"
rel="nofollow">Java KeyStore</a> containing the HTTPS certificate must
be created first. Java KeyStores can be created and managed using the <a
href="https://docs.oracle.com/javase/8/docs/technotes/tools/unix/keytool.html"
rel="nofollow">keytool</a> command included with all installations of
Java.

First ensure that you use the keytool command shipped with the
<a href="Prerequisite_Java_Installation"
data-linked-resource-id="488800406" data-linked-resource-version="24"
data-linked-resource-type="page">Java v1.8 package you downloaded to
support MettleCI</a>. You can check which version of `keytool` is your
command line's default by using the operating system-specific commands
`where keytool` WINDOWS or `which keytool` UNIX. Verify that the
response indicates that you will be using the keytool in the correct bin
directory (e.g. in your OpenJDK installation).

Next, you’ll use the `keytool` command (with a format like that show
below) to create a KeyStore that contains a single, basic, self-signed
certificate:

``` bash
keytool -genkey -keyalg RSA -alias workbench -keystore <path-to-keystore> 
        -storepass <store-password> -storetype PKCS12 -keysize 2048 
        -sigalg SHA256withRSA -dname "CN=<host url>"
        -ext san=dns:<host url>
        -validity <days-valid>
```

Use the following table to replace the `<placeholder-values>` in this
example command with values that are specific to your environment and
policies.

<table class="confluenceTable" data-layout="default"
data-local-id="1d3be04e-353d-4bcd-bf8d-9b6a018dda30">
<tbody>
<tr class="header">
<th class="confluenceTh"><p><strong>Placeholder</strong></p></th>
<th class="confluenceTh"><p><strong>Description</strong></p></th>
<th class="confluenceTh"><p><strong>Example Value</strong></p></th>
</tr>
&#10;<tr class="odd">
<td class="confluenceTd"><p>path-to-keystore</p></td>
<td class="confluenceTd"><p>Full qualified path of the key store to be
created</p></td>
<td class="confluenceTd"><p><code>/opt/dm/mci/workbench.p12</code>
(Unix)</p>
<p><code>C:\dm\mci\workbench.p12</code> (Windows)</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>store-password</p></td>
<td class="confluenceTd"><p>Password required when reading or writing to
the newly created key store</p></td>
<td class="confluenceTd"><p>Choose a random password string.</p>
<p>Note that the key stores supplied with Java have a default password
of <code>changeit</code>.</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>host-url</p></td>
<td class="confluenceTd"><p>The domain name of the URL that will be used
to access Workbench in your browser. This does not include the protocol
or port numbers. For example,
<code>dev-engine.datamigrators.com</code></p></td>
<td class="confluenceTd"><p><code>your-engine.yourdomain.com</code></p>
<p>(no port number)</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>days-valid</p></td>
<td class="confluenceTd"><p>The number of days for which the key should
remain valid</p></td>
<td class="confluenceTd"><p>Note that the key stores supplied with Java
have a default validity of 180 days.</p></td>
</tr>
</tbody>
</table>

For example, this command creates a keystore called `workbench.p12` in
the MettleCI home directory for use with workbench currently accessed at
URL `http://my-engine.datamigrators.com:8080`:

This example generates a key with a 10-year validity.

``` bash
$> keytool -genkey -keyalg RSA -alias workbench -keystore workbench.p12 \
-storepass changeit -storetype PKCS12 -keysize 2048 \
-sigalg SHA256withRSA -dname "CN=my-engine.datamigrators.com" \
-ext san=dns:my-engine.datamigrators.com \
-validity 3650
```

Note that in the example above you must ensure that both instances of
`engine.datamigrators.com` are replaced with the domain name of
***your*** DataStage engine. It is suggested that you use the Workbench
URL to derive this (e.g. `mydsengine.acmesandwichmakers.com`).

You can verify your keystore by listing the certificates within it.
You’ll need to re-enter your keystore password, which is 'changeit' (no
quotes) in our example.

``` java
keytool -list -v -keystore workbench.p12 -storetype PKCS12
Enter keystore password: ********
```

If you need to export your certificate for signing you can use a command
like the following:

``` java
keytool -certreq -keyalg RSA -alias workbench -keystore workbench.p12
-storepass changeit -sigalg SHA256withRSA -file C:\dm\mci\workbench.csr 
```

Note that with the exception of `keytool -list` the `keytool` command
will not normally return a value to the console to indicate it has
executed successfully

## Regenerating keys

If you want to regenerate your keystore certificate for any reason (i.e.
it has expired) you can use the following command:

``` java
# Delete it
$> keytool -delete -noprompt -alias workbench  -keystore workbench.p12  -storepass changeit

# Verify it has been deleted 
$>  keytool -list -v -keystore  /opt/dm/mci/workbench.p12  -storetype PKCS12  -storepass changeit
Keystore type: PKCS12
Keystore provider: SunJSSE

Your keystore contains 0 entries
$>
```

------------------------------------------------------------------------

# Enabling HTTPS support in the MettleCI Workbench `config.yml`

Once a keystore containing the Workbench HTTPS certificate has been
created, update your MettleCI `config.yml` file to add the following
section:

``` java
server:
  applicationConnectors:
    - type: https
      port: 8443
      keyStoreType: PKCS12
      keyStorePath: <path-to-keystore>
      keyStorePassword: <store-password>
      trustStoreType: PKCS12
      trustStorePath: <path-to-keystore>
      trustStorePassword: <store password>
```

The `<placeholder-values>` must match those used while creating the Java
keystore. For example:

<img src="images/icons/grey_arrow_down.png" class="expand-control-image"
style="vertical-align:middle;" />Windows

``` java
server:
  applicationConnectors:
    - type: https
      port: 8443
      keyStoreType: PKCS12
      keyStorePath: C:\dm\mci\workbench.p12
      keyStorePassword: changeit
      trustStoreType: PKCS12
      trustStorePath: C:\dm\mci\workbench.p12
      trustStorePassword: changeit
```

If you wish to allow Workbench to communicate over both HTTP and HTTPS
protocols then you configure your `config.yml` like this:

``` java
server:
  applicationConnectors:
    - type: http
      port: 8080
    - type: https
      port: 8443
      keyStoreType: PKCS12
      keyStorePath: C:\dm\mci\workbench.p12
      keyStorePassword: changeit
      trustStoreType: PKCS12
      trustStorePath: C:\dm\mci\workbench.p12
      trustStorePassword: changeit
```

<img src="images/icons/grey_arrow_down.png" class="expand-control-image"
style="vertical-align:middle;" />Unix

``` java
server:
  applicationConnectors:
    - type: https
      port: 8443
      keyStoreType: PKCS12
      keyStorePath: /opt/dm/mci/workbench.p12
      keyStorePassword: changeit
      trustStoreType: PKCS12
      trustStorePath: /opt/dm/mci/workbench.p12
      trustStorePassword: changeit
```

If you wish to allow Workbench to communicate over both HTTP and HTTPS
protocols then you configure your `config.yml` like this:

``` java
server:
  applicationConnectors:
    - type: http
      port: 8080
    - type: https
      port: 8443
      keyStoreType: PKCS12
      keyStorePath: /opt/dm/mci/workbench.p12
      keyStorePassword: changeit
      trustStoreType: PKCS12
      trustStorePath: /opt/dm/mci/workbench.p12
      trustStorePassword: changeit
```

Ensure you use fully qualified references for your KeyStorePath and
TrustStorePath as relative references will not work.

For example, instead of `./workbench.p12` use
`/opt/dm/mci/workbench.p12`.

The ports given above are only examples, and you’re free to <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/588972035/Configuring+Workbench+to+use+a+custom+port+number"
rel="nofollow">use custom port numbers</a> as desired.

Once your changes are saved restart your Workbench service using the
Services utility WINDOWS or the commands below for UNIX.

``` bash
sudo service dm-mettleci-workbench stop
sudo service dm-mettleci-workbench start
```

Verify Workbench is up and running under HTTP and/or HTTPS by navigating
to `https://<host url>:8443` and/or `http://<host url>:8080` (as
appropriate) in your browser.

# Trusting your certificate

You will need your local browser to trust the certificate on your
DataStage engine tier. There will be slightly different processes for
this depending upon your chosen browser and whether or not you have
self-signed the certificate or used a CA.

## Inspecting your certificate

Typically, when you first connect to Workbench using HTTPS you will see
a certificate error in your browser. This may look like this…

<img src="attachments/458556297/774897758.png?width=340"
class="image-center" loading="lazy"
data-image-src="attachments/458556297/774897758.png" data-height="79"
data-width="692" data-unresolved-comment-count="0"
data-linked-resource-id="774897758" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20200528-032042.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="458556297"
data-linked-resource-container-version="56"
data-media-id="844e8e07-7ba5-49be-bcb8-cd6bf19e67b5"
data-media-type="file" width="340" />

or this…

<img src="attachments/458556297/775094422.png?width=340"
class="image-center" loading="lazy"
data-image-src="attachments/458556297/775094422.png" data-height="60"
data-width="468" data-unresolved-comment-count="0"
data-linked-resource-id="775094422" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20200528-065422.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="458556297"
data-linked-resource-container-version="56"
data-media-id="75b8abe9-cee2-4ea9-8ca4-2a72aa892aa3"
data-media-type="file" width="340" />

Click on the warning indicator ('Not secure' or ‘Certificate error’ in
these examples) and select **Certificate (not valid)**.

<img src="attachments/458556297/1035763793.png?width=204"
class="image-center" loading="lazy"
data-image-src="attachments/458556297/1035763793.png" data-height="1002"
data-width="651" data-unresolved-comment-count="0"
data-linked-resource-id="1035763793" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20200916-134929.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="458556297"
data-linked-resource-container-version="56"
data-media-id="6db6161c-a295-49a0-b5bd-4dab7b02030d"
data-media-type="file" width="204" />

This will present a certificate dialog which may or may not allow you to
install the certificate.

Before you install your certificate click on the **Details** tab and
look at the **Thumbprint algorithm** and **Thumbprint** values.

<img src="attachments/458556297/775061566.png?width=204"
class="image-center" loading="lazy"
data-image-src="attachments/458556297/775061566.png" data-height="548"
data-width="453" data-unresolved-comment-count="0"
data-linked-resource-id="775061566" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20200528-044454.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="458556297"
data-linked-resource-container-version="56"
data-media-id="cc0567fd-36ac-46ca-9e0c-339154899f94"
data-media-type="file" width="204" />

The **Thumbprint** value should match the appropriate value displayed by
the `keytool -list` command you entered when you first generated your
certificate keystore.

``` java
Certificate fingerprints:
  MD5:  86:6A:96:1E:29:19:45:F9:46:B9:E6:54:DD:D0:1D:6C
  SHA1: 11:A1:75:E2:71:AA:5D:C8:85:8A:BF:65:02:FC:09:2D:C7:41:CA:BC
  SHA256: 5C:3A:87:77:13:17:77:F8:7C:2F:8A:F4:48:0D:B6:61:31:92:91:B6:90:36:0B:4C:5B:BC:30:5F:EC:C1:CA:36
```

Once you’re happy that the thumbprint matches you can proceed to
installing your certificate.

## Installing your certificate

If **Install Certificate** is enabled then click it to install the
certificate into the *Trust Root Certification Authorities* store

<img src="attachments/458556297/774963273.png?width=204"
class="image-center" loading="lazy"
data-image-src="attachments/458556297/774963273.png" data-height="554"
data-width="454" data-unresolved-comment-count="0"
data-linked-resource-id="774963273" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20200528-055815.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="458556297"
data-linked-resource-container-version="56"
data-media-id="817f4572-000e-4c3d-8087-e806bed3c45f"
data-media-type="file" width="204" />

If **Install Certificate** is not enabled then select the **Details**
tab in the Certificate dialog then click **Copy to File**.

<img src="attachments/458556297/1284866096.png?width=204"
class="image-center" loading="lazy"
data-image-src="attachments/458556297/1284866096.png" data-height="1024"
data-width="814" data-unresolved-comment-count="0"
data-linked-resource-id="1284866096" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20201217-123039.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="458556297"
data-linked-resource-container-version="56"
data-media-id="8ca87633-e8f1-4265-83a3-fb5221b7ccd1"
data-media-type="file" width="204" />

1.  Start the Certificate Export Wizard by clicking **Next**, accept the
    default settings, enter a meaningful certificate name to export it
    to your local system, and click **Finish**. Now the certificate has
    been successfully exported to a file.

2.  In the Certificate Export Wizard success message, click **Finish**.

3.  In the Certificate dialog, click **OK**.

You can now follow your operating system’s process for importing the
certificate file into the *Trust Root Certification Authorities* store.

Ensure you restart your browser after installing your certificate!

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200528-032042.png](attachments/458556297/774897758.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200528-032121.png](attachments/458556297/772964630.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200528-032151.png](attachments/458556297/774897764.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200528-032230.png](attachments/458556297/774930533.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200528-044454.png](attachments/458556297/775061566.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200528-055815.png](attachments/458556297/774963273.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200528-065418.png](attachments/458556297/775094416.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200528-065422.png](attachments/458556297/775094422.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200916-134923.png](attachments/458556297/1035731083.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20200916-134929.png](attachments/458556297/1035763793.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20201215-223619.png](attachments/458556297/1282179073.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20201217-123039.png](attachments/458556297/1284866096.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20221121-190950.png](attachments/458556297/2350940193.png)
(image/png)  

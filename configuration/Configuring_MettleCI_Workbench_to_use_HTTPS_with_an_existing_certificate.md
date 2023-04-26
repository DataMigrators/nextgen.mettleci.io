---
layout: page
title: Configuring_MettleCI_Workbench_to_use_HTTPS_with_an_existing_certificate
parent: Configuration
---

# Configuring MettleCI Workbench to use HTTPS with an existing certificate

In <a href="Configuring_MettleCI_Workbench_to_use_HTTPS"
data-linked-resource-id="458556297" data-linked-resource-version="56"
data-linked-resource-type="page">Configuring MettleCI Workbench to use
HTTPS</a> we describe how to create and install a self signed
certificate. However, some organizations prefer use of a certificate
that has been signed by a CA (or can trace signatures to a root
certificate signed by a CA). There are many ways to create or obtain
such a certificate, and discussion of those ways is out of scope for
this documentation. Consulting the OpenSSL documentation may be helpful
if you are tasked with doing it yourself. Consulting with system
administrators, network administrators, or the security team may be
required to determine your organizational process for requesting a
certificate signed by a CA.

Some key points about certificates

-   Certificates come in many formats, which may or may not be
    interconvertible with the tools available to you. If you are
    requesting or creating one, using the PKCS#12 format will be
    convenient, as that is what is used in the enabling HTTPS examples.
    The file may be supplied or generated with a `.pfx` or `.p12 `file
    suffix, either will work.

-   You will need the keystore password for the certificate. This is
    stored in the `config.yml`file, either directly, or via indirection
    to a secrets repository

-   Checking the certificate to ensure it’s been signed, or that it is
    chained to a CA signed root before trying to use it may help you
    avoid problems. You can examine created or provided certificates by
    using` keytool`which will be available with your OpenJDK
    installation. Consult the keytool manpage documentation for details.

Once you have created or had one provided to you, and it is on the
server where MettleCI Workbench will be running, the installation
process is similar to that given in the referenced page, with some
differences as noted

-   Enable HTTPS support in workbench. See <a
    href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/458556297/Configuring+MettleCI+Workbench+to+use+HTTPS#Enabling-HTTPS-support"
    data-card-appearance="inline"
    rel="nofollow">https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/458556297/Configuring+MettleCI+Workbench+to+use+HTTPS#Enabling-HTTPS-support</a>

    -   You will need the absolute path to where the certificate is, the
        name can be anything but we suggest a meaningful name such as
        workbenchEntrustSigned.p12 (or whatever CA may apply in your
        case)

    -   You will also need the keystore password. it is possible to not
        have one at all, although this is not a good practice, and this
        may require an exception in the process you used to obtain your
        certificate.

    -   MettleCI typically uses the same certificate for both the
        keystore and the truststore so the information in the
        `applicationConnectors:`section will be duplicated for the two
        stores

    -   If you also want the `adminConnectors: `to be enabled

-   After you restart the server the instructions <a
    href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/458556297/Configuring+MettleCI+Workbench+to+use+HTTPS#Trusting-your-certificate"
    data-card-appearance="inline"
    rel="nofollow">https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/458556297/Configuring+MettleCI+Workbench+to+use+HTTPS#Trusting-your-certificate</a>
    explain how to import the certificate into browsers as necessary.
    Hhowever, if you have a certificate signed by a CA, or traceable to
    a root signed by a CA, you should not need to import things.

Once you have changed your configuration to use the new certificate, and
you have restarted workbench successfully (if it doesn’t start, check
your mci.log for errors) you can test the certificate by pointing your
browser to the https URL you’ve established, and then click on the left
“padlock” icon. For a valid certificate it looks something like this:
(Windows using Chrome, uses a grey closed padlock, but other OS and
browser combinations may present information differently) rather than
the “not secure” appearance show in the Trusting your Certificate
section.  

<img src="attachments/2209349666/2339536905?width=340"
class="image-left" loading="lazy"
data-image-src="attachments/2209349666/2339536905" data-height="682"
data-width="837" data-unresolved-comment-count="0"
data-linked-resource-id="2339536905" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="03990583-9607-4b9a-ad18-12021b3e4e87#media-blob-url=true&amp;id=fc70225a-51d5-448a-901e-c5c0f00a58a5&amp;contextId=43751&amp;collection="
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="2209349666"
data-linked-resource-container-version="6"
data-media-id="40576360-7024-498b-8708-f05182061992"
data-media-type="file" width="340" />

To see more details, click on “connection is secure” and you should see
something analogous to this

<img src="attachments/2209349666/2339569677?width=204"
class="image-left" loading="lazy"
data-image-src="attachments/2209349666/2339569677" data-height="277"
data-width="337" data-unresolved-comment-count="0"
data-linked-resource-id="2339569677" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="b06033ed-279b-4893-afaf-3725316da5f1#media-blob-url=true&amp;id=90f4f3e1-d99d-4eed-8ebb-536a191787fb&amp;contextId=43751&amp;collection="
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="2209349666"
data-linked-resource-container-version="6"
data-media-id="607fbafb-5930-4822-80af-4d7bde907f42"
data-media-type="file" width="204" />

With these tips in mind you can continue the process outlined in the
<a href="Configuring_MettleCI_Workbench_to_use_HTTPS"
data-linked-resource-id="458556297" data-linked-resource-version="56"
data-linked-resource-type="page">Configuring MettleCI Workbench to use
HTTPS</a> documentation section.

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[03990583-9607-4b9a-ad18-12021b3e4e87#media-blob-url=true&id=fc70225a-51d5-448a-901e-c5c0f00a58a5&contextId=43751&collection=](attachments/2209349666/2339536905)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[b06033ed-279b-4893-afaf-3725316da5f1#media-blob-url=true&id=90f4f3e1-d99d-4eed-8ebb-536a191787fb&contextId=43751&collection=](attachments/2209349666/2339569677)
(image/png)  

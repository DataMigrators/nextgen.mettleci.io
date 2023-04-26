# Workbench login fails with 'No appropriate protocol' error

# Problem

Attempting to login to the MettleCI Workbench user interface presents
the following error:

<img src="attachments/1953366240/1954283528.png?width=224"
class="image-center" loading="lazy"
data-image-src="attachments/1953366240/1954283528.png" data-height="238"
data-width="335" data-unresolved-comment-count="0"
data-linked-resource-id="1954283528" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20210806-020331.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="1953366240"
data-linked-resource-container-version="4"
data-media-id="f1790769-03ca-451b-ab75-19e54aa8e5d9"
data-media-type="file" width="224" />

> “Could not communicate with DataStage domain.
>
> No appropriate protocol (protocol is disabled or cipher suites are
> inappropriate); nested exception is:
>
> javax.net.ssl.SSLHandshakeException: No appropriate protocol (protocol
> is disabled or cipher suites are inappropriate).
>
> Please verify DataStage services tier is running and available.”

# Solution

To fix this issue…

1.  Login to the Engine Tier where the MettleCI Workbench Service is
    running.

2.  Open the
    file `/opt/IBM/InformationServer/ASBNode/eclipse/plugins/com.ibm.iis.client/iis.client.site.properties` for
    editing.

3.  Replace `com.ibm.iis.ssl.protocol=SSL_TLSv2 `with
    `com.ibm.iis.ssl.protocol=TLSv1.2`

    <img src="attachments/1953366240/1954218028.png" class="image-center"
    loading="lazy" data-image-src="attachments/1953366240/1954218028.png"
    data-height="446" data-width="936" data-unresolved-comment-count="0"
    data-linked-resource-id="1954218028" data-linked-resource-version="1"
    data-linked-resource-type="attachment"
    data-linked-resource-default-alias="image-20210806-021532.png"
    data-base-url="https://datamigrators.atlassian.net/wiki"
    data-linked-resource-content-type="image/png"
    data-linked-resource-container-id="1953366240"
    data-linked-resource-container-version="4"
    data-media-id="f4f58dab-8e68-4705-8e82-4bcca44ae958"
    data-media-type="file" />

4.  Save the edited file and <a
    href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/1954578453/Starting+Stopping+the+Monitoring+MettleCI+Workbench+Service"
    rel="nofollow">restart the MettleCI Workbench service</a>

# Explanation

Workbench connects to DataStage using IBM's `com.ibm.iis.client` Java
library.  However, this library relies on IBM-specific security
extensions which are old, insecure, and introduce issues with HTTPS
security features in the server/clients upon which the MettleCI
Workbench rely.  Workbench handles the inconsistencies inherent
in `com.ibm.iis.client` to make it compatible with modern Java
distributions, such as the recommended OpenJDK distribution. 

One problem Workbench handles is the way
that `com.ibm.iis.client` initiates HTTPS connections.  The
IBM `com.ibm.iis.client` library use a non-standard protocol identifier
hard-coded into its HTTPS negotiation process. The IBM JRE introduces a
proprietary protocol called `SSL_TLSv2` (which is not an HTTPS protocol
in the traditional sense) which by-passes standard Java security
negotiation processes and is specific to the IBM JRE. A standard JRE has
no knowledge of this protocol, and so it cannot be used. MettleCI
Workbench remaps this protocol to
either `TLSv1`, `TLSv1.1` or `TLSv1.2`.

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210806-020331.png](attachments/1953366240/1954283528.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210806-021532.png](attachments/1953366240/1954218028.png)
(image/png)  

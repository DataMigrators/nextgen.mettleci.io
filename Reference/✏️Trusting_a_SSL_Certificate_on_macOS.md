# ✏️Trusting a SSL Certificate on macOS

If the Workbench SSL certificate is not trusted you will see a prompt
alerting you about this.

<img src="attachments/2269511701/2269249544.png" class="image-center"
loading="lazy" data-image-src="attachments/2269511701/2269249544.png"
data-height="546" data-width="769" data-unresolved-comment-count="0"
data-linked-resource-id="2269249544" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20220802-064440.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="2269511701"
data-linked-resource-container-version="1"
data-media-id="a88a082a-9001-4bef-9fa4-7f3e99f9dd81"
data-media-type="file" />

Click the Not Secure text in the address bar and select the
**Certificate is not valid** (or similar) warning.

Note that the wording and format of this warning varies by browser.

<img src="attachments/2269511701/2269282317.png" class="image-center"
loading="lazy" data-image-src="attachments/2269511701/2269282317.png"
data-height="353" data-width="332" data-unresolved-comment-count="0"
data-linked-resource-id="2269282317" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20220802-064544.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="2269511701"
data-linked-resource-container-version="1"
data-media-id="fb851d36-d4b8-4ab3-8c88-40b297318009"
data-media-type="file" />

<img src="attachments/2269511701/2269511711.png" class="image-center"
loading="lazy" data-image-src="attachments/2269511701/2269511711.png"
data-height="354" data-width="402" data-unresolved-comment-count="0"
data-linked-resource-id="2269511711" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20220802-065512.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="2269511701"
data-linked-resource-container-version="1"
data-media-id="1b6517d3-994a-435b-b18d-ac161ef4f813"
data-media-type="file" />

<img src="attachments/2269511701/2269610003.png" class="image-center"
loading="lazy" data-image-src="attachments/2269511701/2269610003.png"
data-height="266" data-width="566" data-unresolved-comment-count="0"
data-linked-resource-id="2269610003" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20220802-064747.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="2269511701"
data-linked-resource-container-version="1"
data-media-id="06ea6948-c0f9-464d-9ba9-ce30442f9253"
data-media-type="file" />

 Drag and Drop the certificate icon and place the certificate on your
desktop.

You should see a new icon on your desktop after you release your mouse.

<img
src="https://support.pkware.com/home/sfd/files/15.7/39747881/39747887/1/1591901376191/Screen+Shot+2016-10-28+at+11.22.25+AM.png"
class="image-center"
data-image-src="https://support.pkware.com/home/sfd/files/15.7/39747881/39747887/1/1591901376191/Screen+Shot+2016-10-28+at+11.22.25+AM.png"
loading="lazy" width="340" />

 

Double Click the certificate on your desktop to add the certificate to
the System keychain. You will need to authenticate this action with an
administrator credential.

<img
src="https://support.pkware.com/home/sfd/files/15.7/39747881/39747883/1/1591901376145/4.png"
class="image-center"
data-image-src="https://support.pkware.com/home/sfd/files/15.7/39747881/39747883/1/1591901376145/4.png"
loading="lazy" width="340" />

 If Keychain Access does not automatically open, open the Application
Keychain Access.

Once it is open, navigate to the new certificate by selecting
Certificates on the left side menu, then finding the certificate in the
list.

Once you have found the certificate, double click the certificate to
load the details.

<img
src="https://support.pkware.com/home/sfd/files/15.7/39747881/39747884/1/1591901376156/6.png"
class="image-center"
data-image-src="https://support.pkware.com/home/sfd/files/15.7/39747881/39747884/1/1591901376156/6.png"
loading="lazy" width="340" />

 Expand the Trust section of the certificate and find the option:

"When using this certificate"

 

Mark this as "Always Trust".

 

Close the certificate details window.

<img
src="https://support.pkware.com/home/sfd/files/15.7/39747881/39747885/1/1591901376167/7.png"
class="image-center"
data-image-src="https://support.pkware.com/home/sfd/files/15.7/39747881/39747885/1/1591901376167/7.png"
loading="lazy" width="340" />

 

Upon closing the Window, you will need to verify and provide
Administrator credentials to confirm your change to trust the
certificate.

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220802-064440.png](attachments/2269511701/2269249544.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220802-064544.png](attachments/2269511701/2269282317.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220802-064747.png](attachments/2269511701/2269610003.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220802-065506.png](attachments/2269511701/2269937683.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220802-065512.png](attachments/2269511701/2269511711.png)
(image/png)  

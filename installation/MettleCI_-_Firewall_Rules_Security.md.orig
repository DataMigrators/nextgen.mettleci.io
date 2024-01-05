# MettleCI - Firewall Rules & Security

**NOTE**

-   MettleCI Workbench uses your existing Information Server
    authentication scheme so users login to Workbench using their
    DataStage Designer credentials.

-   If you wish to configure MettleCI to use HTTPS you can either use
    the self-signed certificate generated during the MettleCI Workbench
    installation, or provide one yourself.  We will work with you to
    describe how your certificate renewal process will work with
    MettleCI's components.  See IBM's page on <a
    href="https://www.ibm.com/support/knowledgecenter/en/SSZJPZ_11.7.0/com.ibm.swg.im.iis.found.admin.common.doc/topics/cert_truststore.html"
    rel="nofollow">Storing certificates for client applications</a>.

# Firewall Rules

<table class="confluenceTable" data-layout="full-width"
data-local-id="2591d251-cd27-4435-af5a-a357cbbc595b">
<tbody>
<tr class="header">
<th class="confluenceTh"><p>Host</p></th>
<th class="confluenceTh"><p>Component</p></th>
<th class="confluenceTh"><p>Windows Service Name</p></th>
<th class="confluenceTh"><p>External Port</p></th>
<th class="confluenceTh"><p>Internal Port</p></th>
<th class="confluenceTh"><p>Comment</p></th>
</tr>
&#10;<tr class="odd">
<td class="confluenceTd"><p>MettleCI Agent Host</p></td>
<td class="confluenceTd"><p>Build Agent</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>As
required</p></td>
<td class="confluenceTd" data-highlight-colour="#f0f0f0"><p>n/a</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>As
required</p></td>
<td class="confluenceTd"><p><br />
</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>MettleCI Agent Host</p></td>
<td class="confluenceTd"><p>DataStage Designer Client</p></td>
<td class="confluenceTd" data-highlight-colour="#f0f0f0"><p>n/a</p></td>
<td class="confluenceTd" data-highlight-colour="#f0f0f0"><p>n/a</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>As
required</p></td>
<td class="confluenceTd"><p>Interfacing MettleCI to Information Server
via whichever port you are currently using for DataStage clients.  This
Designer Client is exclusively for MettleCI automated use
only.  Internal port is set based on customer standards, and/or as
required by IBM.</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>MettleCI Agent Host</p></td>
<td class="confluenceTd"><p>Windows Remote Desktop</p></td>
<td class="confluenceTd"><p>Remote Desktop Services</p></td>
<td class="confluenceTd"><p>3389 (default)</p></td>
<td class="confluenceTd" data-highlight-colour="#f0f0f0"><p>n/a</p></td>
<td class="confluenceTd"><p>As required by your organisation<br />
</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>DataStage Development
<strong>Engine</strong> Tier</p></td>
<td class="confluenceTd"><p>MettleCI Workbench</p></td>
<td class="confluenceTd"><p>MettleCI Workbench</p></td>
<td class="confluenceTd"><p>8080 &amp; 8081</p></td>
<td class="confluenceTd"><p>8080 &amp; 8081</p></td>
<td class="confluenceTd"><p>Browser-based user interface for Unit Test
specification and results, Compliance invocation, and Git check in. Note
that these ports are configurable.  Port 8081 is required only for the
exposure of MettleCI diagnostic output.</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>DataStage Development
<strong>Engine</strong> Tier</p></td>
<td class="confluenceTd"><p>Installation access</p></td>
<td class="confluenceTd"><p>SSH</p></td>
<td class="confluenceTd"><p>22</p></td>
<td class="confluenceTd" data-highlight-colour="#f0f0f0"><p>n/a</p></td>
<td class="confluenceTd"><p>The Customer Engineer (who will perform the
installation and commissioning of MettleCI under our remote guidance)
will require port 22 (SSH) open on the DataStage Engine tier for the
duration of the installation process.</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>DataStage Development
<strong>Engine</strong> Tier</p></td>
<td class="confluenceTd"><p>Information Server processes</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>As
required</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>As
required</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>As
required</p></td>
<td class="confluenceTd"><p>As supported by O/S, configured by customer,
and/or required by IBM</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>DataStage Development
<strong>Engine</strong> Tier</p></td>
<td class="confluenceTd"><p>SSH server process</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>As
required</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>As
required</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>As
required</p></td>
<td class="confluenceTd"><p>As supported by O/S, configured by customer,
and/or required by IBM</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>DataStage Development
<strong>Services</strong> Tier</p></td>
<td class="confluenceTd"><p>Information Server processes</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>As
required</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>As
required</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>As
required</p></td>
<td class="confluenceTd"><p>As supported by O/S, configured by customer,
and/or required by IBM</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>DataStage Development
<strong>Services</strong> Tier</p></td>
<td class="confluenceTd"><p>Information Server Operations
Console</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>As
required</p></td>
<td class="confluenceTd"><p>9443 (default)</p></td>
<td class="confluenceTd"><p>9443 (default)</p></td>
<td class="confluenceTd"><p>As supported by O/S, configured by customer,
and/or required by IBM</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>DataStage Development
<strong>Services</strong> Tier</p></td>
<td class="confluenceTd"><p>Information Governance Catalog REST
API</p></td>
<td class="confluenceTd" data-highlight-colour="#e0f0ff"><p>As
required</p></td>
<td class="confluenceTd"><p>9443 (default)</p></td>
<td class="confluenceTd"><p>9443 (default)</p></td>
<td class="confluenceTd"><p>As supported by O/S, configured by customer,
and/or required by IBM</p></td>
</tr>
</tbody>
</table>

## Public Internet Access

Ideally, developers, testers, and any other MettleCI users should be
provided with unfiltered HTTP (port 80) and HTTPS (port 443) internet
access to the following domains **for installation support purposes
only**:

-   \*.<a href="http://mettleci.com" rel="nofollow">mettleci.com</a>
    (for access to the self-service
    <a href="https://upgrade.mettleci.com/" rel="nofollow">MettleCI Report
    Card</a>)

-   \*.<a href="http://mettleci.io" rel="nofollow">mettleci.io</a>
    (documentation and software downloads)

-   <a href="http://datamigrators.atlassian.net"
    rel="nofollow">datamigrators.atlassian.net</a> (support portal)

MettleCI itself <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/457933104/Do+any+MettleCI+components+require+internet+access"
rel="nofollow">does not access the internet</a>. 

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[MettleCI topology (simplified)
Copy.png](attachments/1109491891/1109491894.png) (image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[MettleCI topology (simplified) Copy](attachments/1109491891/1109491897)
(application/gliffy+json)  

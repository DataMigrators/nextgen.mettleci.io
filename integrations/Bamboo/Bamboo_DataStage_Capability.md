# Bamboo DataStage Capability

Bamboo build agents optionally possess attributes called <a
href="https://confluence.atlassian.com/bamboo/configuring-capabilities-289277148.html"
rel="nofollow">capabilities</a> which describe the functions they are
able to perform. An agent which is resident on a host which also
provides a database interface might poses a `database` capability, for
example. You can then optionally configure each of your build pipeline's
steps to only run using build agents which present the capabilities
necessary to execute that step.

MettleCI extends the default capabilities of Bamboo with
the **MettleCI - DataStage Capability Plugin** which installs a
`DataStage` capability. This allows you to identify which of your Bamboo
build agents are installed co-resident with a MettleCI Command Line
Interface, necessary to execute MettleCI-specific build pipeline steps.

## To configure a DataStage Capability

1.  Navigate to the **Server capabilities** configuration page.
    Typically at
    `http://<bamboo base URL>/bamboo/admin/agent/configureSharedLocalCapabilities.action`

2.  Click the 'Edit' option of an existing DataStage Capability, or
    click **Add Capability**.

3.  If you can't find the DataStage Capability type, check the add-on
    **MettleCI - DataStage Capability Plugin**
    (dm-capability-plugin.jar) has been installed and is enabled.

4.  Complete the following settings, then click **Save:**

<table class="confluenceTable" data-layout="default"
data-local-id="d4b264d9-7d33-4f02-9749-a6e874662a05">
<tbody>
<tr class="header">
<th colspan="2" class="confluenceTh"><p><em>Add Capability</em></p></th>
</tr>
&#10;<tr class="odd">
<th class="confluenceTh"><p><strong>Capability type</strong></p></th>
<td class="confluenceTd"><p>DataStage</p></td>
</tr>
<tr class="even">
<th class="confluenceTh"><p>Install Label</p></th>
<td class="confluenceTd"><p>A label to uniquely identify this DataStage
install</p></td>
</tr>
<tr class="odd">
<th class="confluenceTh"><p>Path</p></th>
<td class="confluenceTd"><p>The path to the DataStage client or engine
home directory<br />
 (e.g. <strong>'C:\IBM\InformationServer\Clients\Classic'</strong> or
<strong>'/opt/IBM/InformationServer/Server/DSEngine'</strong>)</p></td>
</tr>
</tbody>
</table>

<img src="attachments/116525745/116525818.png?width=550"
class="image-left" loading="lazy"
data-image-src="attachments/116525745/116525818.png" data-height="279"
data-width="1069" data-unresolved-comment-count="0"
data-linked-resource-id="116525818" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image2017-3-9_10-19-16.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="116525745"
data-linked-resource-container-version="14"
data-media-id="8444e7fd-0be0-4a5d-981b-c3be63d25fb2"
data-media-type="file" width="550" />

  

  

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2017-3-8_17-44-41.png](attachments/116525745/116525749.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2017-3-8_16-56-25.png](attachments/116525745/116525752.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2017-3-7_16-53-12.png](attachments/116525745/116525755.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2017-3-9_10-19-16.png](attachments/116525745/116525818.png)
(image/png)  

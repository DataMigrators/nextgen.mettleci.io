# Data Fabrication Functions - Address

<table class="confluenceTable" data-layout="default">
<tbody>
<tr class="header">
<th class="confluenceTh"><p><strong>Module</strong></p></th>
<th class="confluenceTh"><p><strong>Fabricator</strong></p></th>
<th class="confluenceTh"><p><strong>Description</strong></p></th>
<th class="confluenceTh"><p><strong>Parameters</strong></p></th>
<th class="confluenceTh"><p><strong>Notes</strong></p></th>
</tr>
&#10;<tr class="odd">
<td class="confluenceTd"><p>address</p></td>
<td class="confluenceTd"><p>city</p></td>
<td class="confluenceTd"><p>Generates a random localized city name. The
format string can contain any method provided by the MettleCI data
fabrication library wrapped in <code>{{}}</code>,
e.g. <code>{{name.firstName}}</code> in order to build the city
name.</p>
<p>If no format string is provided one of the following is randomly
used:</p>
<ul>
<li><p><code>{{address.cityPrefix}} {{name.firstName}}{{address.citySuffix}}</code></p></li>
<li><p><code>{{address.cityPrefix}} {{name.firstName}}</code></p></li>
<li><p><code>{{name.firstName}}{{address.citySuffix}}</code></p></li>
<li><p><code>{{name.lastName}}{{address.citySuffix}}</code></p></li>
</ul></td>
<td class="confluenceTd"><p><strong>format</strong> string</p></td>
<td class="confluenceTd"></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>address</p></td>
<td class="confluenceTd"><p>cityPrefix</p></td>
<td class="confluenceTd"><p>Return a random localized city
prefix</p></td>
<td class="confluenceTd"><p>-</p></td>
<td class="confluenceTd"></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>address</p></td>
<td class="confluenceTd"><p>citySuffix</p></td>
<td class="confluenceTd"><p>Return a random localized city
suffix</p></td>
<td class="confluenceTd"><p>-</p></td>
<td class="confluenceTd"></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>address</p></td>
<td class="confluenceTd"><p>country</p></td>
<td class="confluenceTd"><p>Return a random country name</p></td>
<td class="confluenceTd"><p>-</p></td>
<td class="confluenceTd"></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>address</p></td>
<td class="confluenceTd"><p>countryCode</p></td>
<td class="confluenceTd"><p>Return a random ISO country code</p></td>
<td class="confluenceTd"><p>-</p></td>
<td class="confluenceTd"></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>address</p></td>
<td class="confluenceTd"><p>county</p></td>
<td class="confluenceTd"><p>Return a random county name</p></td>
<td class="confluenceTd"><p>-</p></td>
<td class="confluenceTd"></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>address</p></td>
<td class="confluenceTd"><p>latitude</p></td>
<td class="confluenceTd"><p>Return a random latitude</p></td>
<td class="confluenceTd"><p><strong>max</strong> double default is
90</p>
<p><strong>min</strong> double default is -90</p>
<p><strong>precision</strong> number default is 4</p></td>
<td class="confluenceTd"><p><em>The function parameters are currently
disabled and will be made available in a forthcoming
release.</em></p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>address</p></td>
<td class="confluenceTd"><p>longitude</p></td>
<td class="confluenceTd"><p>Return a random longitude</p></td>
<td class="confluenceTd"><p><strong>max</strong> double default is
90</p>
<p><strong>min</strong> double default is -90</p>
<p><strong>precision</strong> number default is 4</p></td>
<td class="confluenceTd"><p><em>The function parameters are currently
disabled and will be made available in a forthcoming
release.</em></p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>address</p></td>
<td class="confluenceTd"><p>secondaryAddress</p></td>
<td class="confluenceTd"><p>Return a secondary address</p></td>
<td class="confluenceTd"><p>-</p></td>
<td class="confluenceTd"></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>address</p></td>
<td class="confluenceTd"><p>state</p></td>
<td class="confluenceTd"><p>Return a state</p></td>
<td class="confluenceTd"><p><strong>useAbbr</strong> boolean</p></td>
<td class="confluenceTd"><p><em>This function parameter is deprecated
and will be removed in a forthcoming release. Please use the stateAbbr
function instead.</em></p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>address</p></td>
<td class="confluenceTd"><p>stateAbbr</p></td>
<td class="confluenceTd"><p>Return a state abbreviation</p></td>
<td class="confluenceTd"><p>-</p></td>
<td class="confluenceTd"></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>address</p></td>
<td class="confluenceTd"><p>streetAddress</p></td>
<td class="confluenceTd"><p>Returns a random localized street
address</p></td>
<td class="confluenceTd"><p><strong>useFullAddress</strong>
boolean</p></td>
<td class="confluenceTd"></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>address</p></td>
<td class="confluenceTd"><p>streetName</p></td>
<td class="confluenceTd"><p>Returns a random localized street
name</p></td>
<td class="confluenceTd"><p>-</p></td>
<td class="confluenceTd"></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>address</p></td>
<td class="confluenceTd"><p>streetPrefix</p></td>
<td class="confluenceTd"><p>Returns a random street prefix</p></td>
<td class="confluenceTd"><p>-</p></td>
<td class="confluenceTd"></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>address</p></td>
<td class="confluenceTd"><p>streetSuffix</p></td>
<td class="confluenceTd"><p>Returns a random street suffix</p></td>
<td class="confluenceTd"><p>-</p></td>
<td class="confluenceTd"></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>address</p></td>
<td class="confluenceTd"><p>zipCode</p></td>
<td class="confluenceTd"><p>Returns a random localized zip or postal
code</p></td>
<td class="confluenceTd"><p>-</p></td>
<td class="confluenceTd"></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>address</p></td>
<td class="confluenceTd"><p>direction</p></td>
<td class="confluenceTd"><p>Return a direction</p></td>
<td class="confluenceTd"><p><strong>useAbbr</strong> boolean defaults to
false</p></td>
<td class="confluenceTd"><p><em>This function is currently disabled and
will be made available in a forthcoming release.</em></p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>address</p></td>
<td class="confluenceTd"><p>cardinalDirection</p></td>
<td class="confluenceTd"><p>Return a cardinal direction</p></td>
<td class="confluenceTd"><p>-</p></td>
<td class="confluenceTd"><p><em>This function is currently disabled and
will be made available in a forthcoming release.</em></p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>address</p></td>
<td class="confluenceTd"><p>ordinalDirectiopn</p></td>
<td class="confluenceTd"><p>Return a direction .</p></td>
<td class="confluenceTd"><p><strong>useAbbr</strong> boolean defaults to
false</p></td>
<td class="confluenceTd"><p><em>This function is currently disabled and
will be made available in a forthcoming release.</em></p></td>
</tr>
</tbody>
</table>

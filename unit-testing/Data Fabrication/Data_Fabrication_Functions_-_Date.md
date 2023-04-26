# Data Fabrication Functions - Date

<table class="confluenceTable" data-layout="default"
data-local-id="bd062b85-9d45-4e3b-b881-3e6ddc7f56a3">
<tbody>
<tr class="header">
<th class="confluenceTh"><p><strong>Module</strong></p></th>
<th class="confluenceTh"><p><strong>Fabricator</strong></p></th>
<th class="confluenceTh"><p><strong>Description</strong></p></th>
<th class="confluenceTh"><p><strong>Parameters</strong></p></th>
<th class="confluenceTh"><p><strong>Notes</strong></p></th>
</tr>
&#10;<tr class="odd">
<td class="confluenceTd"><p>date</p></td>
<td class="confluenceTd"><p>between</p></td>
<td class="confluenceTd"><p>Random date between two supplied
dates</p></td>
<td class="confluenceTd"><p><strong>from</strong>
(date<strong>,</strong> default is empty)</p>
<p><strong>to</strong> (date<strong>,</strong> default is empty</p></td>
<td class="confluenceTd"><p>If either parameter is empty the function
generates an error message.</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>date</p></td>
<td class="confluenceTd"><p>future</p></td>
<td class="confluenceTd"><p>Generates a random future date X years from
Y date, where X and Y are parameters.</p></td>
<td class="confluenceTd"><p><strong>years</strong>
(number<strong>,</strong> default is 1)</p>
<p><strong>refDate</strong> (date<strong>,</strong> default is
today)</p></td>
<td class="confluenceTd"></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>date</p></td>
<td class="confluenceTd"><p>month</p></td>
<td class="confluenceTd"><p>A random month name</p></td>
<td class="confluenceTd"><p><strong>abbr</strong>
(boolean<strong>,</strong> default is false)</p>
<p><strong>context</strong> (boolean<strong>,</strong> default is
false)</p></td>
<td class="confluenceTd"></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>date</p></td>
<td class="confluenceTd"><p>past</p></td>
<td class="confluenceTd"><p>Generates a random past date X years from Y
date, where X and Y are parameters.</p></td>
<td class="confluenceTd"><p><strong>years</strong>
(number<strong>,</strong> default is 1)</p>
<p><strong>refDate</strong> (date<strong>,</strong> default is
today)</p></td>
<td class="confluenceTd"></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p>date</p></td>
<td class="confluenceTd"><p>recent</p></td>
<td class="confluenceTd"><p>Generates a random past date a specified
number of days from the current date.</p></td>
<td class="confluenceTd"><p><strong>days</strong>
(number<strong>,</strong> default is 1)</p></td>
<td class="confluenceTd"></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p>date</p></td>
<td class="confluenceTd"><p>weekday</p></td>
<td class="confluenceTd"><p>A random weekday name</p></td>
<td class="confluenceTd"><p><strong>abbr</strong>
(boolean<strong>,</strong> default is true)</p>
<p><strong>context</strong> (boolean, default is true)</p></td>
<td class="confluenceTd"></td>
</tr>
</tbody>
</table>

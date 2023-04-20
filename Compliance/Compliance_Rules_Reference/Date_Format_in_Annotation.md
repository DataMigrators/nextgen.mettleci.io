---
layout: page
title: Date_Format_in_Annotation
parent: .
---

# Date Format in Annotation

|                  |                                                                                                                                         |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| **Rule name**    | Date Format in Annotation                                                                                                               |
| **Parallel Job** | Yes                                                                                                                                     |
| **Server Job**   | Yes                                                                                                                                     |
| **Job Sequence** | Yes                                                                                                                                     |
| **Description**  | Identify whether the a ‘Job Description’ annotation contains instances of particular arbitrary text. This example rule looks for dates. |

# Description

Identify whether the a ‘Job Description’ annotation contains instances
of particular arbitrary text. You can modify this rule to get it to seek
out any text your team wants to prevent passing compliance. This example
rule looks for text matching the following date formats:

<table class="confluenceTable" data-layout="default"
data-local-id="23ce791c-fcba-494b-9b35-283770951eb0">
<tbody>
<tr class="header">
<th class="confluenceTh"
data-highlight-colour="var(--ds-background-neutral, #F4F5F7)"><p><strong>Format</strong></p></th>
<th class="confluenceTh"
data-highlight-colour="var(--ds-background-neutral, #F4F5F7)"><p><strong>Description</strong></p></th>
</tr>
&#10;<tr class="odd">
<td class="confluenceTd"><p><code>YYYY-MM-DD</code></p>
<p><code>YYYY/MM/DD</code></p>
<p><code>YYYY MM DD</code></p>
<p><code>YYYY-MMM-DD</code></p>
<p><code>YYYY/MMM/DD</code></p>
<p><code>YYYY MMM DD</code></p>
<p><code>YYYY-MMMM-DD</code></p>
<p><code>YYYY/MMMM/DD</code></p>
<p><code>YYYY MMMM DD</code></p></td>
<td class="confluenceTd"><p>YYYY-MM-DD format</p>
<p>with <code>/</code>, <code>-</code>, as delimited</p>
<p> </p>
<p>Month format can be</p>
<p><code>MM</code> , <code>MMM</code>, <code>MMMM</code> or
<code>MON</code></p>
<p> </p>
<p><code>MMM</code> and <code>MMMM</code> are Excel Syntax</p></td>
</tr>
<tr class="even">
<td class="confluenceTd"><p><code>DD-MM-YYYY</code></p></td>
<td class="confluenceTd"><p>Similar to YYYY-MM-DD</p></td>
</tr>
<tr class="odd">
<td class="confluenceTd"><p><code>MM-DD-YYYY</code></p></td>
<td class="confluenceTd"><p>Similar to YYYY-MM-DD (common US date
format)</p></td>
</tr>
</tbody>
</table>

# Actions

Remove or alter the offending text.

# RDU-Backlog CSV Command ⛔️

This is available on request to certain MettleCI direct customer
opportunities at the sole discretion of Justin McCamish and John
McKeever.

This documentation page remains - with viewing restrictions enabled and
the ⛔️ icon - purely for reference by Data Migrators engineers.

**DO NOT CHANGE THE VIEWING RESTRICTIONS OF THIS PAGE!**

# Purpose

This command takes a JSON file delivered as part of the process of
generating a project Report Card and creates a backlog of associated
stories in Atlassian Jira to drive the work involved in migrating those
jobs to a new version of Information Server.  The tool can be used to
either load the Jira backlog live (using Jira's REST API) or create a
CSV file which can be shipped to your Jira Administrator who can import
it to generate a backlog.

# Syntax

<img src="attachments/430342145/457736193.png?width=340"
class="image-center" loading="lazy"
data-image-src="attachments/430342145/457736193.png" data-height="546"
data-width="1278" data-unresolved-comment-count="0"
data-linked-resource-id="457736193" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image2019-10-22_12-28-9.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="430342145"
data-linked-resource-container-version="21"
data-media-id="3358c2af-9957-46c7-a785-fa7c9b08dc85"
data-media-type="file" width="340" />

``` java
$> mettleci rdu-backlog csv
Expected a command
Usage: rdu-backlog [options] [command] [command options]
  Commands:
    csv
    Usage: csv [options]
        Options:
        * -output
             Location to write the CSV file to
        * -reportcard
             Location of report card JSON file
```

# Example

``` bash
$> mettleci rdu-backlog csv \
   -reportcard "report-card.json" \
   -output "backlog.csv"
```

By default, Jira Server has a default limit on issue imports of 250
issues. Due to the current implementation, this does not affect the api
command but it will be a problem when a user attempts to import the
generated CSV in Jira. This limit can be changed in Jira's Advanced
Settings (<a
href="http://testing.mettleci.io/jira/secure/admin/AdvancedApplicationProperties.jspa"
rel="nofollow">http://[JIRA_BASE_URL]/jira/secure/admin/AdvancedApplicationProperties.jspa</a>)
by changing the setting `jira.bulk.create.max.issues.per.import`.

  

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-6-28_15-5-40.png](attachments/430342145/430768149.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-6-28_15-16-50.png](attachments/430342145/430440490.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-6-28_17-18-8.png](attachments/430342145/430735403.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-7-3_13-39-41.png](attachments/430342145/431947807.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-10-22_12-28-9.png](attachments/430342145/457736193.png)
(image/png)  

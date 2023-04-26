# RDU-Backlog API command ⛔️

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

<img src="attachments/458522681/458522684.png?width=340"
class="image-center" loading="lazy"
data-image-src="attachments/458522681/458522684.png" data-height="546"
data-width="1278" data-unresolved-comment-count="0"
data-linked-resource-id="458522684" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image2019-10-22_12-28-9.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="458522681"
data-linked-resource-container-version="7"
data-media-id="2b478c61-35b2-4dc2-92cb-007cb5e93969"
data-media-type="file" width="340" />

``` java
$> mettleci.cmd rdu-backlog
Expected a command
Usage: rdu-backlog [options] [command] [command options]
  Commands:
    help
    Usage: help [options]

    api
    Usage: api [options]
        Options:
        * -jiraurl
             URL of the Jira Server instance
        * -password
             Jira password
        * -project
             Key of the Jira project
        * -reportcard
             Location of report card JSON file
        * -username
             Jira username
```

# Example

``` bash
$> shell rdu-backlog api \
   -reportcard "report-card.json" \
   -jiraurl "http://testing.mettleci.io/jira" -project "RBT" \
   -username "drew" -password "password"
```

  

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-10-22_12-28-9.png](attachments/458522681/458522684.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-7-3_13-39-41.png](attachments/458522681/458522687.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-6-28_17-18-8.png](attachments/458522681/458522690.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-6-28_15-16-50.png](attachments/458522681/458522693.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image2019-6-28_15-5-40.png](attachments/458522681/458522696.png)
(image/png)  

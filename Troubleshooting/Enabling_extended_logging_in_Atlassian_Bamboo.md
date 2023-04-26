# Enabling extended logging in Atlassian Bamboo

To help us investigate unexpected behaviour involving MettleCI functions
triggered by **Local** Bamboo Agents, take the following steps in the
Atlassian Bamboo Server GUI…

1.  Go to Bamboo’s menu **Administration → System → Log settings**.

2.  Add the relevant MettleCI Java class to Bamboo’s log4j-based logging
    list by...

    1.  putting
        “com.datamigrators.mettle.services.joboperation.DataStageJobLaunchOperation”
        (no quotes) in the Classpath field.

    2.  selecting “DEBUG" from the Type menu; and

    3.  clicking on the “Add” button.

3.  In the new entry that appears in the 'Edit current levels' table,
    check that the Current Level value is set to ‘DEBUG’. If not,
    correct it in New Level and click the Save button to the right.

4.  Run the CI Plan where the Unit Tests are exhibiting the issue.

5.  Get a copy of the resulting Bamboo Server
    log (BAMBOO_HOME/logs/atlassian-bamboo.log) and forward that to Data
    Migrators for diagnostics.

6.  Go to Bamboo’s menu **Administration → System → Log settings**.

7.  Remove the
    `com.datamigrators.mettle.services.joboperation.DataStageJobLaunchOperation`
    line by clicking ‘**Delete**’ on the relevant line in the '**Edit
    current levels**' table.

Bamboo doesn’t have to be restarted during these operations.

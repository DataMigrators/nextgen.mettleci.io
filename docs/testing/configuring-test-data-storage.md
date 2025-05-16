---
status: reviewed
owner: John McKeever
tags:
  - DATASTAGE
  - TESTING
---
# Configuring test data storage

## Create a connection

Start by creating a connection to a storage resource where test assets will be stored.

1. From the CPD Cluster home page open an existing project or create a new project then, on the **Assets** tab, click **New Asset** > **Connect to a data source**.
1. On the resulting page select one of the storage connection types supported by test cases and **Next**. Connection typesd currently supported as a DataStage test data connector are:
    - Storage volume,
    - Google Cloud Storage, 
    - IBM Cloud Object Storage,
    - Microsoft Azure Blob Storage, and 
    - Generic S3, which should be used instead of the **Amazon S3** connector which is **not supported**.

Using a **Storage volume** connection:

1. On the **Create connection: Storage volume** page give your new connection a name and optional description.
1. Select an available storage volume. If you don't already have an storage volume available ...
   - click **New volume**.
   - Select a namespace (the default will be fine).
   - Give your storage volume a name and optional description.
   - Select your preferred storage type and click **Add**.
1. Under **Personal credentials** > **Input method** select **Enter credentials manually**.
1. Check the **Use my platform login credentials** then click **Test connection**.
1. Assuming you have a successful connection, click **Save**.

When using one of the cloud object storage connectors (i.e. **not Storage Volume**) then see [the relevant documentation](https://www.ibm.com/docs/en/cloud-paks/cp-data/5.1.x?topic=data-supported-sources) for the connection type you selected.  Remember to verify your connection, by clicking **Test connection**, before clicking **Save**.

## Add the connection to your project settings

Next you'll configure DataStage® to use your test data connection for storing test case assets.

1. From the CPD Cluster home page select the **Manage** tab then, under **Tools**, select **DataStage** and then select the tab **Test cases**.
1. For **Test data connection type** select the type of test data storage connector you created in the step above.
1. For **Test data storage** select the name of your test data connection.
1. For **Default DataStage Test case job suffix** specify a suffix which will be appended to all test case jobs to help distinguish them in the job log from invocations of their associated flows. e.g. ` DataStage Test Case Job`. Note that you may wish to include a leading space as DataStage will not automatically add one for you.

## Sharing a test data connection across projects

Rather than creating individual test data connections for each of your projects you may prefer to share your test data connection across projects by adding it to the catalog.  This allows you to share the connection with other projects in your organization, making it easier to manage and maintain your test data connections.  Note that sharing test data connections in this way will not permit multiple projects to access each other's test data, despite them sharing an underlying storage mechanism. 

To share a test data connection using the catalog:

1. From your project asset browser select your test data connection asset and use the vertical overflow menu (![three vertical dots](../images/overflow-menu--vertical.svg "three vertical dots")) to select **Publish to catalog**.
1. On the resulting dialog select the **Platform assets catalog** and click **Next**.
1. On the next step of the wizard set any other preferences you wish and click **Next**.
1. Review your selections and click **Publish**. 
1. From the hamburger menu in the top left of the CPD interface, select **All catalogs** and then select the **Platform assets catalog**.
1. Use the vertical overflow menu (![three vertical dots](../images/overflow-menu--vertical.svg "three vertical dots")) alongside the connection you want to share and click **Add to project**.
1. Select the project with which you want to share the connection and click **Next** then **Add**.  Repeat this step for each project you want to share the connection with.  Note that you can only add a connection to a project if you have the **Project Admin** role in that project. 

Once you have configured a connection to a storage volume, you can use it to create test cases.  For more information see [Creating DataStage test cases](creating-datastage-test-cases.md).

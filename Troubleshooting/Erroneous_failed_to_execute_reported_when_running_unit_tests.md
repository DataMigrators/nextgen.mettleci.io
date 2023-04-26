# Erroneous "failed to execute" reported when running unit tests

## Problem

When running unit tests “failed to execute” is reported and the test
aborts with an exception similar to the following:

``` java
Failed to execute job 'jb_ext_eenr_acct_hist' for unit testing: 
com.datamigratorsmettle.services.dsexecute.RunnableJobException: 
Service operation failed when performing action 'jobruns/latest' for resource 
'jobdesigns/P1EHOWLD2601/CLR_ODS_DLY/Jobs/Extract/jb_ext_eenr_acct_hist'
at com.datamigrators.mettle.services.dsexecute.rest.RestRunnableJob.getLatestJobRun(SourceFile:298)
at com.datamigrators.mettle.services.dsexecute.rest.RestRunnableJob.executeJob(SourceFile:245
```

  
or in the results you may see an exception similar to the following:

``` java
Failed to execute job 'TR_ORDERS' for unit testing: com.datamigrators.mettle.services.dsexecute.RunnableJobException: Service operation failed when performing action 'jobruns/latest' for resource 'jobdesigns/DEMO4-ENGN.DATAMIGRATORS.IO/wwi_jenkins_ds117_ci/Jobs/Transform/TR_ORDERS'
at com.datamigrators.mettle.services.dsexecute.rest.RestRunnableJob.getLatestJobRun(SourceFile:298)
at com.datamigrators.mettle.services.dsexecute.rest.RestRunnableJob.executeJob(SourceFile:245)
at com.datamigrators.mettle.services.dsexecute.rest.RestRunnableJob.run(SourceFile:191)
at com.datamigrators.plugin.dstest.process.UnitTestRunner.call(SourceFile:115)
```

# Cause

The <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/718831617/UnitTest+Test+Command"
data-linked-resource-id="718831617" data-linked-resource-version="19"
data-linked-resource-type="page">Command</a> / <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/512163847/Run+DataStage+Unit+Tests+Task"
data-linked-resource-id="512163847" data-linked-resource-version="1"
data-linked-resource-type="page">Bamboo Task</a> for running Unit Tests
as part of a CI/CD pipeline is expected to run a lot of short lived
DataStage jobs in quick succession. To reduce the processing overhead
introduced by running a lot of concurrent instances of <a
href="https://www.ibm.com/docs/en/iis/11.7?topic=jobs-running-job-from-command-line"
rel="nofollow">dsjob</a>, MettleCI will attempt to use the <a
href="https://www.ibm.com/docs/en/iis/11.7?topic=panel-job-run-dialog"
rel="nofollow">DataStage Operations Console</a> API. When the DataStage
Operations Console is unavailable or disabled, MettleCI will execute
Unit Tests using the less efficient `dsjob` command.

If DataStage Operations Console is enabled but not fully functioning,
eg. there are one or more services not running, the responses MettleCI
receives during a job execution will be inconsistent, and will result in
exceptions like those shown above.

# Solution

<a
href="https://www.ibm.com/docs/en/iis/11.7?topic=processes-starting-stopping-appwatcher-process"
rel="nofollow">Restarting the Operations Console AppWatcher</a> will
address this issue while the Operations Console continues to operate
nominally. If this issue reoccurs then you should investigate the
reasons for your Operations Console’s unreliability.

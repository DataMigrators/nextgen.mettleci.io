# Enabling debug logging for MettleCI CLI

The MettleCI Command Line Interface has a debugging mode which is
enabled by inserting entries in a configuration file:

In the root directory of your CLI installation (e.g. `/opt/dm/mci/cli`
UNIX or `C:\MettleCI\cli` WINDOWS) you will see the file
`config.properties`.

Update the file to contain the following entries:

``` java
# Setting the log level for a specific logger takes the format:
#     logger.[LOG_NAME]=[LOG_LEVEL]

logger.com.datamigrators.mettle.process.CommandRunner=DEBUG
logger.com.datamigrators.mettle.dsadmin.commands.DSParamsMergeCommand=DEBUG
```

These entries will create a log file under your CLI install directory in
the sub-directory file `log/stdout.log`. In the event of a support
request you may be asked to download this file and forwarded it to
MettleCI support for analysis.

#### Available Debug Loggers

|                                                                         |                                                                                             |
|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| **Logger**                                                              | **Enhanced Logging Provided**                                                               |
| `logger.com.datamigrators.mettle.process.CommandRunner`                 | Logs the external calls made to DataStage APIs                                              |
| `logger.com.datamigrators.mettle.dsadmin.commands.DSParamsMergeCommand` | Logs details of differences (sections and entries) calculated by the DSParams Merge Command |
| `logger.com.datamigrators.mettle.dsadmin.commands.DSParamsDiffCommand`  | Logs sections and entries merged by the DSParams Diff Command                               |

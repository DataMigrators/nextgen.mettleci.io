# ISX Import Command

## Purpose

Imports the contents of ISX files underneath a defined location into a
DataStage project.  Incremental imports can be performed by including
the `-project-cache` parameter.

See <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/1266843717/Repeatable+DataStage+Project+Deployments"
data-linked-resource-id="1266843717" data-linked-resource-version="8"
data-linked-resource-type="page">Repeatable DataStage Project
Deployments</a> for more details on how the `-project-cache` parameter
is used to implement **incremental imports**. For more information on
using the `-project-cache` parameter see our <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/1356890161/MettleCI+CLI+and+the+project-cache+directory"
rel="nofollow">detailed explanation</a>.

Note that the `isx import` commands requires access to a
correctly-functioning `istool` command and so is only executable on a
Windows-based DataStage Client Tier.

# Syntax

# Examples

## Import all jobs from a given directory

``` bash
$> mettleci isx import \
   -domain test2-svcs.datamigrators.io:59445 \
   -username myuser -password mypassword \
   -server test2-engn.datamigrators.io \
   -project myproject \
   -location /tmp/isx_location

Analyzing test2-engn.datamigrators.io/myproject
Optimising assets for import
Attempting to import with 1 working threads.
Importing DataStage assets...
 * Import 'test2-engn.datamigrators.io/myproject/Jobs/Load/LD_SALE.pjb' - COMPLETED
 * Import 'test2-engn.datamigrators.io/myproject/Jobs/Load/LD_STOCK_HOLDING.pjb' - COMPLETED
 * Import 'test2-engn.datamigrators.io/myproject/Jobs/Load/LD_STOCKITEM.pjb' - COMPLETED
 * Import 'test2-engn.datamigrators.io/myproject/Jobs/Load/LD_SUPPLIER.pjb' - COMPLETED
Import complete
```

## Incrementally import project binaries only

This example incrementally imports project binaries, ignoring Job design
information. Any Jobs in the project which do not exist in the source
directory are deleted from the project.  `C:/shared/myproject/export` is
a directory containing ISX files (with binaries) to be imported and
`C:/shared/myproject/cache` contains *state* files related to
incremental operations performed against `myproject`:

``` bash
$> mettleci.cmd isx import \
   -domain test2-svcs.datamigrators.io:59445 \
   -username myuser -password mypassword \
   -server test2-engn.datamigrators.io \
   -project myproject \
   -location c:/shared/myproject/export \
   -exclude-designs \
   -project-cache c:/shared/myproject/cache

Analyzing test2-engn.datamigrators.io/myproject
Attempting to identify changes with 4 working threads.
Inspecting DataStage assets for changes...
 * Check test2-engn.datamigrators.io/myproject/Jobs/Transform/TR_MOVEMENT.pjb - COMPLETED
 * Check test2-engn.datamigrators.io/myproject/Jobs/Load/LD_TRANSACTION_TYPE.pjb - COMPLETED
<SNIP>
 * Check test2-engn.datamigrators.io/myproject/Jobs/ParameterSets/pDMSqlServer_DW.pst - COMPLETED
 * Check test2-engn.datamigrators.io/myproject/Jobs/ParameterSets/pGlobal.pst - COMPLETED
Change identification complete
Deleting assets...
 * Delete 'test2-engn.datamigrators.io/myproject/Jobs/Transform/TR_ORDERS.pjb' - COMPLETED
 * Delete 'test2-engn.datamigrators.io/myproject/Jobs/Transform/TR_PURCHASE.pjb' - COMPLETED
Deletion complete
Optimising assets for import
Attempting to import with 1 working threads.
Importing DataStage assets...
 * Import 'test2-engn.datamigrators.io/myproject/Jobs/Transform/TR_PURCHASE.pjb' - COMPLETED
 * Import 'test2-engn.datamigrators.io/myproject/Jobs/Transform/TR_ORDERS.pjb' - COMPLETED
Import complete
Attempting to identify last change with 4 working threads.
Inspecting DataStage assets for last change...
 * Check test2-engn.datamigrators.io/myproject/Jobs/ParameterSets/pDMSqlServer_OLTP.pst - COMPLETED
 * Check test2-engn.datamigrators.io/myproject/Jobs/ParameterSets/pDMSqlServer_DW.pst - COMPLETED
<SNIP>
 * Check test2-engn.datamigrators.io/myproject/Jobs/Load/LD_EMPLOYEE.pjb - COMPLETED
 * Check test2-engn.datamigrators.io/myproject/Jobs/Load/LD_STOCKITEM.pjb - COMPLETED
Last change identification complete
```

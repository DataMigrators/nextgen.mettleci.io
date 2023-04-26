# ISX Export Command

# Purpose

Exports DataStage Assets to ISX files, one file per Asset. This adds a
number of capabilities over the IBM-supplied commands, including…

-   Support for high-performance multi-threaded operation (using the
    `-threads` switch)

-   Support for incremental exports (using the `-project-cache`
    parameter)

See <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/1266843717"
rel="nofollow">Repeatable DataStage Project Deployments</a> for more
details on how the `-project-cache` parameter is used to implement
**incremental exports**. For more information on using the
`-project-cache` parameter see our <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/1356890161/MettleCI+CLI+and+the+project-cache+directory"
rel="nofollow">detailed explanation</a>.

Note that the `isx export` commands requires access to a
correctly-functioning `istool` command and so is only executable on a
Windows-based DataStage Client Tier.

# Syntax

# Examples

## Export by regex usage

Export a subset of a project using the `-jobname` parameter which
accepts a <a href="https://en.wikipedia.org/wiki/Regular_expression"
rel="nofollow">regular expression</a> filter.

The export location is structured to mirror the structure of your
DataStage repository. In the example below we use a `-jobname` filter to
select a set of jobs in the `/Jobs/Load` category of our DataStage
project. The `isx export` command mirrors this be creating our exported
ISX files in a `/Jobs/Load` folder which it creates during the export
process.

``` plain
# Export our ISX files

C:\MettleCI\cli> mettleci isx export ^
     -domain myteam-svcs.corp.com:59445 ^
     -username myuser -password mypassword ^
     -server myteam-engn.corp.com ^
     -project myproject ^
     -jobname .*LD_S.*
Exporting [.*LD_S.*] from repository...
Exporting DataStage assets...
 * Export 'myteam-engn.corp.com/myproject/Jobs/Load/LD_SUPPLIER.pjb' - COMPLETED
 * Export 'myteam-engn.corp.com/myproject/Jobs/Load/LD_STOCK_HOLDING.pjb' - COMPLETED
 * Export 'myteam-engn.corp.com/myproject/Jobs/Load/LD_STOCKITEM.pjb' - COMPLETED
 * Export 'myteam-engn.corp.com/myproject/Jobs/Load/LD_SALE.pjb' - COMPLETED
Export complete

# See the created Jobs directory

c:\MettleCI\cli>dir
 Volume in drive C has no label.
 Volume Serial Number is 8C74-3344

 Directory of c:\MettleCI\cli

15/09/2022  07:29 PM    <DIR>          .
15/09/2022  07:29 PM    <DIR>          ..
15/09/2022  07:29 PM    <DIR>          <SNIP>
15/09/2022  07:29 PM    <DIR>          Jobs
               8 File(s)          9,555 bytes
               8 Dir(s)  15,827,730,432 bytes free

# ... sub-directory

c:\MettleCI\cli>dir Jobs
 Volume in drive C has no label.
 Volume Serial Number is 8C74-3344

 Directory of c:\MettleCI\cli\Jobs

15/09/2022  07:29 PM    <DIR>          .
15/09/2022  07:29 PM    <DIR>          ..
15/09/2022  07:29 PM    <DIR>          Load
               0 File(s)              0 bytes
               3 Dir(s)  15,827,730,432 bytes free

# ... and our ISX files

c:\MettleCI\cli>dir Jobs\Load
 Volume in drive C has no label.
 Volume Serial Number is 8C74-3344

 Directory of c:\MettleCI\cli\Jobs\Load

15/09/2022  07:29 PM    <DIR>          .
15/09/2022  07:29 PM    <DIR>          ..
15/09/2022  07:29 PM            14,161 LD_SALE.isx
15/09/2022  07:29 PM            13,623 LD_STOCKITEM.isx
15/09/2022  07:29 PM            10,010 LD_STOCK_HOLDING.isx
15/09/2022  07:29 PM            11,916 LD_SUPPLIER.isx
               4 File(s)         49,710 bytes
               2 Dir(s)  15,827,783,680 bytes free

c:\MettleCI\cli>
```

## Incremental export usage

Incrementally export project binaries, `C:/shared/myproject/export` is a
directory containing previously exported ISX files and
`C:/shared/myproject/cache` contains *state* files related to
incremental operations performed against `myproject`:

``` plain
C:\MettleCI\cli\> mettleci isx export ^
     -domain myteam-svcs.corp.com:59445 ^
     -username myuser -password mypassword  ^
     -server myteam-engn.corp.com  ^
     -project myproject  ^
     -location C:\shared\myproject\export  ^
     -include-binaries  ^
     -project-cache C:\shared\myproject\cache
Analyzing test2-engn.datamigrators.io/myproject
Attempting to identify changes with 4 working threads.
Inspecting DataStage assets for changes...
 * Check myteam-engn.corp.com/myproject/Jobs/Connections/DMSqlServer_DW.dcn - COMPLETED
 * Check myteam-engn.corp.com/myproject/Jobs/Connections/DMSqlServer_OLTP.dcn - COMPLETED
<SNIP>
 * Check myteam-engn.corp.com/myproject/Jobs/ParameterSets/pGlobal.pst - COMPLETED
 * Check myteam-engn.corp.com/myproject/Jobs/ParameterSets/pDMSqlServer_DW.pst - COMPLETED
Change identification complete
Inspecting ParameterSet definition changes...
ParameterSet definition change identification complete
Deleting assets...
 * Export 'C:\shared\myproject\export\Jobs\Transform\TR_PURCHASE.isx/Jobs/Transform/TR_PURCHASE.pjb' - DELETED
 * Export 'C:\shared\myproject\export\Jobs\Transform\TR_ORDERS.isx/Jobs/Transform/TR_ORDERS.pjb' - DELETED
Deletion complete
Exporting DataStage assets...
 * Export 'myteam-engn.corp.com/myproject/Jobs/Transform/TR_ORDERS.pjb' - COMPLETED
 * Export 'myteam-engn.corp.com/myproject/Jobs/Transform/TR_PURCHASE.pjb' - COMPLETED
Export complete
Attempting to identify last change with 4 working threads.
Inspecting DataStage assets for last change...
 * Check myteam-engn.corp.com/myproject/Jobs/ParameterSets/pDMSqlServer_OLTP.pst - COMPLETED
 * Check myteam-engn.corp.com/myproject/Jobs/ParameterSets/pGlobal.pst - COMPLETED
<SNIP>
 * Check myteam-engn.corp.com/myproject/Jobs/Transform/TR_PURCHASE.pjb - COMPLETED
 * Check myteam-engn.corp.com/myproject/Jobs/Transform/TR_ORDERS.pjb - COMPLETED
Last change identification complete
```

# See also

-   An example using `mettle isx export` to support a <a
    href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/408322069/Compliance+Test+Command#Example"
    rel="nofollow">multi-job compliance query</a>.

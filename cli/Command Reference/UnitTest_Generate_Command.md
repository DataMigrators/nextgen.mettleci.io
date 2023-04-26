# UnitTest Generate Command

# Purpose

Generates a MettleCI Unit Test for one or more specified DataStage Jobs.

The optional `-check-row-count-only` flag will cause the generation of
<a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/1562116127/Row+Count+Unit+Testing"
data-linked-resource-id="1562116127" data-linked-resource-version="3"
data-linked-resource-type="page">unit tests which check row counts</a>,
rather than the default option which is to compare data row-by-row.

# Syntax

  

# Example

``` bash
$> mettleci unittest generate \
   -assets /opt/dm/mci/jobs \
   -joblist ./joblist.txt \
   -specs /opt/dm/mci/testspecs
```

  

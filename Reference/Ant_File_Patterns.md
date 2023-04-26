# Ant File Patterns

A number of MettleCI Commands use
<a href="https://ant.apache.org/manual/dirtasks.html#patterns"
rel="nofollow">Ant file pattens</a> for the specification of files upon
which they operate. For example, the `remote upload`
(<a href="Remote_Upload_Command" data-linked-resource-id="716603405"
data-linked-resource-version="27"
data-linked-resource-type="page">link</a>) and `remote download`
(<a href="Remote_Download_Command" data-linked-resource-id="716636187"
data-linked-resource-version="26"
data-linked-resource-type="page">link</a>) commands use Ant patterns to
specify which files will be included in the command’s transfer process.
For example, to *shallow *copy all files in the `unittest` directory use
the pattern `unittest/*`.  For recursive (deep) copying of the same
directory use `unittest/**/*`. 

Ant is also powerful enough to do more complex matching such as all XML
files within an arbitrarily-deep directory tree
(i.e., `unittest/**/*.xml`) or to shallow copy all XML files only a
single directory deep within the `unittest` directory, i.e.,
`unittest/*/*.xml`) (noting this time the *single* `/*/`).

Multiple transfer patterns can be supplied using a comma separated
notation. For example, `unittest/**/*.xml,unittest/**/*.csv` matches all
XML and CSV files within an arbitrarily-deep directory tree. It should
be noted that many of the MettleCI commands supporting the use of Ant
syntax also support the use of multiple `-pattern` parameters, so in the
previous example it may be more readable to use a command of the form…

``` java
$> mettleci namespace command \
   -patern unittest/**/*.xml \
   -pattern unittest/**/*.csv   
```

## MettleCI Components using ANT Patterns

-   Page:

    <a href="/wiki/spaces/MCIDOC/pages/716636187/Remote+Download+Command"
    data-linked-resource-id="716636187" data-linked-resource-type="page"
    data-linked-resource-version="26">Remote Download Command</a>

-   Page:

    <a href="/wiki/spaces/MCIDOC/pages/716603405/Remote+Upload+Command"
    data-linked-resource-id="716603405" data-linked-resource-type="page"
    data-linked-resource-version="27">Remote Upload Command</a>

-   Page:

    <a href="/wiki/spaces/MCIDOC/pages/458850355/ISX+Set-Params+Command"
    data-linked-resource-id="458850355" data-linked-resource-type="page"
    data-linked-resource-version="23">ISX Set-Params Command</a>

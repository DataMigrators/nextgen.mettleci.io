# ISX Set-Params Command

# Purpose

Update Job Parameter values within an ISX file.

File paths supplied to the `-patterns` parameter must follow
<a href="https://ant.apache.org/manual/dirtasks.html"
rel="nofollow">Ant-style syntax</a>.

# Syntax

# Example

The following command recursively finds all `EX_*.isx` and `LD_*.isx`
files relative to the current working directory and sets the
\``` $APT_CONFIG_FILE` `` parameter within those files to the value
\``` /app/IBM/InformationServer/Server/Configs/default.apt` ``.

``` java
$> mettleci isx set-params \
    -pattern "**/EX_*.isx" \
    -pattern "**/LD_*.isx" \
    -P "$APT_CONFIG_FILE=/app/IBM/InformationServer/Server/Configs/default.apt"
```

  

---
layout: default
title: "Troubleshooting"
nav_order: 2
has_children: true
---

# Troubleshooting

# The \`mettleci datastage create-project\` command fails

# Symptom

The `mettleci datastage create-project` command (<a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/408420417/DataStage+Create-Project+Command"
data-linked-resource-id="408420417" data-linked-resource-version="33"
data-linked-resource-type="page">documented here</a>) fails
inexplicably.

# Cause

Due to a known issue with the DataStage `dsadmin` command (which is
required by `datastage create-project`) it is not possible to
distinguish between...

-   a DataStage project that already exists, and

-   a DataStage project that doesn’t exist in the DataStage repository,
    but for which the associated filesystem directories does exist.

There may be some situations in which this causes the `create-project`
command to fail.

# Solution

When faced with an inexplicable failure of this nature check to see if
the project’s directory structure already exists on the filesystem. If
so, and it’s safe to do so, remove the file structure and try again

------------------------------------------------------------------------

# See also

-   <a
    href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/408420417/DataStage+Create-Project+Command"
    data-linked-resource-id="408420417" data-linked-resource-version="33"
    data-linked-resource-type="page">DataStage Create-Project Command</a>

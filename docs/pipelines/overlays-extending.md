---
status: draft #Status can be draft, reviewed or published. 
owner: John McKeever
tags:
  - Pipelines
---

# Extending Overlays to more complex Scenarios

## Flexibility in Directory Structure

The examples use a single overlay per environment but mcix overlay allows the application of
multiple overlays when generating the environment specific releases. It also allows variable
substitutions from both environment variables and properties file.
In the examples above, environment-specific overlays have been used. This would be achieved by
running ...

```
mcix overlay apply \
   -assets ./datastage \
    -overlay ./overlays/<environment> \
    -output release.zip
```

... where `<environment>` represents the name of the environment being deployed.

If every environment requires the same configuration changes but with different values, it is possible
to use a single overlay and rely on variable substitution for setting the values. For example,
instead of having a database.json5 overlay file for each environment, a single common overlay
could be used along with environment specific variable substitution file:

```
├── datastage/
│   └── ...
├── overlays/
│   └── common/
│       └── connection/
│           └── database.json5
├── test.var
├── qa.var
└── prod.var
```

The `database.json5` file would then look like this:

```
{
    oracle_db_host: "${database.host}",
    oracle_service_name: "${database.instance}",
    username: "${database.username}",
    password: "${database.password}",
}
```

The variables for each environment can be specified in the `test.var`, `qa.var`, and `prod.var` files.

The following is an example of the variables stored in `qa.var` :

```
database.host = qa.database.local
database.instance = qa
database.username = scott
database.password = tiger
```

This would then be executed like this...

```
 mcix overlay apply \
   -assets ./datastage
   -overlay ./overlays/common \
   -properties qa.var \
   -output release.zip
```

The `mcix overlay apply` (documentation) command is not restricted to applying a single overlay. This also allows the above strategies to be combined:

```
├── datastage/
│   └── ...
├── overlays/
│   ├── common/
│   ├── test/
│   ├── qa/
│   └── prod/
├── test.var
├── qa.var
└── prod.var
```

This approach would be executed like this...

```
mcix overlay apply \
   -assets ./datastage \
   -overlay ./overlays/common \
   -overlay ./overlays/<environment> \
   -properties qa.var \
   -output release.zip
```

... where `<environment>` again represents the name of the environment being deployed.


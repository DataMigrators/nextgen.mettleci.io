---
layout: page
title: Configuring_MettleCI_Workbench_to_increase_session_timeout
parent: Configuration
---

# Configuring MettleCI Workbench to increase session timeout

MettleCI Workbench ships with a default configuration which causes your
Workbench session to timeout after 60 minutes of inactivity. This
session limit (which is specified in minutes) can be modified by
specifying a `userInactiveTimeout` value in your MettleCI `config.yml`
file:

To increase the session timeout from 1 hour to 2 hours, for example,
configure this line in `config.yml`:

``` java
userInactiveTimeout: 120
```

 To remove the session timeout entirely (which we would not recommend)
set the limit to 0 minutes:

``` java
userInactiveTimeout: 0
```

 After each change to your `config.yml` file you will need to restart
the MettleCI Workbench service for the change to take effect.

---
layout: page
title: SELECT_used_in_custom_SQL
parent: .
---

# SELECT \* used in custom SQL

|                  |                                                                               |
|------------------|-------------------------------------------------------------------------------|
| **Rule name**    | SELECT \* used in custom SQL                                                  |
| **Parallel Job** | Yes                                                                           |
| **Server Job**   | Yes                                                                           |
| **Job Sequence** | \-                                                                            |
| **Description**  | Identifies Connector Stages using customer SQL employing a ‘SELECT \*’ clause |

# Description

Using a SQL `SELECT *` clause is can often retrieve more columns from
the database than your application requires, introducing unnecessary
inefficiency into your solution. This problem is exacerbated when a
database developer introduces new, unexpected columns to underlying
tables. Using 'SELECT \*' can also prevent the database from optimising
its underlying data access, and therefore may have to use more expensive
methods to retrieve your data than it otherwise might. This can
substantially affect the performance of your query. Finally, when you
use `SELECT *` as part of a join it's possible to retrieve two columns
of the same name from two different tables, which can cause potential
runtime errors when DataStage attempts to bind them to a single column
definition with that shared name.

# Actions

Modify your Connector Stages' `SELECT` statements to use explicit column
names.

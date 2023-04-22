---
layout: page
title: Job_Control_Routines_are_present
parent: .
---

# Job Control Routines are present

|                  |                                                   |
|------------------|---------------------------------------------------|
| **Rule name**    | Job Control Routines are present                  |
| **Parallel Job** | Yes                                               |
| **Server Job**   | Yes                                               |
| **Job Sequence** | \-                                                |
| **Description**  | Identifies Jobs with Job Control Routines defined |

# Description

When stopping a parent job, a Job triggered by a Job Control Routine
will not be stopped, and has to be killed manually. You may wish to
promote your Job Control into the overarching Job Sequence or other Job
orchestration mechanism.

Also note that the
<a href="http://s2px.mettleci.io/" rel="nofollow">S2PX Server to
Parallel conversion utility</a> does not convert Job Control Routines.

# Actions

Promote your Job Control into the overarching Job Sequence or other Job
orchestration mechanism.

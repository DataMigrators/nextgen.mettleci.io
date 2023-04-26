# How does the MettleCI Workbench Service work in Unix?

Services in linux are always executed as the root user. The MettleCI
Workbench installer configures the service to execute the script located
in `/opt/dm/mci/dm-mettleci-workbench` to provide the service. When this
script runs it will switch user to the `mciworkb` user and execute the
`start-mettleci.sh` script which is responsible for setting required
environment variables and starting the Workbench server.

The chain of technologies works like this:

Linux O/S → `dm-mettleci-workbench` → `start-mettleci.sh` → Java v1.8 →
`workbench.jar`

In an environment running multiple versions of Java, the `mciworkb`
user's path and environment variables must be configured so that when
the `mciworkb` user executes `java -version` it shows the expected
OpenJDK v1.8 JVM. 

**Note:** The `start-mettleci.sh` and `dm-mettleci-workbench` scripts
should not be manually modified as they may be replaced during MettleCI
software updates.

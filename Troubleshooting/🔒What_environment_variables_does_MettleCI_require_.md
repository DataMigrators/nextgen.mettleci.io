# 🔒What environment variables does MettleCI require?

\<describe them here\>

# Diagnostics

``` bash
# Get the MettleCI PID...
$> ps -ef | grep -i [m]ettle-ui
mciworkb  2113     1  0 09:10 ?        00:00:41 /bin/java -jar /opt/dm/mci/mettle-ui-1.0-1415.jar server /opt/dm/mci/config.yml

# Get the process environment for the MettleCI PID...
$> sudo cat /proc/2113/environ | tr '\0' '\n'
DSHOME=/opt/IBM/InformationServer/Server/DSEngine
XDG_SESSION_ID=c3
HOSTNAME=myhost.mycorp.com
SHELL=/bin/bash
TERM=unknown
USER=mciworkb
LD_LIBRARY_PATH=/opt/IBM/InformationServer/Server/biginsights/IHC/c++/Linux-amd64-64/lib:/opt/IBM/InformationServer/Server/branded_odbc/lib:/opt/IBM/InformationServer/Server/DSComponents/lib:/opt/IBM/InformationServer/Server/DSComponents/bin:/opt/IBM/InformationServer/Server/DSEngine/lib:/opt/IBM/InformationServer/Server/DSEngine/uvdlls:/opt/IBM/InformationServer/Server/PXEngine/lib:/opt/IBM/InformationServer/jdk/jre/lib/amd64/j9vm:/opt/IBM/InformationServer/jdk/jre/lib/amd64:/opt/IBM/InformationServer/ASBNode/lib/cpp:/opt/IBM/InformationServer/ASBNode/apps/proxy/cpp/linux-all-x86_64:
SUDO_USER=root
SUDO_UID=0
ISHOME=/opt/IBM/InformationServer
USERNAME=mciworkb
APT_ORCHHOME=/opt/IBM/InformationServer/Server/PXEngine
MAIL=/var/spool/mail/mciworkb
PATH=/sbin:/bin:/usr/sbin:/usr/bin:/usr/local/sbin:/home/mciworkb/.local/bin:/home/mciworkb/bin
DSRPCD_PORT_NUMBER=31538
PWD=/home/mciworkb
UDTBIN=/opt/IBM/InformationServer/Server/DSEngine/ud41/bin
LANG=en_US.UTF-8
TZ=:/etc/localtime
HOME=/home/mciworkb
SUDO_COMMAND=/bin/bash -c /opt/dm/mci/start-mettleci.sh
ODBCINI=/opt/IBM/InformationServer/Server/DSEngine/.odbc.ini
ASBHOME=/opt/IBM/InformationServer/ASBNode
LOGNAME=mciworkb
LESSOPEN=||/usr/bin/lesspipe.sh %s
SUDO_GID=0
XDG_RUNTIME_DIR=/run/user/1002
UDTHOME=/opt/IBM/InformationServer/Server/DSEngine/ud41
_=/bin/nohup

$>
```

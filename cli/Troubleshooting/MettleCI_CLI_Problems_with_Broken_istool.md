# MettleCI CLI: Problems with Broken istool

Some of the MettleCI CLI commands such as import export etc. rely on the
Information Server istool utility.

While performing an upgrade to 11.7.1 FP4 recently, it was found that
istool was no longer working for the mciworkb user.

An IBM Tech Note has been published which documents the issue:-

<a
href="https://www.ibm.com/support/pages/infosphere-information-server-manager-and-istool-command-may-encounter-errors-after-applying-jr55455"
data-card-appearance="inline"
rel="nofollow">https://www.ibm.com/support/pages/infosphere-information-server-manager-and-istool-command-may-encounter-errors-after-applying-jr55455</a>

WARNING: Do not perform Step 1 of the ‘Resolving the Problem’ ISTOOL
section in the above tech note without first backing up the files

## Detailed Explanation of the Issue

After an upgrade, running the istool command on the Information Server
engine is not returning anything:-

``` java
$ . cat /.dshome/dsenv
$ /opt/IBM/InformationServer/Clients/istools/cli/istool.sh
export
-domain test1171-svcs.dm-sandbox.datamigrators.io:59445
-username isadmin
-password "*******"
-archive AnimalZodiac.isx
-preview
-datastage ' -base="TEST1171-ENGN.DM-SANDBOX.DATAMIGRATORS.IO/s2px_original" "/AnimalZodiac."'
$
```

  
​When inspecting the log from `~/istools_workspace/.metadata/.log`, it
shows:-

``` java
!SESSION 2022-10-28 08:24:18.841 -----------------------------------------------
eclipse.buildId=unknown
java.fullversion=8.0.7.0 - pxa6480sr7-20211025_01(SR7)
JRE 1.8.0 Linux amd64-64-Bit Compressed References 20211022_15212 (JIT enabled, AOT enabled)
OpenJ9   - 6abb372
OMR      - b898db9
IBM      - 2f2c48b
BootLoader constants: OS=linux, ARCH=x86_64, WS=gtk, NL=en_US
Framework arguments:  export -domain test1171-svcs.dm-sandbox.datamigrators.io:59445 -username isadmin -password (omitted) -archive AnimalZodiac.isx -preview -datastage  -base="TEST1171-ENGN.DM-SANDBOX.DATAMIGRATORS.IO/s2px_original" "/AnimalZodiac."
Command-line arguments:  export -domain test1171-svcs.dm-sandbox.datamigrators.io:59445 -username isadmin -password (omitted) -archive AnimalZodiac.isx -preview -datastage  -base="TEST1171-ENGN.DM-SANDBOX.DATAMIGRATORS.IO/s2px_original" "/AnimalZodiac."
​
!ENTRY org.eclipse.emf.ecore 2 0 2022-10-28 08:24:19.980
!MESSAGE Both 'com.ibm.iis.istools.cli.commands' and 'com.ibm.iis.istools.cli' register a package for 'http://com.ibm.iis.istools.repository.core/connection'
​
!ENTRY com.ibm.iis.client 2 0 2022-10-28 08:24:20.226
!MESSAGE Property [j2ee.opts] is empty or not found in the [/opt/IBM/InformationServer/ASBNode/bin/setupEnv.properties] file. No application server specific JVM properties will be set.
​
!ENTRY org.eclipse.osgi 2 1 2022-10-28 08:24:20.284
!MESSAGE NLS unused message: Rename_suffix_default in: com.ibm.istools.cli.ftoptions.utils.messages
​
!ENTRY org.eclipse.osgi 4 0 2022-10-28 08:24:22.290
!MESSAGE Application error
!STACK 1
java.lang.NoClassDefFoundError: org.apache.http.auth.Credentials
at java.lang.J9VMInternals.newInstanceImpl(Native Method)
at java.lang.Class.newInstance(Class.java:2062)
at com.ibm.iis.isf.service.impl.JavaHttpServiceFactory.getServiceWithoutWrapper(JavaHttpServiceFactory.java:182)
at com.ibm.iis.isf.service.ServiceFactory.getServiceWithoutWrapper(ServiceFactory.java:291)
at com.ibm.iis.isf.security.auth.impl.HttpAuthenticationService.getAuthService(HttpAuthenticationService.java:655)
at com.ibm.iis.isf.security.auth.impl.HttpAuthenticationService.createSession(HttpAuthenticationService.java:559)
at com.ibm.iis.isf.security.auth.impl.HttpAuthenticationService.login(HttpAuthenticationService.java:118)
at com.ibm.iis.istools.isf.core.ISFSession.login(ISFSession.java:132)
at com.ibm.iis.istools.isf.core.ISFSession.<init>(ISFSession.java:109)
at com.ibm.iis.istools.isf.core.connection.ConnectionManager.connect(ConnectionManager.java:97)
at com.ibm.iis.istools.cli.utils.ConnectionUtils.doConnect(ConnectionUtils.java:214)
at com.ibm.iis.istools.cli.utils.ConnectionUtils.connect(ConnectionUtils.java:135)
at com.ibm.iis.istools.cli.framework.AbstractCommandSet.getServerConnection(AbstractCommandSet.java:220)
at com.ibm.iis.istools.cli.commands.CommandSets.Export.doAction(Export.java:222)
at com.ibm.iis.istools.cli.Istool.parseCommandLine(Istool.java:114)
at com.ibm.iis.istools.cli.Application.start(Application.java:70)
at org.eclipse.equinox.internal.app.EclipseAppHandle.run(EclipseAppHandle.java:196)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.runApplication(EclipseAppLauncher.java:110)
at org.eclipse.core.runtime.internal.adaptor.EclipseAppLauncher.start(EclipseAppLauncher.java:79)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:369)
at org.eclipse.core.runtime.adaptor.EclipseStarter.run(EclipseStarter.java:179)
at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:90)
at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:55)
at java.lang.reflect.Method.invoke(Method.java:508)
at org.eclipse.equinox.launcher.Main.invokeFramework(Main.java:619)
at org.eclipse.equinox.launcher.Main.basicRun(Main.java:574)
at org.eclipse.equinox.launcher.Main.run(Main.java:1407)
at org.eclipse.equinox.launcher.Main.main(Main.java:1383)
Caused by: java.lang.ClassNotFoundException: org.apache.http.auth.Credentials
at org.eclipse.osgi.internal.loader.BundleLoader.findClassInternal(BundleLoader.java:506)
at org.eclipse.osgi.internal.loader.BundleLoader.findClass(BundleLoader.java:422)
at org.eclipse.osgi.internal.loader.BundleLoader.findClass(BundleLoader.java:410)
at org.eclipse.osgi.internal.baseadaptor.DefaultClassLoader.loadClass(DefaultClassLoader.java:107)
at java.lang.ClassLoader.loadClass(ClassLoader.java:873)
... 29 more
```

​  
After installation of 11.5 Fix Pack 2, ISM would not open; the flash
screen for the product would appear for a few seconds and close. No
messages are generated in the log.  
​  
Cause:  
After installing JR55455, or upgrading to 11.7.1.4 (aka FP4)  
​​  
IBM Technote:  
<a
href="https://www.ibm.com/support/pages/infosphere-information-server-manager-and-istool-command-may-encounter-errors-after-applying-jr55455"
data-card-appearance="inline"
rel="nofollow">https://www.ibm.com/support/pages/infosphere-information-server-manager-and-istool-command-may-encounter-errors-after-applying-jr55455</a>  
<a href="http://www-01.ibm.com/support/docview.wss?uid=swg21982420"
data-card-appearance="inline"
rel="nofollow">http://www-01.ibm.com/support/docview.wss?uid=swg21982420</a>  
​  

## Resolution Steps​

### Solution for istool:

#### Part 1

1.  Go to user's eclipse istool configuration

Note: the folder is not fixed at
`com.ibm.iis.istools.cli.istoolCli_1.0.0_953920789`, the build number
can change with different version of DataStage

``` java
cd ~/.eclipse/com.ibm.iis.istools.cli.istoolCli_1.0.0_953920789/configuration
ls -al
```

2\. If "config.ini" is missing, create "config.ini" with the following

``` java
#Linked configuration
#Fri Oct 28 11:25:02 GMT+10:00 2022
osgi.sharedConfiguration.area=file:configuration/
```

​3. Remove all org.eclipse.\*

``` java
rm -rf org.eclipse.*
```

​4. Remove istool workspace under user home

Note: For Windows, it will be under
`%userprofile%.eclipse\com.ibm.iis.istools.cli.istoolCli_x.x.x_xxxxxxx\configuration\`

``` java
cd ~
rm -rf istool_workspace
```

#### ​ Part2

Usually applying Part1 of the solution will be enough, only if that
doesn't work try Part 2

Note: Part 2 of the solution is extracted from IBM tech note, and has
not been tested successfully, so backup the files/folders first

``` java
cd $ISHOME/Clients/istools/cli/configurations
rm -rf org.eclipse.*
```

###  ​Solution for IS Manager:

1.  Check whether the following files exist in the Information Server
    Manager configuration directory
    `<ISHOME>\Clients\istools\manager\configuration`  

    ``` java
    config.ini
    org.eclipse.core.runtime
    org.eclipse.equinox.app
    org.eclipse.equinox.launcher
    org.eclipse.equinox.simpleconfigurator
    org.eclipse.osgiorg.eclipse.update
    ```

      

2.  Take a backup of the
    `<ISHOME>\Clients\istools\manager\configuration` directory for
    safekeeping.  
    ​

3.  Delete all the `org.eclipse.*` folders except
    `org.eclipse.equinox.simpleconfigurator` folder so that you ONLY
    have the following files in
    `<ISHOME>\Clients\istools\manager\configuration` directory.  
    ​

    ``` java
    config.ini
    org.eclipse.equinox.simpleconfigurator
    ```

    ​

4.  Make sure that the
    `org.eclipse.equinox.simpleconfigurator\bundles.info` file is NOT
    moved or deleted.  
    ​

5.  Delete Eclipse workspace for Information Server Manager.  

6.  Take a backup of `%userprofile%\ismanager_workspace` and delete the
    folder. The folder will get re-created when IS Manager is used the
    next time.  
    ​

Note: If you are now able to login to the Information Server Manager and
all is working as expected, you can remove the backup of
`<ISHOME>\Clients\istools\manager\configuration` directory.

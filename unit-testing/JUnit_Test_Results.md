# JUnit Test Results

# What is JUnit?

JUnit is a unit testing framework which plays a crucial role test-driven
development, and is part of a family of unit testing frameworks
collectively known as
<a href="https://en.wikipedia.org/wiki/XUnit" rel="nofollow">xUnit</a>.
The JUnit XML output format is widely understood by build and test tools
and is a good choice for tools wishing to describe their test outcomes.
Here is a summary of a JUnit output file, showing a skipped, failed and
passed result.

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<testsuites>
   <testsuite name="MyTestSuiteName" errors="0" tests="0" failures="0" time="0" timestamp="2000-01-01T11:12:13" />
   <testsuite name="MyOtherTestSuiteName" errors="0" skipped="1" tests="3" failures="1" time="0.006" timestamp="2000-01-02T11:12:13">
      <properties>
         <property name="MyName1" value="one" />
         <property name="MyName2" value="two" />
         <property name="MyName3" value="three" />
      </properties>
      <testcase classname="MyTest1" name="should default path to an empty string" time="0.006">
         <failure message="test failure">Assertion failed</failure>
      </testcase>
      <testcase classname="MyTest2" name="should default consolidate to true" time="0">
         <skipped />
      </testcase>
      <testcase classname="MyTest3" name="should default some other thing to true" time="0" />
   </testsuite>
</testsuites>
```

# Schema

The JUnit XML Report output is produced by a number of MettleCI commands
and it can be a little tricky to nail down an official spec for the
format, even though it's widely adopted and used.   There have been a
number of attempts to codify the schema, but here’s a working XSD for
JUnit:

<img src="attachments/1754890299/1806827622.png?width=550"
class="image-center" loading="lazy"
data-image-src="attachments/1754890299/1806827622.png" data-height="470"
data-width="1309" data-unresolved-comment-count="0"
data-linked-resource-id="1806827622" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20210609-104941.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="1754890299"
data-linked-resource-container-version="7"
data-media-id="6ab24fc7-9854-4df9-bd1e-65c16510fbd7"
data-media-type="file" width="550" />

``` java
<?xml version="1.0" encoding="UTF-8"?>
<!-- a description of the JUnit XML format and how Jenkins parses it. See also junit.xsd -->

<!-- if only a single testsuite element is present, the testsuites
     element can be omitted. All attributes are optional. -->
<testsuites disabled=""   <!-- total number of disabled tests from all testsuites. -->
            errors=""     <!-- total number of tests with error result from all testsuites. -->
            failures=""   <!-- total number of failed tests from all testsuites. -->
            name=""
            tests=""      <!-- total number of successful tests from all testsuites. -->
            time=""       <!-- time in seconds to execute all test suites. -->
            >

  <!-- testsuite can appear multiple times, if contained in a testsuites element.
       It can also be the root element. -->
  <testsuite name=""      <!-- Full (class) name of the test for non-aggregated testsuite documents.
                               Class name without the package for aggregated testsuites documents. Required -->
         tests=""         <!-- The total number of tests in the suite, required. -->
         disabled=""      <!-- the total number of disabled tests in the suite. optional -->
             errors=""    <!-- The total number of tests in the suite that errored. An errored test is one that had an unanticipated problem,
                               for example an unchecked throwable; or a problem with the implementation of the test. optional -->
             failures=""  <!-- The total number of tests in the suite that failed. A failure is a test which the code has explicitly failed
                               by using the mechanisms for that purpose. e.g., via an assertEquals. optional -->
             hostname=""  <!-- Host on which the tests were executed. 'localhost' should be used if the hostname cannot be determined. optional -->
         id=""            <!-- Starts at 0 for the first testsuite and is incremented by 1 for each following testsuite -->
         package=""       <!-- Derived from testsuite/@name in the non-aggregated documents. optional -->
         skipped=""       <!-- The total number of skipped tests. optional -->
         time=""          <!-- Time taken (in seconds) to execute the tests in the suite. optional -->
         timestamp=""     <!-- when the test was executed in ISO 8601 format (2014-01-21T16:17:18). Timezone may not be specified. optional -->
         >

    <!-- Properties (e.g., environment settings) set during test
     execution. The properties element can appear 0 or once. -->
    <properties>
      <!-- property can appear multiple times. The name and value attributres are required. -->
      <property name="" value=""/>
    </properties>

    <!-- testcase can appear multiple times, see /testsuites/testsuite@tests -->
    <testcase name=""       <!-- Name of the test method, required. -->
          assertions=""     <!-- number of assertions in the test case. optional -->
          classname=""      <!-- Full class name for the class the test method is in. required -->
          status=""
          time=""           <!-- Time taken (in seconds) to execute the test. optional -->
          >

      <!-- If the test was not executed or failed, you can specify one
           the skipped, error or failure elements. -->

      <!-- skipped can appear 0 or once. optional -->
      <skipped/>

      <!-- Indicates that the test errored. An errored test is one
           that had an unanticipated problem. For example an unchecked
           throwable or a problem with the implementation of the
           test. Contains as a text node relevant data for the error,
           for example a stack trace. optional -->
      <error message=""     <!-- The error message. e.g., if a java exception is thrown, the return value of getMessage() -->
         type=""            <!-- The type of error that occured. e.g., if a java execption is thrown the full class name of the exception. -->
         ></error>

      <!-- Indicates that the test failed. A failure is a test which
       the code has explicitly failed by using the mechanisms for
       that purpose. For example via an assertEquals. Contains as
       a text node relevant data for the failure, e.g., a stack
       trace. optional -->
      <failure message=""   <!-- The message specified in the assert. -->
           type=""          <!-- The type of the assert. -->
           ></failure>

      <!-- Data that was written to standard out while the test was executed. optional -->
      <system-out></system-out>

      <!-- Data that was written to standard error while the test was executed. optional -->
      <system-err></system-err>
    </testcase>

    <!-- Data that was written to standard out while the test suite was executed. optional -->
    <system-out></system-out>
    <!-- Data that was written to standard error while the test suite was executed. optional -->
    <system-err></system-err>
  </testsuite>
</testsuites>
```

# MettleCI Commands which produce JUnit files

-   Page:

    <a href="/wiki/spaces/MCIDOC/pages/408322069/Compliance+Test+Command"
    data-linked-resource-id="408322069" data-linked-resource-type="page"
    data-linked-resource-version="29">Compliance Test Command</a>

-   Page:

    <a href="/wiki/spaces/MCIDOC/pages/410157081/DataStage+Compile+Command"
    data-linked-resource-id="410157081" data-linked-resource-type="page"
    data-linked-resource-version="33">DataStage Compile Command</a>

-   Page:

    <a
    href="/wiki/spaces/MCIDOC/pages/410681364/DataStage+Connector+Migration+Command"
    data-linked-resource-id="410681364" data-linked-resource-type="page"
    data-linked-resource-version="23">DataStage Connector Migration
    Command</a>

-   Page:

    <a href="/wiki/spaces/MCIDOC/pages/423952410/DataStage+Deploy+Command"
    data-linked-resource-id="423952410" data-linked-resource-type="page"
    data-linked-resource-version="30">DataStage Deploy Command</a>

-   Page:

    <a href="/wiki/spaces/MCIDOC/pages/458817755/DataStage+Execute+Command"
    data-linked-resource-id="458817755" data-linked-resource-type="page"
    data-linked-resource-version="15">DataStage Execute Command</a>

-   Page:

    <a href="/wiki/spaces/MCIDOC/pages/718831617/UnitTest+Test+Command"
    data-linked-resource-id="718831617" data-linked-resource-type="page"
    data-linked-resource-version="19">UnitTest Test Command</a>

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20210609-104941.png](attachments/1754890299/1806827622.png)
(image/png)  

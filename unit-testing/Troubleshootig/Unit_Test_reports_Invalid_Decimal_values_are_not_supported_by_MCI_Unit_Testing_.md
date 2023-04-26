# Unit Test reports 'Invalid Decimal values are not supported by MCI Unit Testing'

# Problem

When running MettleCI Unit Testing you receive the message
`Invalid Decimal values are not supported by MCI Unit Testing`.

# Cause

MettleCI’s Unit Test functionality relies on DataStage’s underlying Java
integration capabilities. There are two types of data which will cause
exceptions within DataStage’s Java Integration stage:

1.  **Invalid Decimals** which are data defined as decimal but which do
    not fulfil the definition of that format, and

2.  **Binary Zero Decimals** which are literal `0x00` (ASCII `null`)
    bytes in the memory space which we are attempting to interpret as
    '0.0' but *can* be considered valid by DataStage if the
    <a href="https://www.ibm.com/docs/en/iis/11.7?topic=listing-fix-zero"
    rel="nofollow">fix_zero</a> option is specified.

For Unit Testing to operate correctly it needs to be able to read
(during Unit Test Interception) and write (during Unit Test Execution)
both of these types of decimal values. Unfortunately, the Java
Integration Stage can’t successfully do this for either type of invalid
data. MettleCI implements a workaround to avoid the exception reported
when reading one of these types of invalid decimal values:

|                                            |                                                                          |                                                                          |
|--------------------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------|
|  MettleCI support for invalid decimal data | **Read**                                                                 | **Write**                                                                |
| **Invalid Decimal**                        | <img src="images/icons/emoticons/72/2714.png"                            
                                              class="emoticon emoticon-blue-star" data-emoji-id="2714"                  
                                              data-emoji-shortname=":heavy_check_mark:" data-emoji-fallback="✔️"        
                                              data-emoticon-name="blue-star" width="16" height="16"                     
                                              alt="(blue star)" />                                                      | <img src="images/icons/emoticons/72/2716.png"                            
                                                                                                                         class="emoticon emoticon-blue-star" data-emoji-id="2716"                  
                                                                                                                         data-emoji-shortname=":heavy_multiplication_x:" data-emoji-fallback="✖️"  
                                                                                                                         data-emoticon-name="blue-star" width="16" height="16"                     
                                                                                                                         alt="(blue star)" />                                                      |
| **Binary Zero**                            | <img src="images/icons/emoticons/72/2716.png"                            
                                              class="emoticon emoticon-blue-star" data-emoji-id="2716"                  
                                              data-emoji-shortname=":heavy_multiplication_x:" data-emoji-fallback="✖️"  
                                              data-emoticon-name="blue-star" width="16" height="16"                     
                                              alt="(blue star)" />                                                      | <img src="images/icons/emoticons/72/2716.png"                            
                                                                                                                         class="emoticon emoticon-blue-star" data-emoji-id="2716"                  
                                                                                                                         data-emoji-shortname=":heavy_multiplication_x:" data-emoji-fallback="✖️"  
                                                                                                                         data-emoticon-name="blue-star" width="16" height="16"                     
                                                                                                                         alt="(blue star)" />                                                      |

Despite this there is still no way for MettleCI to write Invalid
Decimals, or to read or write Binary Zero Decimals.

MettleCI captures the invalid decimals during Unit Test <a
href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/437518414/Unit+Test+Data+Interception+-+Capturing+Existing+Test+Data?src=search"
rel="nofollow">Interception</a> but when a Unit Test is executed the
MettleCI Unit Test harness attempts to read those Unit Test data
containing invalid decimals the Unit Test Harness will display an error
message.

The benefits of this approach are:

1.  Invalid Decimals are likely to be rare and possibly unexpected, so
    capturing them allows users to capture all useful data and then
    either manually change the Invalid Decimal values or remove them
    entirely using the <a
    href="https://datamigrators.atlassian.net/wiki/spaces/MCIDOC/pages/466387402/Manually+Editing+Unit+Test+Data"
    data-linked-resource-id="466387402" data-linked-resource-version="6"
    data-linked-resource-type="page">Unit Test Data editor</a>.

2.  Unit Testing would still be able to produce failed test results when
    the expected Job output does not contain Invalid Decimals but the
    actual output does. This is a lot more useful then aborting a Unit
    Test where the Job produces unexpected Invalid Decimals

3.  When a user intercepts data and then attempts to run the resulting
    unit test MettleCI , we can present the user with a very clear
    message stating its not supported. This will hopefully prevent
    unnecessary support requests

Unfortunately, we’ll still crash out with Binary Zero decimals but there
isn’t anything we can do about that (including specific error message).

# Solution

Edit the intercepted unit test data to remove the invalid values. You
can do this by either replacing individual values with invalid values,
or removing the rows containing invalid values entirely.

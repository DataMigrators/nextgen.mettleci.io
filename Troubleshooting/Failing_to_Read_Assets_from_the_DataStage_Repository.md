# Failing to Read Assets from the DataStage Repository

## Problem

If you are using the DataStage Bamboo capability (<a
href="https://datamigrators.atlassian.net/wiki/spaces/AET/pages/291700836/Bamboo+Agent+Configuration"
data-linked-resource-id="291700836" data-linked-resource-version="27"
data-linked-resource-type="page">Bamboo Agent Configuration</a>) then
under the hood MettleCI will interact with DataStage through SSH
(<a href="https://en.wikipedia.org/wiki/Secure_Shell" rel="nofollow">What
is SSH?</a>).  To configure this communication to work properly you must
take some preparatory steps.

## Solution

Follow carefully the steps described by IBM in their document <a
href="https://www.ibm.com/support/knowledgecenter/en/SSZJPZ_11.3.0/com.ibm.swg.im.iis.found.admin.common.doc/topics/cert_truststore.html"
rel="nofollow">Storing certificates for client applications</a>.  This
should adequately solve any outstanding issues with the DataStage bamboo
capability.

Be attentive to the paragraph that mentions "**For command line
utilities"**.  We recommend using <a
href="https://www.ibm.com/support/knowledgecenter/en/search/istool%20export?scope=SSZJPZ_11.5.0"
rel="nofollow">istool export</a> to test if this communication is
working properly without harming your environment.

## Related articles

-   Page:

    <a href="/wiki/spaces/MCIDOC/pages/619511871"
    data-linked-resource-id="619511871" data-linked-resource-type="page"
    data-linked-resource-version="5">WIP - Wallboard give 'self signed
    certificate in certificate chain' error 🔓</a>

-   Page:

    <a href="/wiki/spaces/MCIDOC/pages/514326673/deprecated+labels"
    data-linked-resource-id="514326673" data-linked-resource-type="page"
    data-linked-resource-version="1">deprecated labels</a>

  

  

  

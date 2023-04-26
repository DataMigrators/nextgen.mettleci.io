# Workbench / DataStage TLS not working on Red Hat Enterprise Linux 8 (RHEL-8) or later

# Problem

Version 8 of Red Hat introduces some major overhauls to its security and
cryptographic components (<a
href="https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/considerations_in_adopting_rhel_8/security_considerations-in-adopting-rhel-8"
rel="nofollow">documented here</a>). Most notably, TLSv1 is disabled by
default which causes a problem for some not-so-recent versions of
DataStage which require TLSv1. Users of these versions may encounter
either of the following TLS Errors:

``` java
javax.net.ssl.SSLHandshakeException: Server chose TLSv1, but that protocol version is not enabled or not supported by the client.
```

or

``` java
javax.net.ssl.SSLHandshakeException: The server selected protocol version TLS10 is not accepted by client preferences [TLS12]
```

# Solution

Run the following command:

``` bash
update-crypto-policies --set LEGACY
```

Now restart the server that hosts MettleCI Workbench and verify that the
issue no longer occurs.

------------------------------------------------------------------------

# See Also

-   <a href="What_versions_of_TLS_does_MettleCI_Workbench_support_"
    data-linked-resource-id="2131460097" data-linked-resource-version="8"
    data-linked-resource-type="page">What level of TLS can MettleCI
    Workbench use?</a>

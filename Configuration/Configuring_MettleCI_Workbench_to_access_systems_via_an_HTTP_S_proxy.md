---
layout: page
title: Configuring_MettleCI_Workbench_to_access_systems_via_an_HTTP_S_proxy
parent: Configuration
---

# Configuring MettleCI Workbench to access systems via an HTTP/S proxy

All communication from MettleCI Workbench to other servers over HTTP/S
(e.g., Git and Work Item Management systems), can be configured to use a
proxy by adding the following settings to `config.yml`:

``` java
httpClient:
  proxy:
    host: 192.168.52.11
    port: 8080
    scheme : http
    auth:
      username: secret
      password: stuff
      authScheme: NTLM
      realm: realm
      hostname: host
      domain: WINDOWSDOMAIN
      credentialType: NT
    nonProxyHosts:
      - localhost
      - '192.168.52.*'
      - '*.example.com'
```

|                |                  |                                                                                                                                                                                                           |
|----------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Name**       | **Default**      | **Description**                                                                                                                                                                                           |
| host           | REQUIRED         | The proxy server host name or ip address.                                                                                                                                                                 |
| port           | (scheme default) | The proxy server port. If the port is not set then the scheme default port is used.                                                                                                                       |
| scheme         | http             | The proxy server URI scheme. HTTP and HTTPS schemas are permitted. By default HTTP scheme is used.                                                                                                        |
| auth           | (none)           | The proxy server `Basic` or `NTLM` authentication schemes. If they are not set then no credentials will be passed to the server.                                                                          |
| username       | REQUIRED         | The username used to connect to the server.                                                                                                                                                               |
| password       | REQUIRED         | The password used to connect to the server.                                                                                                                                                               |
| authScheme     | Basic            | The authentication scheme used by the. Allowed options are: `Basic`, `NTLM`                                                                                                                               |
| realm          | (none)           | The realm, used for NTLM authentication.                                                                                                                                                                  |
| hostname       | (none)           | The hostname of the windows workstation, used for NTLM authentication. Only used when credentialType is `NT`.                                                                                             |
| domain         | (none)           | The Windows Domain, used for NTLM authentication. Only used when credentialType is `NT`.                                                                                                                  |
| credentialType | (none)           | The type of credentials used for proxy authentication. Allowed options are: `UsernamePassword` or `NT`.                                                                                                   |
| nonProxyHosts  | (none)           | List of patterns of hosts that should be reached without proxy. The patterns may contain symbol ‘\*’ as a wildcard. If a host matches one of the patterns it will be reached through a direct connection. |

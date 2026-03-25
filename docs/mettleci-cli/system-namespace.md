---
status: reviewed #Status can be draft, reviewed or published. 
owner: John McKeever
tags:
  - Pipeline
  - CLI
---
# system namespace

The `system` namespace contains commands for understanding, diagnosing, and customizing your MettleCI CLI environment.  It can be useful in CI/CD pipelines as a diagnostic step to ensure the MettleCI CLI container environment is correctly configured. 

## system version

![system version](../railroads/svgs/system-version.svg "system version syntax")

This command displays:

- The MettleCI CLI [command shell](../command-shell) version number,
- Your O/S version and architecture,
- Your O/S username and language/locale settings, and
- A list of MettleCI CLI plugins loaded from your `plugins` folder.

Example output is ...

```shell
MettleCI Command Line (build 1.0-123)
(C) 2018-2025 Data Migrators Pty Ltd
system version (1.0-123)
Mac OS X 26.0 (aarch64)
johnmckeever, English (Australia)

Loaded plugins:
 * MettleCI CP4D Asset-Analysis Plugin (1.0-SNAPSHOT)
 * MettleCI CP4D Compilation Plugin (1.0-SNAPSHOT)
 * MettleCI CP4D Import Plugin (1.0-SNAPSHOT)
 * MettleCI CP4D Overlays Plugin (1.0-SNAPSHOT)
```

#### Examples

=== "Command Line"
    ```shell
    mcix system version
    ```

=== "GitHub Actions"
    ```yaml
    - name: mcix system version action
      uses: mettleci/mcix/system/version@latest
      id: mcix-system-version
    ```

=== "Azure DevOps Task"
    ```yaml
    - task: mcixSystemVersion@1
      inputs:
        imageName: 'mettleci.azurecr.io/mettleci/mcix'
      displayName: mcix system version action
    ```

---

=== "Command Line"
    ```shell
    mcix datastage compile \
      -api-key XXXXXXXXXXXXXXXXXXXXXXXX \
      -url https://cp4d.datamigrators.io \
      -user isadmin \
      -report mettleci_compilation.xml \
      -project dstage1 \
      -include-asset-in-test-name
    ``` 

=== "GitHub Actions"
    ```yaml
    - name: DataStage Compile using mcix datastage compile action
      uses: datamigrators/mcix/datastage/compile@latest
      id: mcix-datastage-compile
      with:
        api-key: ${{ secrets.CP4DKEY }}
        url: ${{ vars.CP4DHOSTNAME }}
        user: ${{ vars.CP4DUSERNAME }}
        project: ${{ env.DatastageProject }}         
    ```

=== "Azure DevOps Tasks"
    ```yaml
    - task: mcixDatastageCompile@1
      inputs:
        url: ${{ parameters.CP4DHostName }}
        user: ${{ parameters.CP4DUsername }}
        apiKey: ${{ parameters.CP4DKey }}
        project: ${{ parameters.DatastageProject }}
        report: '$(Build.SourcesDirectory)/log/compile/compilation_results.xml'
        includeAssetInTestName: true
        imageName: 'mettleci.azurecr.io/datamigrators/mcix'
      displayName: 'Compile DataStage Assets'
    ```

---



Your CI/CD pipelines (and which are demonstrated in the example pipelines) use a variety of mcix commands to achieve their outcomes.  These commands can be invoked within your pipeline using either of two different mechanisms:

1. Directly invoking the mcix CLI commands using a command line task within your pipeline, or
2. Using native mcix build tasks/plugins available for popular CI/CD platforms like Jenkins, GitHub Actions, Azure DevOps, and Bitbucket Pipelines.

The mcix build tasks/plugins provide a more integrated experience within your chosen CI/CD platform, allowing you to configure the tasks using the platform's native UI and features.  They also provide additional capabilities such as better logging, error handling, and integration with other tasks within your pipeline.

The following sections provide examples of how to use the mcix build tasks/plugins within your CI/CD pipelines for different platforms.

## Jenkins

To use the mcix build tasks in Jenkins, you need to install the MettleCI plugin from the Jenkins plugin repository. Once installed, you can add the mcix build tasks to your Jenkins pipeline using the following steps:

1. In your Jenkins pipeline script, add a stage for the mcix build task.
2. Use the `mcixBuild` step to configure the task, specifying the required parameters such as the assets location, overlay location, and output location.
3. Save and run your Jenkins pipeline.

Here is an example of a GitHub Actions pipeline stage that uses the mcix datastage import action to import datastage assets into a CP4D DataStage project:

````yaml
jobs:
  DeployMettleCIProject:
    runs-on: ubuntu-latest
    environment: ${{ inputs.EnvironmentName }}
    env:
      DatastageProject: ${{ vars.BASEPROJECTNAME }}_${{ vars.ENVID }}
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      # Import the DataStage assets to CPD using the mcix datastage import action
      - name: DataStage import using mcix datastage import action
        uses: datamigrators/mcix/datastage/import@latest
        id: mcix-datastage-import
        with:
          api-key: ${{ secrets.CP4DKEY }}
          url: ${{ vars.CP4DHOSTNAME }}
          user: ${{ vars.CP4DUSERNAME }}
          project: ${{ env.DatastageProject }}         
          assets: "${{ github.workspace }}/datastage"
````



## GitHub Actions

To use the mcix build tasks in GitHub Actions, you need to add a step in your workflow file that uses the MettleCI GitHub Action. You can configure the action by specifying the required parameters such as the assets location, overlay location, and output location.

Here is an example of a GitHub Actions workflow that uses the mcix build task to apply overlays:

```yaml
name: Apply Overlays
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v2
    - name: Apply Overlays
      uses: mettleci/mcix-github-action@v1
      with:
        assets: './datastage'
        overlay: './overlays/${{ env.TARGET_ENVIRONMENT }}'
        output: './build/deployment.zip'
``` 

## Azure DevOps

To use the mcix build tasks in Azure DevOps, you need to add a task in your pipeline that uses the MettleCI Azure DevOps extension. You can configure the task by specifying the required parameters such as the assets location, overlay location, and output location.

Here is an example of an Azure DevOps pipeline that uses the mcix build task to apply overlays: 

```yaml
trigger:
- main
pool:
  vmImage: 'ubuntu-latest'
steps:
- task: MettleCI.mcix-azure-devops-extension.mcixBuild.mcixBuild@1
  inputs:
    assets: './datastage'
    overlay: './overlays/$(TARGET_ENVIRONMENT)'
    output: './build/deployment.zip'
```


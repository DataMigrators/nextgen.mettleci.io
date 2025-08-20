---
status: reviewed
owner: John McKeever
tags:
  - DataStage
  - Creating Tests
  - Data Fabrication
---

# Using Test Case Data Fabrication

Test Casse Data fabrication is a DataStage capability accessed via the unit test [data editor](../testing/editing-datastage-tests.md).  This page provides a set of steps to using it.

## Step-by-step instructions

1. When editing test data use the column overflow menu ( ⠇) to select edit column then under Data Generation Settings select your Generator Type.  The fabrication  tools listed, and their uses, are described in MettleCI’s data fabrication tools.
???+ info "Note"
    Note that some generators may prompt you for parameters which are available (or required) for you to customise their behaviour.  Where one or more parameters are mandatory the column editor panel on the right of the screen will not permit you to save your settings (and hence close the panel) until the mandatory parameters have been supplied.
1. When you have selected your generator type and provided any required parameters, click Save.
1. Back in the test data editor you can regenerate data using your supplied specification in one of three ways:
    1. Right click the column header and select Regenerate data,
    1. Right click the table header (the unlabelled top-left header cell) and select Regenerate data, or
    1. Select a subset of cells by clicking and dragging in the table, then right click the table selection and select Regenerate data.

Note that these data fabrication settings are evaluated once, at the time that you select the Regenerate data option in the MettleCI Workbench test data editor. Once invoked they will populate the selected test data table cells with appropriate values.  The test data fabricaction settings will NOT be stored in the test data table’s metadata definition and the data itself will remain static, even when depoyed to downstream systems.  The only way to regenerate the test data is to use the test data editory in a MettleCI Workbench instance.
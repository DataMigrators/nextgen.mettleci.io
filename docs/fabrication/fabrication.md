---
classification: confidential #Remove this line if it's not IBM Confidential.
status: draft #Status can be draft, reviewed or published. 
owner: Add the main page authors
tags:
  - Fabrication
  - Test cases
---
# Fabrication

There are many benefits to using artifically generated data in software unit testing:

  * It enables consistent and repeatable tests. Fabricated data is predictable and avoids reliance on external systems like live databases or APIs.  This makes tests deterministic - exhibiting the same behaviour every time they’re run - which is critical for debugging and automation.

  * It can improve test coverage. You can fabricate edge cases, boundary conditions, and unusual scenarios that may not be present in real datasets. This allows you to stress-test logic under various conditions such as empty strings, large inputs, and invalid values.

  * It increases testing speed and efficiency. Tests run faster when they don’t have to query or populate real databases or APIs. The volume of your fabricated data can be optimised to supply no more and no less than is required to demonstrate your code’s correct behaviour, resulting in quicker execution, and consequently faster feedback, when used in CI/CD pipelines.

  * It supports test isolation. Data fabrication ensures that each unit test is self-contained and does not depend on the state of an external system, or the result of other tests. This promotes modular testing and avoids flaky tests caused by the use of shared data.

  * It improves security and privacy. Synthetic data avoids the risks of exposing sensitive or production data in development or test environments.  This is particularly important for DataStage applications which commonly handle PII, health, or financial data.

To deliver these benefits MettleCI provides a comprehensive set of test data fabrication tools which support a wide range of use cases.  You can learn how to use these capabilities below.

Where you have additional data fabrication requirements, specific to your industry, organization, or team, MettleCI also enables you to develop your own custom data fabrication capabilities.

# Using MettleCI data fabrication

Data fabrication is a MettleCI capability accessed via the MettleCI Workbench’s unit test data editor.  This page provides a set of steps to using it.

#### Step-by-step instructions

1. When editing test data use the column overflow menu ( ⠇) to select edit column then under Data Generation Settings select your Generator Type.  The fabrication  tools listed, and their uses, are described in MettleCI’s data fabrication tools.
2. Note that some generators may prompt you for parameters which are available (or required) for you to customise their behaviour.  Where one or more parameters are mandatory the column editor panel on the right of the screen will not permit you to save your settings (and hence close the panel) until the mandatory parameters have been supplied.
3. When you have selected your generator type and provided any required parameters, click Save.

Back in the test data editor you can regenerate data using your supplied specification in one of three ways:

Right click the column header and select Regenerate data,

image-20250715-073543.png
Right click the table header (the unlabelled top-left header cell) and select Regenerate data, or

image-20250715-073510.png
Select a subset of cells by clicking and dragging in the table, then right click the table selection and select Regenerate data.

image-20250715-073630.png
Note that these data fabrication settings are evaluated once, at the time that you select the Regenerate data option in the MettleCI Workbench test data editor. Once invoked they will populate the selected test data table cells with appropriate values.  The test data fabricaction settings will NOT be stored in the test data table’s metadata definition and the data itself will remain static, even when depoyed to downstream systems.  The only way to regenerate the test data is to use the test data editory in a MettleCI Workbench instance.

Add label

---
status: reviewed
owner: John McKeever
tags:
  - DataStage
  - Creating Tests
  - Data Fabrication
---

# Introduction to Data Fabrication

There are many benefits to using artifically generated data in software unit testing:

- It enables the construction of **consistent and repeatable tests**. Fabricated data is predictable and avoids reliance on external systems like live databases or APIs.  This makes tests deterministic - exhibiting the same behaviour every time they’re run - which is critical for debugging and automation.

- It can **improve test coverage**. You can fabricate edge cases, boundary conditions, and unusual scenarios that may not be present in real datasets. This allows you to stress-test logic under various conditions such as empty strings, large inputs, and invalid values.

- It **increases testing speed and efficiency**. Tests run faster when they don’t have to query or populate real databases or APIs. The volume of your fabricated data can be optimised to supply no more and no less than is required to demonstrate your code’s correct behaviour, resulting in quicker execution, and consequently faster feedback, when used in CI/CD pipelines.

- It **supports test isolation**. Data fabrication ensures that each unit test is self-contained and does not depend on the state of an external system, or the result of other tests. This promotes modular testing and avoids flaky tests caused by the use of shared data.

- It **improves security and privacy**. Synthetic data avoids the risks of exposing sensitive or production data in development or test environments.  This is particularly important for DataStage applications which commonly handle PII, health, or financial data.

To deliver these benefits MettleCI provides a comprehensive set of [test data fabrication tools]() which support a wide range of use cases.  You can learn how to use these capabilities here.

Where you have additional data fabrication requirements, specific to your industry, organization, or team, MettleCI also enables you to [develop your own custom data fabrication capabilities](creating-custom-data-fabrication-tests.md).

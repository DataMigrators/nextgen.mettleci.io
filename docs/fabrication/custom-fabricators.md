---
status: reviewed #Status can be draft, reviewed or published. 
owner: John McKeever
tags:
  - Testing
  - Fabrication
---
# Creating Custom Data Fabricators

One of the many tools MettleCI provides for fabricating authentic-looking data is a comprehensive set of built-in data generators.  While these often fulfill many of the most common data fabrication requirements you may wish to create your own data fabrication generators to support your specific industry, organisation or team requirements.  This is easily achievable by supplying an appropriately formatted JSON file (called a ‘bundle file’) to the MettleCI Workbench, after which your new generators are immediately available in the MettleCI Workbench test data editor. 

#### A step-by-step guide to creating custom data generators

1. Create an appropriately-formatted JSON file
2. Test it on your local command line
3. Upload it to MettleCI Workbench
4. Use it in your test data specifications

We strongly encourage you to share your data generators with the DataStage community by committing them to the public GitHub repository at https://github.mettleci.io/datafab.

???+ warning "Warning"

    Please ensure any data generator definitions submitted to this public repository do not contain any Intellectual Property or Personally Identifiable Information.

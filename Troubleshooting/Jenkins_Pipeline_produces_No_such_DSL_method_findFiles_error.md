# Jenkins Pipeline produces \`No such DSL method 'findFiles'\` error

# Symptom

At the end of a Jenkins Pipeline deployment step (using the
`mettleci datastage deploy` command) you receive an error message that
looks like this...

``` java
Command failed.

No such DSL method 'findFiles' found among steps 
[acceptGitLabMR, addGitLabMRComment, archive, bat, build, ... ]
```

# Cause

Your Jenkins platform does not have the <a
href="https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#findfiles-find-files-in-the-workspace"
rel="nofollow">findFiles</a> command available as you don’t have the
<a href="https://plugins.jenkins.io/pipeline-utility-steps/"
rel="nofollow">Pipeline Utility Steps</a> plugin installed.

# Solution

Install the <a href="https://plugins.jenkins.io/pipeline-utility-steps/"
rel="nofollow">Pipeline Utility Steps</a> plugin in your Jenkins
platform.

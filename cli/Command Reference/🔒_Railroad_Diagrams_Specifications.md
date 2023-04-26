# 🔒 Railroad Diagrams Specifications

This is a note for DM documentation authors on how to create railroad
diagrams.

This is an INTERNAL ONLY page. Do not change the visibility of this
page.

Created at:

<a href="https://tabatkins.github.io/railroad-diagrams/generator.html"
rel="nofollow">https://tabatkins.github.io/railroad-diagrams/generator.html</a>

# Contents

-   [Generic
    Example](#id-🔒RailroadDiagramsSpecifications-GenericExample)
-   [Compliance
    Namespace](#id-🔒RailroadDiagramsSpecifications-ComplianceNamespace)
    -   [Compliance Query Command
        ✅](#id-🔒RailroadDiagramsSpecifications-ComplianceQueryCommand✅)
    -   [Compliance Report Card Command
        ✅](#id-🔒RailroadDiagramsSpecifications-ComplianceReportCardCommand✅)
    -   [Compliance Test Command
        ✅](#id-🔒RailroadDiagramsSpecifications-ComplianceTestCommand✅)
    -   [Compliance Console Command
        ✅](#id-🔒RailroadDiagramsSpecifications-ComplianceConsoleCommand✅)
-   [DataStage
    Namespace](#id-🔒RailroadDiagramsSpecifications-DataStageNamespace)
    -   [DataStage Connector Migration Command
        ✅](#id-🔒RailroadDiagramsSpecifications-DataStageConnectorMigrationCommand✅)
    -   [DataStage Cleanup-Projects Command
        ✅](#id-🔒RailroadDiagramsSpecifications-DataStageCleanup-ProjectsCommand✅)
    -   [DataStage Create-Project Command
        ✅](#id-🔒RailroadDiagramsSpecifications-DataStageCreate-ProjectCommand✅)
    -   [DataStage Compile Command
        ✅](#id-🔒RailroadDiagramsSpecifications-DataStageCompileCommand✅)
    -   [DataStage Delete-Project Command
        ✅](#id-🔒RailroadDiagramsSpecifications-DataStageDelete-ProjectCommand✅)
    -   [DataStage Deploy Command
        ✅](#id-🔒RailroadDiagramsSpecifications-DataStageDeployCommand✅)
    -   [DataStage Execute Command
        ✅](#id-🔒RailroadDiagramsSpecifications-DataStageExecuteCommand✅)
-   [Deploy
    Namespace](#id-🔒RailroadDiagramsSpecifications-DeployNamespace)
    -   [DevOps-Pipeline
        🧪](#id-🔒RailroadDiagramsSpecifications-DevOps-Pipeline🧪)
-   [DSParams
    Namespace](#id-🔒RailroadDiagramsSpecifications-DSParamsNamespace)
    -   [DSParams Delete Command
        ✅](#id-🔒RailroadDiagramsSpecifications-DSParamsDeleteCommand✅)
    -   [DSParams Diff Command
        ✅](#id-🔒RailroadDiagramsSpecifications-DSParamsDiffCommand✅)
    -   [DSParams Merge Command
        ✅](#id-🔒RailroadDiagramsSpecifications-DSParamsMergeCommand✅)
-   [ISX Namespace](#id-🔒RailroadDiagramsSpecifications-ISXNamespace)
    -   [ISX Cat Command
        ✅](#id-🔒RailroadDiagramsSpecifications-ISXCatCommand✅)
    -   [ISX Cut Command
        ✅](#id-🔒RailroadDiagramsSpecifications-ISXCutCommand✅)
    -   [ISX Export Command
        ❌](#id-🔒RailroadDiagramsSpecifications-ISXExportCommand❌)
    -   [ISX Import Command
        ❌](#id-🔒RailroadDiagramsSpecifications-ISXImportCommand❌)
    -   [ISX Message-Handlers Command
        ✅](#id-🔒RailroadDiagramsSpecifications-ISXMessage-HandlersCommand✅)
    -   [ISX Set-Params Command
        ❌](#id-🔒RailroadDiagramsSpecifications-ISXSet-ParamsCommand❌)
-   [Properties
    Namespace](#id-🔒RailroadDiagramsSpecifications-PropertiesNamespace)
    -   [Properties Configuration Command
        ❌](#id-🔒RailroadDiagramsSpecifications-PropertiesConfigurationCommand❌)
-   [Remote
    Namespace](#id-🔒RailroadDiagramsSpecifications-RemoteNamespace)
    -   [Remote Download Command
        ❌](#id-🔒RailroadDiagramsSpecifications-RemoteDownloadCommand❌)
    -   [Remote Execute Command
        ❌](#id-🔒RailroadDiagramsSpecifications-RemoteExecuteCommand❌)
    -   [Remote Upload Command
        ❌](#id-🔒RailroadDiagramsSpecifications-RemoteUploadCommand❌)
-   [UnitTest
    Namespace](#id-🔒RailroadDiagramsSpecifications-UnitTestNamespace)
    -   [UnitTest Test Command
        ❌](#id-🔒RailroadDiagramsSpecifications-UnitTestTestCommand❌)
    -   [UnitTest Generate Command
        ❌](#id-🔒RailroadDiagramsSpecifications-UnitTestGenerateCommand❌)
-   [Deprecated](#id-🔒RailroadDiagramsSpecifications-Deprecated)
    -   [Backlog Generation
        Command](#id-🔒RailroadDiagramsSpecifications-BacklogGenerationCommand)

------------------------------------------------------------------------

# Generic Example

Use these settings:

<img src="attachments/455311472/2224586875.png" class="image-center"
loading="lazy" data-image-src="attachments/455311472/2224586875.png"
data-height="193" data-width="681" data-unresolved-comment-count="0"
data-linked-resource-id="2224586875" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20220609-011647.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="455311472"
data-linked-resource-container-version="36"
data-media-id="12dd6359-12ea-4064-94c8-94b596f49b94"
data-media-type="file" />

To produce this diagram…

<img src="attachments/455311472/2226421775.png" class="image-center"
loading="lazy" data-image-src="attachments/455311472/2226421775.png"
data-height="279" data-width="1350" data-unresolved-comment-count="0"
data-linked-resource-id="2226421775" data-linked-resource-version="1"
data-linked-resource-type="attachment"
data-linked-resource-default-alias="image-20220609-071029.png"
data-base-url="https://datamigrators.atlassian.net/wiki"
data-linked-resource-content-type="image/png"
data-linked-resource-container-id="455311472"
data-linked-resource-container-version="36"
data-media-id="130c8ba8-25e4-4b70-89d0-628ec359604f"
data-media-type="file" />

Use this markup:

``` java
Diagram(
    NonTerminal('mettleci'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('namespace'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('command'), 
                    Choice(0,
                        'help',
                        Sequence(
                            MultipleChoice(0, 'all',
                                Sequence(NonTerminal('-mandatory_option_1'), '{value}'),
                                Sequence(NonTerminal('-mandatory_option_2'), '{value}'),
                                Sequence(NonTerminal('-mandatory_option_3'), '{value}')                        
                            ),
                            MultipleChoice(0, 'any',
                                Sequence(Skip()), 
                                Sequence(NonTerminal('-optional_value_1')),
                                Sequence(NonTerminal('-optional_value_2'), '{option_value}'),
                                Sequence(NonTerminal('-optional_value_3')),
                                Sequence(NonTerminal('-optional_value_4'), '{option_value}')
                            )
                        )
                    )
                )
            )
        )
    )
)
```

------------------------------------------------------------------------

# Compliance Namespace

## Compliance Query Command ✅

<a href="Compliance_Query_Command" data-linked-resource-id="458556115"
data-linked-resource-version="25"
data-linked-resource-type="page">Compliance Query Command</a>

``` java
Diagram(
    NonTerminal('mettleci'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('compliance'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('query'), 
                    Choice(0,
                        'help',
                            Sequence(
                                MultipleChoice(0, 'all',
                                Sequence(NonTerminal('-queries'), '{location of query files}'),
                                Sequence(NonTerminal('-assets'), '{location of ISX assets}'),
                                Sequence(NonTerminal('-report'), '{CSV output report name}')
                            ),
                            MultipleChoice(0, 'any',
                                Sequence(Skip()), 
                                Sequence(NonTerminal('-threads'), '{number of execution threads}')
                            )
                        )
                    )
                )
            )
        )
    )
)
```

## Compliance Report Card Command ✅

<a href="Compliance_ReportCard_Command_⛔️"
data-linked-resource-id="720994614" data-linked-resource-version="15"
data-linked-resource-type="page">Compliance Report Card Command</a>

``` java
Diagram(
    NonTerminal('mettleci'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('compliance'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('reportcard'), 
                    Choice(0,
                        'help',
                        Sequence(
                            MultipleChoice(0, 'all',
                                Sequence(NonTerminal('-zipfile'), '{filename}'),
                                Sequence(NonTerminal('-reportdir'), '{directory}'),
                                Sequence(NonTerminal('-client'), '{client name}'),
                                Sequence(NonTerminal('-email'), '{email}')
                            )
                        )
                    )
                )
            )
        )
    )
)
```

## Compliance Test Command ✅

<a href="Compliance_Test_Command" data-linked-resource-id="408322069"
data-linked-resource-version="29"
data-linked-resource-type="page">Compliance Test Command</a>

``` java
Diagram(
    NonTerminal('mettleci'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('compliance'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('test'), 
                    Choice(0,
                        'help',
                        Sequence(
                            MultipleChoice(0, 'all',
                                Sequence(NonTerminal('-rules'), '{location of compliance rules}'),
                                Sequence(NonTerminal('-assets'), '{location of ISX assets}'),
                                Sequence(NonTerminal('-report'), '{xml output report name}')                        
                            ),
                            MultipleChoice(0, 'any',
                                Sequence(Skip()), 
                                Sequence(NonTerminal('-junit')),
                                Sequence(NonTerminal('-project-cache'), '{number of execution threads}'),
                                Sequence(NonTerminal('-test-suite'), '{test suite label}'),
                                Sequence(NonTerminal('-ignore-test-failures')),
                                Sequence(NonTerminal('-include-job-in-test-name'))
                            )
                        )
                    )
                )
            )
        )
    )
)
```

## Compliance Console Command ✅

<a href="Compliance_Console_Command"
data-linked-resource-id="2422341633" data-linked-resource-version="5"
data-linked-resource-type="page">Compliance Console Command</a>

``` java
Diagram(
    NonTerminal('mettleci'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('compliance'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('console'), 
                    Choice(0,
                        'help',
                        Sequence(NonTerminal('-assets'), '{Directory or Zip containing project export}')
                    )
                )
            )
        )
    )
)
```

------------------------------------------------------------------------

# DataStage Namespace

## DataStage Connector Migration Command ✅

<a href="DataStage_Connector_Migration_Command"
data-linked-resource-id="410681364" data-linked-resource-version="23"
data-linked-resource-type="page">DataStage Connector Migration
Command</a>

``` java
Diagram(
    NonTerminal('mettleci'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('datastage'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('ccmt'), 
                                        Choice(0, 
                        Terminal('help'),
                        Sequence(
                            MultipleChoice(0, 'all', 
                                Sequence(NonTerminal('-domain'), '{domain}'),
                                Sequence(NonTerminal('-server'), '{engine tier}'),
                                Sequence(NonTerminal('-project'), '{project}'),
                                Sequence(NonTerminal('-username'), '{user}'),
                                Sequence(NonTerminal('-password'), '{password}'),
                                Sequence(NonTerminal('-logfile'), '{filename}'),
                                Sequence(NonTerminal('-isxdirectory'), '{directory}'),
                            ),
                            Optional(
                                Choice(0, 
                                    Sequence(NonTerminal('-param'), '{parameter}'),
                                    Sequence(NonTerminal('-project-cache'), '{directory}'),
                                    Sequence(NonTerminal('-threads'), '{number}'),
                                    Sequence(NonTerminal('-heapsize'), '{number}'),
                                    Sequence(NonTerminal('-noBatchThreshold'), '{path}'),
                                ),
                                'skip'
                            )
                        )
                    )
                )
            )
        )
    )
)
```

## DataStage Cleanup-Projects Command ✅

<a href="DataStage_Cleanup-Projects_Command"
data-linked-resource-id="458424418" data-linked-resource-version="14"
data-linked-resource-type="page">DataStage Cleanup-Projects Command</a>

``` java
Diagram(
    NonTerminal('mettleci'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('datastage'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('cleanup-projects'), 
                                        Choice(0, 
                        Terminal('help'),
                        Sequence(
                            MultipleChoice(0, 'all', 
                                Sequence(NonTerminal('-domain'), '{domain}'),
                                Sequence(NonTerminal('-server'), '{engine tier}'),
                                Sequence(NonTerminal('-project'), '{project}'),
                                Sequence(NonTerminal('-username'), '{user}'),
                                Sequence(NonTerminal('-password'), '{password}'),
                                Sequence(NonTerminal('-pattern'), '{filename}'),
                            ),
                            Optional(
                                Choice(0, 
                                Sequence(NonTerminal('-retain'), '{number}'),
                                ),
                                'skip'
                            )
                        )
                    )
                )
            )
        )
    )
)
```

## DataStage Create-Project Command ✅

<a href="DataStage_Delete-Project_Command"
data-linked-resource-id="458424387" data-linked-resource-version="18"
data-linked-resource-type="page">DataStage Delete-Project Command</a>

``` java
Diagram(
    NonTerminal('mettleci'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('datastage'),
            Choice(0,
                'help',
                Sequence(
                    NonTerminal('create-project'),
                    Choice(0, 
                        Terminal('help'),
                        Sequence(
                            MultipleChoice(0, 'all', 
                                Sequence(NonTerminal('-domain'), '{domain}'),
                                Sequence(NonTerminal('-server'), '{engine tier}'),
                                Sequence(NonTerminal('-project'), '{project}'),
                                Sequence(NonTerminal('-username'), '{user}'),
                                Sequence(NonTerminal('-password'), '{password}'),
                            ),
                            MultipleChoice(0, 'any',
                                Sequence(Skip()),
                                Sequence(NonTerminal('-path'), '{path}')
                            )
                        )
                    )
                )
            )
        )
    )
)
```

## DataStage Compile Command ✅

<a href="DataStage_Compile_Command" data-linked-resource-id="410157081"
data-linked-resource-version="33"
data-linked-resource-type="page">DataStage Compile Command</a>

``` java
Diagram(
    NonTerminal('mettleci'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('datastage'),
            Choice(0,
                'help',
                Sequence(
                    NonTerminal('compile'),
                    Choice(0, 
                        Terminal('help'),
                        Sequence(
                            MultipleChoice(0, 'all', 
                                Sequence(NonTerminal('-domain'), '{domain}'),
                                Sequence(NonTerminal('-server'), '{engine tier}'),
                                Sequence(NonTerminal('-project'), '{project}'),
                                Sequence(NonTerminal('-username'), '{user}'),
                                Sequence(NonTerminal('-password'), '{password}')
                            ),
                            MultipleChoice(0, 'any',
                                Sequence(Skip()),
                                Sequence(NonTerminal('-include_server_routines'), 'true/false'),
                                Sequence(NonTerminal('-provision_rulesets'), 'true/false')
                            )
                        )
                    )
                )
            )
        )
    )
)
```

## DataStage Delete-Project Command ✅

<a href="DataStage_Delete-Project_Command"
data-linked-resource-id="458424387" data-linked-resource-version="18"
data-linked-resource-type="page">DataStage Delete-Project Command</a>

``` java
Diagram(
    NonTerminal('mettleci'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('datastage'),
            Choice(0,
                'help',
                Sequence(
                    NonTerminal('delete-project'),
                    Choice(0, 
                        Terminal('help'),
                        Sequence(
                            MultipleChoice(0, 'all', 
                                Sequence(NonTerminal('-domain'), '{domain}'),
                                Sequence(NonTerminal('-server'), '{engine tier}'),
                                Sequence(NonTerminal('-project'), '{project}'),
                                Sequence(NonTerminal('-username'), '{user}'),
                                Sequence(NonTerminal('-password'), '{password}'),
                            )
                        )
                    )
                )
            )
        )
    )
)
```

## DataStage Deploy Command ✅

<a href="DataStage_Deploy_Command" data-linked-resource-id="423952410"
data-linked-resource-version="30"
data-linked-resource-type="page">DataStage Deploy Command</a>

``` java
Diagram(
    NonTerminal('mettleci'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('datastage'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('deploy'), 
                    Choice(0,
                        'help',
                        Sequence(
                            MultipleChoice(0, 'all',
                                Sequence(NonTerminal('-domain'), '{service tier}'),
                                Sequence(NonTerminal('-server'), '{engine tier}'),
                                Sequence(NonTerminal('-username'), '{username}'),
                                Sequence(NonTerminal('-password'), '{password}'),
                                Sequence(NonTerminal('-project'), '{project}'),
                                Sequence(NonTerminal('-assets'), '{directory}'),
                                Sequence(NonTerminal('-project-cache'), '{directory}')
                            ),
                            MultipleChoice(0, 'any',
                                Sequence(Skip()), 
                                Sequence(NonTerminal('-include-job-in-test-name')), 
                                Sequence(NonTerminal('-threads'), '{number}'),
                                Sequence(NonTerminal('-parameter-sets'), '{directory}')
                            )
                        )
                    )
                )
            )
        )
    )
)
```

## DataStage Execute Command ✅

<a href="DataStage_Execute_Command" data-linked-resource-id="458817755"
data-linked-resource-version="15"
data-linked-resource-type="page">DataStage Execute Command</a>

``` java
Diagram(
    NonTerminal('mettleci'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('datastage'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('execute'), 
                    Choice(0,
                        'help',
                        Sequence(
                            MultipleChoice(0, 'all',
                                Sequence(NonTerminal('-domain'), '{service tier}'),
                                Sequence(NonTerminal('-server'), '{engine tier}'),
                                Sequence(NonTerminal('-project'), '{project}'),
                                Sequence(NonTerminal('-username'), '{username}'),
                                Sequence(NonTerminal('-password'), '{password}'),
                                Sequence(NonTerminal('-project'), '{project}')
                                Sequence(NonTerminal('-jobname'), '{job}'),
                            ),
                            MultipleChoice(0, 'any',
                                Sequence(Skip()), 
                                Sequence(NonTerminal('-runmode'), '{runmode}'),
                                Sequence(NonTerminal('-param'), '{parameter}')
                            )
                        )
                    )
                )
            )
        )
    )
)
```

------------------------------------------------------------------------

# Deploy Namespace

## DevOps-Pipeline 🧪

``` java
Diagram(
    Sequence(NonTerminal('deploy'), NonTerminal('devops-pipeline')),
    Choice(0,
        Terminal('help'),
        Sequence(
            Comment('Bamboo Connection'),
            MultipleChoice(0, 'all',
                Sequence(NonTerminal('-bamboo'), '{url}'),
                Sequence(NonTerminal('-username'), '{string}'),
                Sequence(NonTerminal('-password'), '{string}'),
            ),
            Comment('Continuous Integration'),
            MultipleChoice(0, 'all',
                Sequence(NonTerminal('-plan-key'), '{string}'),
                Sequence(NonTerminal('-plan-name'), '{string}'),
                Sequence(NonTerminal('-source-repository'), '{string}'),
                Sequence(NonTerminal('-compliance-repository'), '{string}'),
                Sequence(NonTerminal('-datastage-install'), '{string}'),
                Sequence(NonTerminal('-bamboo-shared-credentials'), '{string}'),
            ),
            Optional(
                Choice(0, 
                    Sequence(NonTerminal('-project-key'), '{string}'),
                    Sequence(NonTerminal('-project-name'), '{string}'),
                ), 
                'skip'
            ),
            Comment('DataStage Project'),
            Optional(
                Choice(0, 
                    Sequence(NonTerminal('-datastage-server'), '{string}'),
                    Sequence(NonTerminal('-datastage-domain'), '{string}'),
                    Sequence(NonTerminal('-datastage-project'), '{string}'),
                ), 
                'skip'
            ),
            Comment('Continuous Delivery'),
            Optional(
                Sequence(
                    NonTerminal('-deployment-project'), '{string}',
                    OneOrMore(Sequence(NonTerminal('-E'), '{id}={name}'), Comment('Environment')),
                ),
                'skip'
            )
        )
    )
)
```

------------------------------------------------------------------------

# DSParams Namespace

## DSParams Delete Command ✅

``` java
Diagram(
    NonTerminal('mettleci'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('dsparams'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('delete'), 
                    Choice(0,
                        'help',
                        Sequence(
                            MultipleChoice(0, 'all',
                                Sequence(NonTerminal('-before'), '{filename}'),
                                Sequence(NonTerminal('-delete'), '{filename}'),
                                Sequence(NonTerminal('-after'), '{filename}'),
                            )
                        )
                    )
                )
            )
        )
    )
)
```

## DSParams Diff Command ✅

``` java
Diagram(
    NonTerminal('mettleci'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('dsparams'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('diff'), 
                    Choice(0,
                        'help',
                        Sequence(
                            MultipleChoice(0, 'all',
                                Sequence(NonTerminal('-before'), '{filename}'),
                                Sequence(NonTerminal('-after'), '{filename}'),
                                Sequence(NonTerminal('-diff'), '{filename}')
                            )
                        )
                    )
                )
            )
        )
    )
)
```

## DSParams Merge Command ✅

``` java
Diagram(
    NonTerminal('mettleci'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('dsparams'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('merge'), 
                    Choice(0,
                        'help',
                        Sequence(
                            MultipleChoice(0, 'all',
                                Sequence(NonTerminal('-before'), '{filename}'),
                                Sequence(NonTerminal('-diff'), '{filename}'),
                                Sequence(NonTerminal('-after'), '{filename}'),
                            )
                        )
                    )
                )
            )
        )
    )
)
```

------------------------------------------------------------------------

# ISX Namespace

## ISX Cat Command ✅

``` java
Diagram(
    NonTerminal('mettleci'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('isx'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('cat'), 
                    Choice(0,
                        'help',
                        Sequence(
                            MultipleChoice(0, 'all',
                                MultipleChoice(0, 'any',
                                    Sequence(NonTerminal('-pattern'), '{pattern}')
                                ),
                                Sequence(NonTerminal('-isx'), '{filename}')
                            ),
                            Choice(0,
                                Sequence(Skip()), 
                                Sequence(NonTerminal('-fqDedupe')),
                            )
                        )
                    )
                )
            )
        )
    )
)
```

## ISX Cut Command ✅

``` java
Diagram(
    NonTerminal('mettleci'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('isx'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('cut'), 
                    Choice(0,
                        'help',
                        Sequence(
                            MultipleChoice(0, 'all',
                                Sequence(NonTerminal('-dir'), '{directory}'),
                                Sequence(NonTerminal('-isx'), '{filename}')
                            )
                        )
                    )
                )
            )
        )
    )
)
```

## ISX Export Command ❌

``` java
```

## ISX Import Command ❌

``` java
```

## ISX Message-Handlers Command ✅

``` java
Diagram(
    NonTerminal('mettleci'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('isx'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('message-handlers'), 
                    Choice(0,
                        'help',
                        Sequence(
                            MultipleChoice(0, 'all',
                                Sequence(NonTerminal('-isx'), '{directory}'),
                                Sequence(NonTerminal('-msh'), '{directory}'),
                            )
                        )
                    )
                )
            )
        )
    )
)
```

## ISX Set-Params Command ❌

``` java
```

------------------------------------------------------------------------

# Properties Namespace

## Properties Configuration Command ❌

``` java
Diagram(
    NonTerminal('mettleci'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('properties'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('config'), 
                    Choice(0,
                        'help',
                        Sequence(
                            MultipleChoice(0, 'all',
                                Sequence(NonTerminal('-baseDir'), '{filename}'),
                                MultipleChoice(0, 'any',
                                    Sequence(NonTerminal('-filerPattern'), '{pattern}')
                                ),
                                Sequence(NonTerminal('-properties'), '{filename}'),
                                Sequence(NonTerminal('-outDir'), '{directory}'),
                            )
                        )
                    )
                )
            )
        )
    )
)
```

------------------------------------------------------------------------

# Remote Namespace

## Remote Download Command ❌

``` java
```

## Remote Execute Command ❌

``` java
```

## Remote Upload Command ❌

``` java
```

------------------------------------------------------------------------

# UnitTest Namespace

## UnitTest Test Command ❌

``` java
```

## UnitTest Generate Command ❌

``` java
```

------------------------------------------------------------------------

# Deprecated

## Backlog Generation Command

``` java
Diagram(
    Sequence(NonTerminal('shell'), NonTerminal('rdu-backlog')),
    Choice(0,
        Terminal('help'),
        Sequence(
            NonTerminal('api'),
            MultipleChoice(0, 'all', 
                Sequence(NonTerminal('-reportcard'), '{file.json}'),
                Sequence(NonTerminal('-jiraurl'), '{URL}'),
                Sequence(NonTerminal('-project'), '{project}'),
                Sequence(NonTerminal('-username'), '{user}'),
                Sequence(NonTerminal('-password'), '{password}')
            )
       ),
        Sequence(
            NonTerminal('csv'),
            MultipleChoice(0, 'all', 
                Sequence(NonTerminal('-reportcard'), '{file.json}'),
                Sequence(NonTerminal('-output'), '{file.csv}'),
            )
        )
    )
)
```

## Attachments:

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220609-011431.png](attachments/455311472/2223603941.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220609-011558.png](attachments/455311472/2227011585.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220609-011647.png](attachments/455311472/2224586875.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220609-070603.png](attachments/455311472/2226323524.png)
(image/png)  
<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[image-20220609-071029.png](attachments/455311472/2226421775.png)
(image/png)  

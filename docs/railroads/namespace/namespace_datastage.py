import cairosvg
from railroad import *

DATASTAGE_CAPTURE = Diagram(
    NonTerminal('mcix'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('datastage'),
            Choice(0, 
                Terminal('help'),
                Sequence(
                    NonTerminal('capture'), 
                    Choice(0,
                        'help',
                        Sequence(
                            MultipleChoice(0, 'all',
                                Sequence(NonTerminal('-domain'), '{service tier}'),
                                Sequence(NonTerminal('-server'), '{engine tier}'),
                                Sequence(NonTerminal('-username'), '{username}'),
                                Sequence(NonTerminal('-password'), '{password}'),
                                Sequence(NonTerminal('-project'), '{project}'),
                                Sequence(NonTerminal('-location'), '{directory}'),
                                Sequence(NonTerminal('-project-cache'), '{directory}')
                            ),
                            MultipleChoice(0, 'any',
                                Sequence(Skip()), 
                                Sequence(NonTerminal('-threads'), '{number}')
                            )
                        )
                    )
                )
            )
        )
    )
)

DATASTAGE_CCMT = Diagram(
    NonTerminal('mcix'),
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

DATASTAGE_CLEANUP_PROJECTS = Diagram(
    NonTerminal('mcix'),
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

DATASTAGE_CREATE_PROJECT = Diagram(
    NonTerminal('mcix'),
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

DATASTAGE_COMPILE = Diagram(
    NonTerminal('mcix'),
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

DATASTAGE_DELETE_PROJECT = Diagram(
    NonTerminal('mcix'),
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

DATASTAGE_DEPLOY = Diagram(
    NonTerminal('mcix'),
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

DATASTAGE_EXECUTE = Diagram(
    NonTerminal('mcix'),
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
                                Sequence(NonTerminal('-project'), '{project}'),
                                Sequence(NonTerminal('-jobname'), '{job}')
                            ),
                            MultipleChoice(0, 'any',
                                Sequence(Skip()), 
                                Sequence(NonTerminal('-runmode'), 'NORMAL|RESET|RESTART|VALIDATE'),
                                Sequence(NonTerminal('-param'), '{parameter}')
                            )
                        )
                    )
                )
            )
        )
    )
)

datastage = {
    'datastage-capture': DATASTAGE_CAPTURE,
    'datastage-ccmt': DATASTAGE_CCMT,
    'datastage-cleanup-projects': DATASTAGE_CLEANUP_PROJECTS,
    'datastage-create-project': DATASTAGE_CREATE_PROJECT,
    'datastage-compile': DATASTAGE_COMPILE,
    'datastage-delete-project': DATASTAGE_DELETE_PROJECT,
    'datastage-deploy': DATASTAGE_DEPLOY,
    'datastage-execute': DATASTAGE_EXECUTE
}
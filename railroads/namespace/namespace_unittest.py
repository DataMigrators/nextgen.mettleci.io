import cairosvg
from railroad import *

UNITTEST_GENERATE = Diagram(
    NonTerminal('mettleci'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('unittest'),
            Choice(0,
                'help',
                Sequence(
                    NonTerminal('generate'),
                    Choice(0, 
                        Terminal('help'),
                        Sequence(
                            MultipleChoice(0, 'all', 
                                Sequence(NonTerminal('-specs'), '{path}'),
                                Sequence(NonTerminal('-assets'), '{path}')
                            ),
                            MultipleChoice(0, 'any',
                                Sequence(Skip()),
                                Sequence(NonTerminal('-joblist'), '{path}'),
                                NonTerminal('-check-row-count-only'),
                            )
                        )
                    )
                )
            )
        )
    )
)

UNITTEST_INSTALL_SERVER_TEST_HARNESS = Diagram(
    NonTerminal('mettleci'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('unittest'),
            Choice(0,
                'help',
                Sequence(
                    NonTerminal('install-server-test-harness'),
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
                                NonTerminal('-skip-stage-type-updater'),
                                NonTerminal('-trust')
                            )
                        )
                    )
                )
            )
        )
    )
)

UNITTEST_MIGRATE = Diagram(
    NonTerminal('mettleci'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('unittest'),
            Choice(0,
                'help',
                Sequence(
                    NonTerminal('migrate'),
                    Choice(0, 
                        Terminal('help'),
                        Sequence(
                            MultipleChoice(0, 'all', 
                                Sequence(NonTerminal('-url'), '{url}'),
                                Sequence(NonTerminal('-user'), '{username}'),
                                Sequence(NonTerminal('-api-key'), '{apikey}'),
                                Sequence(NonTerminal('-specs'), '{path}'),
                                Sequence(NonTerminal('-test-data-archive'), '{path}'),
                            ),
                            MultipleChoice(0, 'any',
                                Sequence(Skip()),
                                Sequence(NonTerminal('-project-id'), '{projectid}'),
                                Sequence(NonTerminal('-project'), '{projectname}'),
                            )
                        )
                    )
                )
            )
        )
    )
)

UNITTEST_TEST = Diagram(
    NonTerminal('mettleci'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('unittest'),
            Choice(0,
                'help',
                Sequence(
                    NonTerminal('test'),
                    Choice(0, 
                        Terminal('help'),
                        Sequence(
                            MultipleChoice(0, 'all', 
                                Sequence(NonTerminal('-domain'), '{domain}'),
                                Sequence(NonTerminal('-server'), '{engine tier}'),
                                Sequence(NonTerminal('-project'), '{project}'),
                                Sequence(NonTerminal('-username'), '{user}'),
                                Sequence(NonTerminal('-password'), '{password}'),
                                Sequence(NonTerminal('-specs'), '{path}'),
                                Sequence(NonTerminal('-reports'), '{path}'),
                            ),
                            MultipleChoice(0, 'any',
                                Sequence(Skip()),
                                Sequence(NonTerminal('-project-cache'), '{path}'),
                                Sequence(NonTerminal('-test-suite'), '{name}'),
                                Sequence(NonTerminal('-threads'), '{threads}'),
                                NonTerminal('-ignore-test-failures')
                            )
                        )
                    )
                )
            )
        )
    )
)

UNITTEST_UNINSTALL_SERVER_TEST_HARNESS = Diagram(
    NonTerminal('mettleci'),
    Choice(0,
        'help',
        Sequence(
            NonTerminal('unittest'),
            Choice(0,
                'help',
                Sequence(
                    NonTerminal('uninstall-server-test-harness'),
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
                            Optional(
                                NonTerminal('-trust')
                            )
                        )
                    )
                )
            )
        )
    )
)


unittest = { 
    'unittest-generate': UNITTEST_GENERATE,
    'unittest-install-server-test-harness': UNITTEST_INSTALL_SERVER_TEST_HARNESS,
    'unittest-migrate': UNITTEST_MIGRATE,
    'unittest-test': UNITTEST_TEST,
    'unittest-uninstall-server-test-harness': UNITTEST_UNINSTALL_SERVER_TEST_HARNESS
}
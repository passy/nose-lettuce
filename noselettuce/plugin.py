# -*- coding: utf-8 -*-
"""
noselettuce.plugin
~~~~~~~~~~~~~~~~~~

Nose plugin implementation.

:copyright: 2010, Pascal Hartig <phartig@rdrei.net>
:license: BSD, see LICENSE for more details.
"""

from nose.plugins import Plugin
import lettuce
import os


class LettucePlugin(Plugin):
    """Issues the lettuce runner in addition to the default test runner."""

    name = "lettuce"
    score = 100

    def options(self, parser, env):
        """Add plugin specific options."""

        parser.add_option('--lettuce-path',
                          help=("Set the base path for feature discovery. "
                                "Default: ./features"),
                          dest='lettuce_path')

        parser.add_option('--lettuce-verbosity',
                          default=4,
                          help="Set the verbosity for the lettuce runner.",
                          dest='lettuce_verbosity')

        parser.add_option('--scenarios',
                          help="Comma seperated list of scenarios to run.",
                          dest="lettuce_scenarios")

        Plugin.options(self, parser, env)

    def configure(self, options, conf):
        """Set the configuration"""

        if options.lettuce_path:
            self._base_path = options.lettuce_path
        else:
            self._base_path = os.path.join(self.conf.workingDir, "features")

        conf.lettuce_verbosity = options.lettuce_verbosity
        conf.lettuce_scenarios = options.lettuce_scenarios
        Plugin.configure(self, options, conf)

    def prepareTestRunner(self, runner):
        """Create and run the lettuce runner."""

        lrunner = lettuce.Runner(self._base_path,
                                 verbosity=self.conf.lettuce_verbosity,
                                 scenarios=self.conf.lettuce_scenarios)
        lrunner.run()

        return runner

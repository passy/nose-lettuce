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


class LettucePlugin(Plugin):
    """Issues the lettuce runner in addition to the default test runner."""

    def prepareTestRunner(self):
        """Create and run the lettuce runner."""

        # These values should be configurable.
        base_path = "."
        verbosity = 4

        runner = lettuce.Runner(base_path, verbosity=verbosity)
        return runner

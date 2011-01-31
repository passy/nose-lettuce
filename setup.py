# -*- coding: utf-8 -*-
"""
nose-lettuce
~~~~~~~~~~~~

A nose plugin to run your lettuce suite with.


:copyright: 2011, Pascal Hartig <phartig@rdrei.net>
:license: BSD, see LICENSE for more details
"""

from setuptools import setup
from noselettuce import __version__


setup(
    name="nose-lettuce",
    version=__version__,
    author="Pascal Hartig",
    author_email="phartig@rdrei.de",
    description="Issue the lettuce test runner from nose",
    url="http://github.com/passy/nose-lettuce",
    packages=['noselettuce'],
    long_description=__doc__,
    requires=['nose (>=0.10)'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.6",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    entry_points={
        'nose.plugins.0.10': [
            'notify = noselettuce.plugin:LettucePlugin'
        ]
    }
)

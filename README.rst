============
nose-lettuce
============

I'm not really sold on this idea, but I needed something like this. Why? Read
below.
``nose-lettuce`` is, obviously, a nose plugin that runs lettuce tests. It
actually just starts the lettuce runner before the usual nose tests are run.

When is this useful?
====================

This is useful if you rely on certain other nose plugins, like coverage_ to
measure the test coverage of both your lettuce and normal nose tests or
nosegae_ to setup a GAE testing environment so you can access the GAE data store
from the lettuce tests.

.. _coverage: http://nedbatchelder.com/code/coverage/
.. _nosegae: http://farmdev.com/projects/nosegae/

How to use it
=============

Installation
------------

Not released to PyPI yet, so you have to install from github::

   pip install https://github.com/passy/nose-lettuce/tarball/master

Usage
-----

To run the plugin, just append ``--with-lettuce`` to your ``nosetests`` command
or set the ``NOSE_WITH_LETTUCE`` environment variable. In order to see any
results, you must have set the ``--nocapture`` option (short: ``-s``).

+---------------------------------------+---------------------------------------------------------+
| Option                                | Description                                             |
+=======================================+=========================================================+
| --with-lettuce                        | Enables the plugin                                      |
+---------------------------------------+---------------------------------------------------------+
| --lettuce-path=LETTUCE_PATH           | Sets the base path for feature discovery.               |
|                                       | (Default: features/ in your current working directory.) |
+---------------------------------------+---------------------------------------------------------+
| --lettuce-verbosity=LETTUCE_VERBOSITY | Changes the verbosity of the output.                    |
+---------------------------------------+---------------------------------------------------------+
| --lettuce-scenarios=LETTUCE_SCENARIOS | Comma seperated list of scenarios to run.               |
+---------------------------------------+---------------------------------------------------------+

Example
~~~~~~~

::

   nosetests --with-lettuce --lettuce-path=myapp/features -s myapp/

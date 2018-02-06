#!/usr/bin/env python3.6

"""
Utility to test this scripts package itself.

Usage:
    test...
            run tests: `./tests_runner.py test`
            check types: `./tests_runner.py types`
"""

import os
import sys

# path hack, https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from scripts.utils import prereq_checker, venv, sys_calls, command_line_args


def main() -> None:
    parser = command_line_args.create_parser(command_map)
    args = parser.parse_args()
    check_prereqs_installed()
    command_line_args.execute_command(args, command_map)


# -------------------------------------
# Required software
# -------------------------------------

def check_prereqs_installed() -> None:
    """
    Confirms all required software installed.
    """
    prereq_checker.check_is_installed(['python3'], windows_support=False)
    prereq_checker.check_is_installed(['python'], posix_support=False)
    command_line_args.check_prereqs_installed()
    sys_calls.check_prereqs_installed()
    venv.check_prereqs_installed()


# -------------------------------------
# Test commands
# -------------------------------------

def check_types() -> None:
    """
    Calls MyPy to check for type errors.
    """
    venv.activate()
    sys_calls.run(["mypy", "--strict-optional", "--ignore-missing-imports",
                   "--package", "scripts"])


def test() -> None:
    """
    Run unit tests.
    """
    if sys_calls.is_windows_environment():
        py = 'python'
    else:
        py = 'python3'
    sys_calls.run([py, '-m', 'unittest', 'discover', 'scripts/tests'])


# -------------------------------------
# Command line options
# -------------------------------------
command_map = command_line_args.CommandMap({'test': test,
                                            'types': check_types,
                                            })

# -------------------------------------
# Run script
# -------------------------------------

if __name__ == '__main__':
    main()

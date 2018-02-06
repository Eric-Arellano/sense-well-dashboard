"""
Utilities to accept and parse command line arguments.
"""

import argparse
from typing import Callable, Dict, NewType

CommandMap = NewType('CommandMap', Dict[str, Callable[..., None]])


# -----------------------------------------------------------------
# Check prereqs installed
# -----------------------------------------------------------------

def check_prereqs_installed() -> None:
    """
    Confirm all required software installed.
    """
    pass


# -------------------------------------
# Parser
# -------------------------------------

def create_parser(command_map: CommandMap, *,
                  accept_target_environment: bool = False) -> argparse.ArgumentParser:
    """
    Setups command line argument parser and assigns defaults and help statements.
    """
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('command',
                        default='run',
                        nargs='?',  # must specify 0-1 argument
                        choices=command_map.keys())
    parser.add_argument('dependencies',
                        default='',
                        nargs='*',  # can specify 0-many arguments
                        help='Dependency(ies) you want to modify.')
    if accept_target_environment:
        parser.add_argument('-t', '--target',
                            default='all',
                            nargs='?',  # must specify 0-1 argument
                            choices=['all', 'backend', 'frontend', 'script'])
    return parser


# -------------------------------------
# Execute command
# -------------------------------------

def execute_command(args: argparse.Namespace,
                    command_map: CommandMap) -> None:
    """
    Determines which command was passed and then executes the command.

    Passes any additional parameters, such as target environment or dependencies.
    """
    func = command_map[args.command]
    # convert arguments to dict
    passed_arguments = vars(args)
    # remove empty values
    additional_arguments = {k: v for k, v in passed_arguments.items() if v}
    # remove command
    del additional_arguments['command']
    # unpack additional arguments into function as named parameters
    func(**additional_arguments)

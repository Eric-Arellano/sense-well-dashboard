#!/usr/bin/env python3.6

"""
Utility to run, install, test, and manage dependencies for the Flask backend.

Usage:
    run...
            normal: `backend.py`
            detached mode: `backend.py detached`
            stop detached: `backend.py stop`
    install...
            install: `./backend.py install`
    test...
            unit tests: `./backend.py test`
            check types: `./backend.py types`
    dependency management...
            catchup: `./backend.py catchup`
            view outdated: `./backend.py outdated`
            view dependency tree: `./backend.py deptree`
            add: `./backend.py add [package(s)]`
            upgrade: `./backend.py upgrade [package(s)]`
            remove: `./backend.py remove [package(s)]`
"""

import os
import sys
from typing import List

# path hack, https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from scripts.utils import prereq_checker, process_management, git, sys_calls, venv, command_line_args


def main() -> None:
    parser = command_line_args.create_parser(command_map)
    args = parser.parse_args()
    check_prereqs()
    command_line_args.execute_command(args, command_map)


# -------------------------------------
# Required software
# -------------------------------------

def check_prereqs() -> None:
    """
    Confirms all required software installed.
    """
    prereq_checker.check_is_installed(['python3'], windows_support=False)
    prereq_checker.check_is_installed(['python'], posix_support=False)
    command_line_args.check_prereqs_installed()
    process_management.check_prereqs_installed()
    git.check_prereqs_installed()
    sys_calls.check_prereqs_installed()
    venv.check_prereqs_installed()


# -------------------------------------
# Run commands
# -------------------------------------

def run() -> None:
    """
    Start backend server normally.
    """
    venv.activate()
    os.environ['FLASK_APP'] = 'backend/src/app.py'
    try:
        sys_calls.run(["flask", "run"])
    except KeyboardInterrupt:
        pass


def run_detached() -> None:
    """
    Start backend server in detached mode, meaning it will not output anything.

    Must later kill process.
    """
    venv.activate()
    os.environ['FLASK_APP'] = 'backend/src/app.py'
    sys_calls.run_detached(["flask", "run"])
    print("Backend server started at localhost:5000. Remember to stop it after.")


def stop() -> None:
    """
    Stop detached backend server by searching PID on port 5000 and then killing process.
    """
    pid = process_management.find_pid_on_port('5000')
    process_management.kill_process(pid)
    print("Backend server stopped at localhost:5000.")


# -------------------------------------
# Install commands
# -------------------------------------

def install() -> None:
    """
    Downloads & installs all dependencies for the backend.
    """
    venv.create()
    venv.activate()
    sys_calls.run(["pip", "install", "-r", "requirements.txt"])


# -------------------------------------
# Test commands
# -------------------------------------

def check_types() -> None:
    """
    Calls MyPy to check for type errors.
    """
    venv.activate()
    sys_calls.run(["mypy", "--strict-optional", "--ignore-missing-imports",
                   "--package", "src"], cwd='backend/')


def test() -> None:
    """
    Run unit tests.
    """
    venv.activate()
    if sys_calls.is_windows_environment():
        py = 'python'
    else:
        py = 'python3'
    sys_calls.run([py, '-m', 'unittest', 'discover', 'tests'], cwd='backend/')


# -------------------------------------
# Dependency management commands
# -------------------------------------
Dependency = str  # type alias


def _freeze_requirements() -> None:
    """
    Updates the requirements.txt file with new dependencies.
    """
    with open('requirements.txt', 'w') as requirements:
        sys_calls.run(['pip', 'freeze'], stdout=requirements)
    git.remind_to_commit("requirements.txt")


def catchup() -> None:
    """
    Check if any new pip dependencies added from others remotely, and then install them if so.
    """
    # TODO: pull from master
    # TODO: actually check for differences in requirements.txt
    venv.activate()
    sys_calls.run(["pip", "install", "-r", "requirements.txt"])


def list_outdated() -> None:
    """
    List pip packages that should be updated.
    """
    venv.activate()
    sys_calls.run(["pip", "list", "--outdated", "--format=columns"])


def dependency_tree() -> None:
    """
    Visualize which dependencies depend upon which.
    """
    venv.activate()
    sys_calls.run(["pipdeptree"])


def add(dependencies: List[Dependency]) -> None:
    """
    Add one or more pip packages.
    """
    venv.activate()
    sys_calls.run(["pip", "install"] + dependencies)
    _freeze_requirements()


def upgrade(dependencies: List[Dependency]) -> None:
    """
    Upgrade one or more out-of-date pip packages.
    """
    venv.activate()
    sys_calls.run(["pip", "install", "--upgrade"] + dependencies)
    _freeze_requirements()


def remove(dependencies: List[Dependency]) -> None:
    """
    Remove one or more pip packages.
    """
    venv.activate()
    sys_calls.run(["pip", "uninstall"] + dependencies)
    _freeze_requirements()


# -------------------------------------
# Command line options
# -------------------------------------
command_map = command_line_args.CommandMap({'run': run,
                                            'detached': run_detached,
                                            'stop': stop,
                                            'install': install,
                                            'test': test,
                                            'types': check_types,
                                            'catchup': catchup,
                                            'outdated': list_outdated,
                                            'deptree': dependency_tree,
                                            'add': add,
                                            'upgrade': upgrade,
                                            'remove': remove
                                            })

# -------------------------------------
# Run script
# -------------------------------------

if __name__ == '__main__':
    main()

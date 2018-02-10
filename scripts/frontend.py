#!/usr/bin/env python3.6

"""
Utility to run, install, test, and manage dependencies for the React frontend.

Usage:
    run...
            normal: `frontend.py`
            detached mode: `frontend.py detached`
            stop detached: `frontend.py stop`
    install...
            install: `./frontend.py install`
            build: `./frontend.py build`
            catchup: `./frontend.py catchup`
    test...
            check types: `./frontend.py types`
    dependency management...
            view outdated: `./frontend.py outdated`
            add: `./frontend.py add [package(s)]`
            upgrade: `./frontend.py upgrade [package(s)]`
            remove: `./frontend.py remove [package(s)]`
"""

import os
import sys
from typing import List

# path hack, https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from scripts.utils import prereq_checker, process_management, git, command_line_args, sys_calls, files


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
    prereq_checker.check_is_installed(['yarn', 'npm', 'node'])
    command_line_args.check_prereqs_installed()
    git.check_prereqs_installed()
    process_management.check_prereqs_installed()
    sys_calls.check_prereqs_installed()
    files.check_prereqs_installed()


# -------------------------------------
# Run commands
# -------------------------------------

def run() -> None:
    """
    Start frontend server normally.
    """
    try:
        sys_calls.run(["yarn", "start"], cwd='frontend/')
    except KeyboardInterrupt:
        pass


def run_detached() -> None:
    """
    Start frontend server in detached mode, meaning it will not output anything.

    Must later kill process.
    """
    sys_calls.run_detached(['yarn', 'start'], cwd='frontend/')
    print("Frontend server started at localhost:3000. Remember to stop it after.")


def stop() -> None:
    """
    Stop detached frontend server by searching PID on port 3000 and then killing process.
    """
    pid = process_management.find_pid_on_port('3000')
    process_management.kill_process(pid)
    print("Frontend server stopped at localhost:3000.")


# -------------------------------------
# Install commands
# -------------------------------------

def install() -> None:
    """
    Downloads & installs all dependencies for the frontend.
    """
    sys_calls.run(["yarn", "install"], cwd='frontend/')


def reinstall() -> None:
    """
    Deletes original packages and re-installs everything.
    """
    files.remove(['frontend/node_modules/'])
    install()


def build() -> None:
    """
    Builds frontend into two minified files, allowing the backend to render frontend.
    """
    sys_calls.run(["yarn", "build"], cwd='frontend/')


def catchup() -> None:
    """
    Check server for changes, and install new dependencies if necessary.
    """
    if not git.is_clean_local():
        raise SystemExit('Must first commit your changes before catching up.')
    old_hash = git.get_file_hash('frontend/package.json')
    git.fast_forward('origin', git.get_current_branch())
    new_hash = git.get_file_hash('frontend/package.json')
    if old_hash != new_hash:
        sys_calls.run(["yarn", "install"])


# -------------------------------------
# Test commands
# -------------------------------------

def check_types() -> None:
    """
    Calls Flow to check for type errors.
    """
    sys_calls.run(["yarn", "flow"], cwd='frontend/')


# -------------------------------------
# Dependency management
# -------------------------------------
Dependency = str  # type alias


def list_outdated() -> None:
    """
    List npm packages that should be updated.
    """
    sys_calls.run(["yarn", "outdated"], cwd='frontend/')


def add(dependencies: List[Dependency]) -> None:
    """
    Add one or more npm packages.
    """
    sys_calls.run(["yarn", "add"] + dependencies, cwd='frontend/')
    git.remind_to_commit("package.json and yarn.lock")


def upgrade(dependencies: List[Dependency]) -> None:
    """
    Upgrade one or more out-of-date npm packages.
    """
    sys_calls.run(["yarn", "upgrade"] + dependencies, cwd='frontend/')
    git.remind_to_commit("package.json and yarn.lock")


def remove(dependencies: List[Dependency]) -> None:
    """
    Remove one or more npm packages.
    """
    sys_calls.run(["yarn", "remove"] + dependencies, cwd='frontend/')
    git.remind_to_commit("package.json and yarn.lock")


# -------------------------------------
# Command line options
# -------------------------------------
command_map = command_line_args.CommandMap({'run': run,
                                            'detached': run_detached,
                                            'stop': stop,
                                            'install': install,
                                            'reinstall': reinstall,
                                            'catchup': catchup,
                                            'build': build,
                                            'types': check_types,
                                            'outdated': list_outdated,
                                            'add': add,
                                            'upgrade': upgrade,
                                            'remove': remove
                                            })

# -------------------------------------
# Run script
# -------------------------------------

if __name__ == '__main__':
    main()

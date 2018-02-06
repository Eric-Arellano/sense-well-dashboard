#!/usr/bin/env python3.6

"""
Top level script to install, run, test, deploy, update, and manage dependencies
for the whole app and its backend and frontend.

Commands follow the syntax:
    `./run.py [command] [-t target]`, where
        [target] = [all|backend|frontend|script] with default to `all`
        [command] = one of the valid commands with default to `run`

Usage:
    run...
            run (detached): `./run.py [--target backend|frontend]`
            stop: `./run.py stop [--target backend|frontend]`
    install...
            install: `./run.py install [--target backend|frontend] `
    test...
            run tests: `./run.py test [--target backend|script]`
            check types: `./run.py types [--target backend|frontend]`
    dependency management...
            catchup: `./run.py catchup [--target backend|frontend]`
            view outdated: `./run.py outdated [--target backend|frontend]`
            add: `./run.py add package1 [package2..] --target backend|frontend`
            upgrade: `./run.py upgrade package1 [package2..] --target backend|frontend`
            remove: `./run.py remove package1 [package2..] --target backend|frontend`
    deploy...
            deploy: `./run.py deploy`

"""
from typing import Callable, List

from scripts import backend, deploy, frontend, scripts_test_runner
from scripts.utils import command_line_args


def main() -> None:
    parser = command_line_args.create_parser(command_map, accept_target_environment=True)
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
    backend.check_prereqs()
    frontend.check_prereqs_installed()
    deploy.check_prereqs_installed()
    scripts_test_runner.check_prereqs_installed()
    command_line_args.check_prereqs_installed()


# -------------------------------------
# Determine target environment
# -------------------------------------

Target = str


def execute_on_target_environment(target: Target = 'all', *,
                                  all_action: Callable = None,
                                  backend_action: Callable = None,
                                  frontend_action: Callable = None,
                                  script_action: Callable = None,
                                  dependencies: List[str] = None) -> None:
    action = {
        'all': all_action,
        'backend': backend_action,
        'frontend': frontend_action,
        'script': script_action
    }[target]
    if action is None:
        raise TypeError(f'{target} target not supported with this command.')
    if not dependencies:
        action()
    else:
        action(dependencies=dependencies)


# -------------------------------------
# Run commands
# -------------------------------------

def run(*, target: Target = 'all') -> None:
    """
    Runs app in detached mode.
    """
    execute_on_target_environment(target,
                                  all_action=lambda: (
                                      backend.run_detached(),
                                      frontend.run_detached()),
                                  backend_action=backend.run_detached,
                                  frontend_action=frontend.run_detached)


def stop(*, target: Target = 'all') -> None:
    """
    Stops detached servers on specified target environment.
    """
    execute_on_target_environment(target,
                                  all_action=lambda: (
                                      backend.stop(),
                                      frontend.stop()),
                                  backend_action=backend.stop,
                                  frontend_action=frontend.stop)


# -------------------------------------
# Install commands
# -------------------------------------

def install(*, target: Target = 'all') -> None:
    """
    Install everything needed for the app to function.
    """
    execute_on_target_environment(target,
                                  all_action=lambda: (
                                      backend.install(),
                                      frontend.install()),
                                  backend_action=backend.install,
                                  frontend_action=frontend.install)


# -------------------------------------
# Test commands
# -------------------------------------


def test(*, target: Target = 'all') -> None:
    """
    Run unit tests for specified environment.
    """
    execute_on_target_environment(target,
                                  all_action=lambda: (
                                      backend.test(),
                                      scripts_test_runner.test()),
                                  backend_action=backend.test,
                                  script_action=scripts_test_runner.test)


def check_types(*, target: Target = 'all') -> None:
    """
    Call Flow and MyPy to check type safety of app.
    """
    execute_on_target_environment(target,
                                  all_action=lambda: (
                                      backend.check_types(),
                                      frontend.check_types(),
                                      scripts_test_runner.check_types()),
                                  backend_action=backend.check_types,
                                  frontend_action=frontend.check_types,
                                  script_action=scripts_test_runner.check_types)


# -------------------------------------
# Dependency management commands
# -------------------------------------
Dependency = str  # type alias


def catchup(*, target: Target = 'all') -> None:
    """
    Check if any dependencies added from others remotely, and then install them if so.
    """
    execute_on_target_environment(target,
                                  all_action=lambda: (
                                      backend.catchup(),
                                      frontend.catchup()),
                                  backend_action=backend.catchup,
                                  frontend_action=frontend.catchup)


def list_outdated(*, target: Target = 'all') -> None:
    """
    List packages that should be updated.
    """
    execute_on_target_environment(target,
                                  all_action=lambda: (
                                      backend.list_outdated(),
                                      frontend.list_outdated()),
                                  backend_action=backend.list_outdated,
                                  frontend_action=frontend.list_outdated)


def dependency_tree(*, target: Target = 'all') -> None:
    """
    Visualize which dependencies depend upon each other.
    """
    execute_on_target_environment(target,
                                  all_action=lambda: (
                                      backend.dependency_tree()),
                                  backend_action=backend.dependency_tree)


def add(*, target: Target, dependencies: List[Dependency]) -> None:
    """
    Add one or more packages.
    """
    execute_on_target_environment(target,
                                  backend_action=backend.add,
                                  frontend_action=frontend.add,
                                  dependencies=dependencies)


def upgrade(*, target: Target, dependencies: List[Dependency]) -> None:
    """
    Upgrade one or more out-of-date packages.
    """
    execute_on_target_environment(target,
                                  backend_action=backend.upgrade,
                                  frontend_action=frontend.upgrade,
                                  dependencies=dependencies)


def remove(*, target: Target, dependencies: List[Dependency]) -> None:
    """
    Remove one or more packages.
    """
    execute_on_target_environment(target,
                                  backend_action=backend.remove,
                                  frontend_action=frontend.remove,
                                  dependencies=dependencies)


# -------------------------------------
# Deploy commands
# -------------------------------------

def deploy_to_heroku(target: Target = 'all') -> None:
    """
    Push changes to GitHub and Heroku.
    """
    execute_on_target_environment(target,
                                  all_action=deploy.main)


# -------------------------------------
# Command line options
# -------------------------------------
command_map = {'run': run,
               'stop': stop,
               'install': install,
               'test': test,
               'types': check_types,
               'catchup': catchup,
               'outdated': list_outdated,
               'deptree': dependency_tree,
               'add': add,
               'upgrade': upgrade,
               'remove': remove,
               'deploy': deploy_to_heroku
               }

# -------------------------------------
# Run script
# -------------------------------------

if __name__ == '__main__':
    main()

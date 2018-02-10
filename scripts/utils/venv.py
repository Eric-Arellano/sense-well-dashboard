"""
Utilities to interface with Python's venv (virtual environment).
"""
from typing import Any, Callable, List

from scripts.utils import files, prereq_checker, sys_calls


# -----------------------------------------------------------------
# Check prereqs installed
# -----------------------------------------------------------------

def check_prereqs_installed() -> None:
    """
    Confirm all required software installed.
    """
    prereq_checker.check_is_installed(['python3'], windows_support=False)
    prereq_checker.check_is_installed(['python'], posix_support=False)
    sys_calls.check_prereqs_installed()
    files.check_prereqs_installed()


# -----------------------------------------------------------------
# Commands
# -----------------------------------------------------------------

def activate() -> None:
    """
    Source the venv so that its packages may be used.
    """
    path = 'backend/Scripts/' if sys_calls.is_windows_environment() else 'backend/bin'
    files.source(file='activate', path=path)


def is_created() -> bool:
    """
    Boolean check if venv folder already exists.
    """
    return operate_on_all_venv_files(files.do_exist)


def operate_on_all_venv_files(func: Callable[[List[str]], Any]) -> Any:
    """
    Performs passed function on every venv file.
    """
    paths = ['pyvenv.cfg', 'pip-selfcheck.json']
    paths += ['Scripts', 'Include', 'Lib', 'lib64'] if sys_calls.is_windows_environment() else ['bin/', 'include/',
                                                                                                'lib/']
    paths = list(map(lambda x: 'backend/' + x, paths))
    return func(paths)


def create() -> None:
    """
    Create new venv in backend folder if not already done.
    """
    if is_created():
        print('venv already created.')
    sys_calls.run_python(['-m', 'venv', 'backend/'])


def remove() -> None:
    """
    Deletes the virtual environment.
    """
    operate_on_all_venv_files(files.remove)

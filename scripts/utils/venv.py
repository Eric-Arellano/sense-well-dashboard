"""
Utilities to interface with Python's venv (virtual environment).
"""

from scripts.utils import prereq_checker, sys_calls


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


# -----------------------------------------------------------------
# Commands
# -----------------------------------------------------------------

def activate() -> None:
    """
    Source the venv so that its packages may be used.
    """
    if sys_calls.is_windows_environment():
        path = 'backend/Scripts/'
    else:
        path = 'backend/bin'
    sys_calls.source_file(file='activate', path=path)


def is_created() -> bool:
    """
    Boolean check if venv folder already exists.
    """
    raise NotImplementedError


def create() -> None:
    """
    Create new venv in backend folder if not already done.
    """
    command = ['-m', 'venv', 'backend/']
    if sys_calls.is_windows_environment():
        sys_calls.run(['python'] + command)
    else:
        sys_calls.run(['python3'] + command)

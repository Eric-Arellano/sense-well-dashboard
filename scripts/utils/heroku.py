"""
Utilities to interface with Heroku.
"""

from scripts.utils import prereq_checker, sys_calls


# -----------------------------------------------------------------
# Check prereqs installed
# -----------------------------------------------------------------

def check_prereqs_installed() -> None:
    """
    Confirm all required software installed.
    """
    prereq_checker.check_is_installed(['heroku'])
    sys_calls.check_prereqs_installed()


# -----------------------------------------------------------------
# Check status
# -----------------------------------------------------------------

def is_logged_in() -> bool:
    """
    Returns true if logged in through CLI to Heroku.
    """
    auth = sys_calls.get_stdout(['heroku', 'auth:whoami'])
    return 'not logged in' not in auth

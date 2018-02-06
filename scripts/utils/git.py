"""
Utilities to interface with Git.
"""

from textwrap import dedent
from typing import List

from scripts.utils import prereq_checker, sys_calls

Branch = str
Remote = str
RemoteURL = str


# -----------------------------------------------------------------
# Check prereqs installed
# -----------------------------------------------------------------

def check_prereqs_installed() -> None:
    """
    Confirm all required software installed.
    """
    prereq_checker.check_is_installed(['git'])
    sys_calls.check_prereqs_installed()


# -----------------------------------------------------------------
# Check status
# -----------------------------------------------------------------

def is_on_branch(target_branch: Branch) -> bool:
    """
    Returns true if current branch is same as target branch.
    """
    current_branch = sys_calls.get_stdout(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
    return current_branch == target_branch


def is_remote_added(remote: Remote) -> bool:
    """
    Returns true if remote is linked to on local machine.
    """
    remotes = sys_calls.get_stdout(['git', 'remote'])
    return remote in remotes


def is_clean_local() -> bool:
    """
    Returns True if there are no differences on local that need to be committed.
    """
    response = sys_calls.run(['git', 'diff-index', '--quiet', 'HEAD', '--'])
    return response.returncode == 0


# -----------------------------------------------------------------
# Git commands
# -----------------------------------------------------------------

def fast_forward_remote(remote: Remote, branch: Branch) -> None:
    """
    Checks given remote for any changes and attempts to fast-forward.
    """
    sys_calls.run(['git', 'fetch', remote, branch])
    sys_calls.run(['git', 'merge', '--ff-only'], check=True)


def checkout(branch: Branch) -> None:
    """
    Simple checkout to given branch.
    """
    sys_calls.run(['git', 'checkout', branch])


def add(files: List[str]) -> None:
    """
    Add given files / glob.
    """
    sys_calls.run(['git', 'add'] + files)


def commit(message: str) -> None:
    """
    Commit with message.
    """
    sys_calls.run(['git', 'commit', '-m', message])


def push(remote: Remote, remote_branch: Branch) -> None:
    """
    Push to given remote.
    """
    sys_calls.run(['git', 'push', remote, remote_branch])


def add_remote(remote: Remote, url: RemoteURL) -> None:
    """
    Add given remote to local git.
    """
    sys_calls.run(['git', 'remote', 'add', remote, url])


# -----------------------------------------------------------------
# Commit reminder
# -----------------------------------------------------------------

def remind_to_commit(file_names: str) -> None:
    """
    Prints reminder to commit to Git the specified files.
    """
    reminder = _generate_commit_reminder(file_names)
    print(reminder)


def _generate_commit_reminder(file_names: str) -> str:
    return dedent(f'''
    -----------------------------------------------------------------

    Remember to commit and push your changes to {file_names}.
    ''')

#!/usr/bin/env python3.6

"""
Utility to deploy app to GitHub and Heroku.
"""
import os
import sys

# path hack, https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from scripts.utils import heroku, git


def main() -> None:
    check_prereqs_installed()
    check_remote_added()
    check_logged_in()
    resolve_git_issues()
    deploy()


def check_prereqs_installed() -> None:
    """
    Confirms all required software installed.
    """
    heroku.check_prereqs_installed()
    git.check_prereqs_installed()


def check_remote_added() -> None:
    """
    Add Heroku remote if not already exists.
    """
    if not git.is_remote_added('heroku'):
        git.add_remote('heroku', 'https://git.heroku.com/ngsc-service-hours.git')


def check_logged_in() -> None:
    """
    Exit script if not logged in to Heroku CLI.
    """
    if not heroku.is_logged_in():
        raise SystemExit('You must first login to Heroku using `heroku login`. '
                         'Ask Eric (ecarell1@asu.edu) for his Heroku credentials.')


def resolve_git_issues() -> None:
    """
    Confirm on master branch, branch is clean, and check for changes from remote.
    """
    if not git.is_on_branch('master'):
        git.checkout('master')
    if not git.is_clean_local():
        raise SystemExit('Make sure the branch is clean before running this script.')
    git.fast_forward('origin', 'master')
    git.fast_forward('heroku', 'master')


def deploy() -> None:
    """
    Push to GitHub origin master and Heroku origin master.
    """
    git.push('origin', 'master')
    git.push('heroku', 'master')


if __name__ == '__main__':
    main()

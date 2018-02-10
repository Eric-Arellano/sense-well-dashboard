"""
Utilities to interface with the outside world.
"""

import os
import subprocess
from pathlib import Path
from typing import List

from scripts.utils import sys_calls


# -----------------------------------------------------------------
# Check prereqs installed
# -----------------------------------------------------------------

def check_prereqs_installed() -> None:
    """
    Confirm all required software installed.
    """
    sys_calls.check_prereqs_installed()


# -----------------------------------------------------------------
# Commands
# -----------------------------------------------------------------
File = str


def do_exist(files: List[File]) -> bool:
    """
    Boolean check if all files specified exist.
    """
    return all(Path(file).exists()
               for file in files)


def remove(files: List[File]) -> None:
    """
    Removes all specified files recursively.
    """
    sys_calls.run(['rm', '-rf'] + files)


def source(*, file: File, path: str) -> None:
    """
    Mirrors the source command by adding values to local environment.

    See https://stackoverflow.com/questions/3503719/emulating-bash-source-in-python
    """
    if sys_calls.is_windows_environment():
        command = ['cmd', '/C', f'{file} && set']
    else:
        command = ['bash', '-c', f'source {file} && env']
    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE,
                               cwd=path)
    for line in process.stdout:
        (key, _, value) = line.decode("utf-8").strip().partition("=")
        os.environ[key] = value
    process.communicate()

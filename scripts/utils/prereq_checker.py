"""
Utilities to check that necessary programs are installed on the system and on its PATH.
"""

import shutil
from typing import List

from scripts.utils import sys_calls

ProgramName = str


def find_not_installed(programs: List[ProgramName]) -> List[ProgramName]:
    """
    Returns list of programs not installed, or empty list.
    """
    return [program for program in programs
            if not is_program_installed(program)]


def is_program_installed(program: ProgramName) -> bool:
    """
    Boolean check if program is installed or not.
    """
    return shutil.which(program) is not None


def check_is_installed(programs: List[ProgramName], *,
                       windows_support=True,
                       posix_support=True) -> None:
    """
    Raise exception if any of the given programs not installed.

    Can conditionally only check Windows or Posix systems.
    """
    not_installed_programs: List[ProgramName] = []
    if windows_support and posix_support:
        not_installed_programs = find_not_installed(programs)
    elif windows_support and sys_calls.is_windows_environment():
        not_installed_programs = find_not_installed(programs)
    elif posix_support and not sys_calls.is_windows_environment():
        not_installed_programs = find_not_installed(programs)
    if not_installed_programs:
        program_list = ' and '.join(not_installed_programs)
        raise SystemExit(f'{program_list} not installed')

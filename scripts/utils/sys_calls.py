"""
Utilities to interface with the outside world.
"""

import os
import subprocess
from typing import Dict, List, Tuple, Union


# -----------------------------------------------------------------
# Check prereqs installed
# -----------------------------------------------------------------

def check_prereqs_installed() -> None:
    """
    Confirm all required software installed.
    """
    pass  # nothing required


# -----------------------------------------------------------------
# Determine environment
# -----------------------------------------------------------------

def is_windows_environment() -> bool:
    """
    Return True if on Windows, else on Posix.
    """
    return os.name == 'nt'


def determine_python_executable() -> str:
    """
    Get name of python executable depending on system.
    """
    if is_windows_environment():
        return 'python'
    else:
        return 'python3'


Command = Union[List[str], str]


def _modify_for_windows(command: List[str], kwargs: Dict) -> Tuple[Command, Dict]:
    """
    Allows running the command on Windows, if Windows is detected.
    """
    if is_windows_environment():
        windows_command = ' '.join(command)
        windows_kwargs = dict(kwargs, shell=True)
        return windows_command, windows_kwargs
    return command, kwargs


# -----------------------------------------------------------------
# Run commands
# -----------------------------------------------------------------

def run(command: List[str], **kwargs) -> subprocess.CompletedProcess:
    """
    Calls subprocess.run() and allows seamless support of both Windows and Unix.
    """
    new_command, new_kwargs = _modify_for_windows(command, kwargs)
    return subprocess.run(new_command,
                          **new_kwargs)


def run_detached(command: List[str], **kwargs) -> None:
    """
    Calls non-blocking subprocess.Popen() and ignores all input and output.
    """
    new_command, new_kwargs = _modify_for_windows(command, kwargs)
    subprocess.Popen(new_command,
                     stdout=subprocess.DEVNULL,
                     stderr=subprocess.DEVNULL,
                     **new_kwargs)


def run_as_shell(command: str, **kwargs) -> subprocess.CompletedProcess:
    """
    Calls subprocess.run() with shell=True.
    """
    return subprocess.run(command,
                          shell=True,
                          **kwargs)


def run_python(command: List[str], **kwargs) -> subprocess.CompletedProcess:
    """
    Run the command using Python executable.
    """
    python = determine_python_executable()
    new_command, new_kwargs = _modify_for_windows([python] + command, kwargs)
    return subprocess.run(new_command,
                          **new_kwargs)


# -----------------------------------------------------------------
# Get StdOut of process
# -----------------------------------------------------------------

def get_stdout(command: List[str], **kwargs) -> str:
    """
    Performs the given command and returns the stdout as a string.
    """
    new_command, new_kwargs = _modify_for_windows(command, kwargs)
    return subprocess.run(new_command,
                          stdout=subprocess.PIPE,
                          encoding='utf-8',
                          **new_kwargs).stdout.strip()


def get_stdout_as_shell(command: str, **kwargs) -> str:
    """
    Performs the given command using Shell and returns the stdout as a string.
    """
    return subprocess.run(command,
                          shell=True,
                          stdout=subprocess.PIPE,
                          encoding='utf-8',
                          **kwargs).stdout.strip()

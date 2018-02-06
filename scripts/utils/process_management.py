"""
Utilities to interface with processes and ports.
"""

from scripts.utils import prereq_checker, sys_calls

Port = str
PID = str


# -----------------------------------------------------------------
# Check prereqs installed
# -----------------------------------------------------------------

def check_prereqs_installed() -> None:
    """
    Confirm all required software installed.
    """
    prereq_checker.check_is_installed(['grep', 'awk'])
    prereq_checker.check_is_installed(['lsof', 'kill'], windows_support=False)
    prereq_checker.check_is_installed(['netstat', 'taskkill', 'findstr'], posix_support=False)
    sys_calls.check_prereqs_installed()


# -----------------------------------------------------------------
# Networking
# -----------------------------------------------------------------

def find_pid_on_port(port: Port) -> PID:
    """
    Finds and returns PID of process listening on specified port.
    """
    # determine environment
    if sys_calls.is_windows_environment():
        command = f"netstat -aon | findstr :{port} | awk '{{ print $5 }}'"
    else:
        command = f"lsof -n -i4TCP:{port} | grep LISTEN | awk '{{ print $2 }}'"
    # find PID
    pid = sys_calls.get_stdout_as_shell(command)
    if not pid:
        raise SystemExit(f'No process found running on port {port}.')
    return PID(pid)


# -----------------------------------------------------------------
# Manage processes
# -----------------------------------------------------------------

def kill_process(pid: PID) -> None:
    """
    Kills the specified PID.
    """
    if sys_calls.is_windows_environment():
        command = ['taskkill', '/F', '/PID']
    else:
        command = ['kill']
    sys_calls.run(command + [pid])

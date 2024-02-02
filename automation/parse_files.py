import os
import re
from rich.console import Console
from create_folder import create_folder
from sort_files import sort_documents

console = Console()

def parse_log_file(username):
    """
    Parses log files for a given user, separating errors and warnings into distinct files.

    Parameters:
        username (str): The username of the user whose log files need to be parsed.
    """
    user_folder = os.path.join("assets", "user-docs", username)

    if not os.path.exists(user_folder):
        console.print(f"[bold yellow]User '{username}' does not exist.[/bold yellow]")
        return

    logs_folder = os.path.join(user_folder, "logs")
    if not os.path.exists(logs_folder):
        sort_documents(username)
    errors_path = os.path.join(logs_folder, "errors.log")
    warnings_path = os.path.join(logs_folder, "warnings.log")

    for log_file in os.listdir(logs_folder):
        log_file_path = os.path.join(logs_folder, log_file)

        with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as logs, open(errors_path, 'a', encoding='utf-8') as errors_log, open(warnings_path, 'a', encoding='utf-8') as warnings_log:
            for line in logs:
                if is_error(line):
                    errors_log.write(line)
                elif is_warning(line):
                    warnings_log.write(line)

    console.print("[bold green]Log file parsed successfully. Errors and warnings logged in separate files.[/bold green]")

def is_error(line):
    """
    Checks if a log line indicates an error.

    Parameters:
        line (str): The log line to be checked.

    Returns:
        bool: True if the line indicates an error, False otherwise.
    """
    return "ERROR" in line.upper()

def is_warning(line):
    """
    Checks if a log line indicates a warning.

    Parameters:
        line (str): The log line to be checked.

    Returns:
        bool: True if the line indicates a warning, False otherwise.
    """
    return "WARNING" in line.upper()
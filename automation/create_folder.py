import os
import re
from rich.console import Console

console = Console()

def create_folder(folder_name):
    """
    Create a new folder with the given name.

    Parameters:
    - folder_name (str): The name of the folder to be created.

    Raises:
    - FileExistsError: If a folder with the same name already exists.
    - Exception: For other unexpected errors during folder creation.

    Returns:
    - None: The function does not return any value.

    Example:
    >>> create_folder("new_folder")
    [bold yellow]Folder 'new_folder' already exists.[/bold yellow]
    """
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        console.print(f"[bold yellow]Folder '{folder_name}' already exists.[/bold yellow]")
    except Exception as e:
        console.print(f"[bold red]Error creating folder '{folder_name}': {e}[/bold red]")
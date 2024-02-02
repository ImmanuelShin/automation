import os
from rich.console import Console

console = Console()

def count_file_types(username):
    """
    Counts the number of different file types and folders in the specified user's directory.

    Parameters:
        username (str): The username of the user.

    Returns:
        dict: A dictionary containing file types and corresponding counts, including folders.
              Example: {'.txt': 3, '.pdf': 1, 'folder': 2}
    """
    user_folder = os.path.join("assets", "user-docs", username)
    if not os.path.exists(user_folder):
        console.print(f"[bold yellow]User '{username}' does not exist.[/bold yellow]")
        return
    types_count = {}
    for item in os.listdir(user_folder):
        path = os.path.join(user_folder, item)
        if os.path.isfile(path):
            _, extension = os.path.splitext(item)
            extension = extension.lower()
            types_count[extension] = types_count.get(extension, 0) + 1
        elif os.path.isdir(path):
            types_count["folder"] = types_count.get("folder", 0) + 1

    return types_count
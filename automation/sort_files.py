import os
import shutil
from rich.console import Console
from create_folder import create_folder

console = Console()

def sort_documents(username):
    """
    Sorts documents for a given user by moving them into folders based on file types.

    Parameters:
        username (str): The username of the user whose documents need to be sorted.
    """
    user_folder = os.path.join("assets", "user-docs", username)

    if not os.path.exists(user_folder):
        console.print(f"[bold yellow]User '{username}' does not exist.[/bold yellow]")
        return

    if not os.path.exists(os.path.join(user_folder, "logs")):
        create_folder(os.path.join(user_folder, "logs"))

    if not os.path.exists(os.path.join(user_folder, "mail")):
        create_folder(os.path.join(user_folder, "mail"))
        
    for filename in os.listdir(user_folder):
        source_file = os.path.join(user_folder, filename)

        file_type = get_file_type(filename)

        if file_type in ["logs", "mail"]:
            destination = os.path.join(user_folder, file_type)

            destination_file = os.path.join(destination, filename)
            shutil.move(source_file, destination_file)

            console.print(f"[bold green]File '{filename}' moved to '{file_type}' folder successfully.[/bold green]")

def get_file_type(file):
    """
    Determines the file type based on the given file name.

    Parameters:
        file (str): The name of the file.

    Returns:
        str: The file type ('logs', 'mail', or 'other').
    """
    name, extension = os.path.splitext(file)
    extension = extension.lower()

    if name.endswith(".log"):
        return "logs"
    elif extension == ".mail":
        return "mail"
    else:
        return "other"
    
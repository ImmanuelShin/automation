import os
import shutil
from rich.console import Console
from create_folder import create_folder

console = Console()

def handle_deleted_user(username):
    """
    Handles the deletion of a user by moving their documents to a temporary folder and deleting their user folder.

    Parameters:
        username (str): The username of the user to be handled.
    """
    user_folder = os.path.join("assets", "user-docs", username)
    temp_folder = os.path.join("assets", "user-docs", "temporary",f"{username}_documents")

    console.print(f"[bold cyan]Handling deleted user '{username}'...[/bold cyan]")

    if not os.path.exists(user_folder):
        console.print(f"[bold yellow]User '{username}' does not exist.[/bold yellow]")
        return
    try:
        if not os.path.exists(os.path.join("assets", "user-docs", "temporary")):
            create_folder(os.path.join("assets", "user-docs", "temporary"))

        create_folder(temp_folder)

        move_documents(user_folder, temp_folder)

        shutil.rmtree(user_folder)

        console.print(f"[bold green]User '{username}' handled successfully. Documents moved to the temporary folder.[/bold green]")
    except Exception as e:
        console.print(f"[bold red]Error handling user '{username}': {e}[/bold red]")

def move_documents(source, destination):
    """
    Moves all items from the source folder to the destination folder.

    Parameters:
        source (str): The path to the source folder.
        destination (str): The path to the destination folder.
    """
    for item in os.listdir(source):
        source_item = os.path.join(source, item)
        destination_item = os.path.join(destination, item)
        shutil.move(source_item, destination_item)

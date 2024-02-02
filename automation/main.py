import os
from rich.console import Console
from rich.prompt import Prompt
from create_folder import create_folder
from handle_redacted import handle_deleted_user
from parse_files import parse_log_file
from sort_files import sort_documents
from count_files import count_file_types

console = Console()

def menu():
    """
    Display the main menu options.

    This function prints the available options in the console for the user to choose from.

    Returns:
        None
    """
    console.print("[bold cyan]Menu:[/bold cyan]")
    console.print("1. Create Folder")
    console.print("2. Handle Deleted User")
    console.print("3. Sort Documents")
    console.print("4. Parse Log Files")
    console.print("5. Count Specific File Types in a Directory")
    console.print("6. Exit")
    
if __name__ == "__main__":
    """
    Main execution loop for the automation script.

    This script provides a menu-driven interface for various file and folder manipulation tasks.

    Returns:
        None
    """
    while True:
        menu()
        choice = Prompt.ask("Choose a task (1-6):", choices=["1", "2", "3", "4", "5", "6"])

        if choice == "1":
            folder_name = Prompt.ask("Enter folder name:")
            create_folder(folder_name)

        elif choice == "2":
            deleted_user = Prompt.ask("Enter the username of the deleted user:")
            handle_deleted_user(deleted_user)

        elif choice == "3":
            user = Prompt.ask("Enter the username of the user:")
            sort_documents(user)

        elif choice == "4":
            user = Prompt.ask("Enter the username of the user:")
            parse_log_file(user)

        elif choice == "5":
            user = Prompt.ask("Enter the username of the user")
            file_types_count = count_file_types(user)
            console.print("[bold cyan]File Types Count in the user's directory:[/bold cyan]")
            for extension, count in file_types_count.items():
                console.print(f"{extension}: {count}")

        elif choice == "6":
            break

        else:
            console.print("[bold red]Invalid choice. Please choose a number between 1 and 6.[/bold red]")
import datetime
import tkinter as tk
from pathlib import Path
from tkinter import filedialog


def get_creation_date(file_path):
    # Get the file creation time in seconds since the epoch
    creation_time = file_path.stat().st_ctime
    # Convert the creation time to a human-readable format
    creation_date = datetime.datetime.fromtimestamp(creation_time)
    return creation_date


def rename_file(file_path, new_name):
    try:
        file_path.rename(file_path.parent / new_name)
        print(f"Renamed '{file_path.name}' to '{new_name}'")
        return True
    except Exception as e:
        print(f"Error renaming '{file_path.name}': {e}")
        return False


def prompt_rename(file_path):
    original_name = file_path.name
    original_extension = file_path.suffix.lower()
    creation_date = get_creation_date(file_path)
    new_name = (
        f"Screenshot_{creation_date.strftime('%Y-%m-%d_%H-%M-%S')}" + original_extension
    )

    user_input = (
        input(
            f"File '{original_name}' will be renamed to '{new_name}'"
            "\nDo you want to proceed? (Y/n): "
        )
        or "y"
    )

    if user_input.lower() == "y":
        return rename_file(file_path, new_name)
    else:
        print(f"Skipped renaming '{original_name}'")
        return False


def print_creation_dates(directory_path):
    # Ensure the provided path is a directory
    directory_path = Path(directory_path)
    if not directory_path.is_dir():
        print(f"Error: {directory_path} is not a valid directory.")
        return

    # Iterate through all files in the directory
    for file_path in directory_path.iterdir():
        # Check if the path is a file
        if file_path.is_file():
            prompt_rename(file_path)


def select_directory():
    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Ask the user to select a directory
    return filedialog.askdirectory(title="Select Directory")


def main():
    # Replace 'your_directory_path' with the path of the directory you want to analyze
    directory_path = select_directory()
    if directory_path:
        print_creation_dates(directory_path)
    else:
        print("No directory selected.")


if __name__ == "__main__":
    main()

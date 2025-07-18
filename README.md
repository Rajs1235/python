# python
# README Content for Projects

---

## Project 1: Automated File Organizer (Python)

# Automated File Organizer

A simple yet powerful Python script to automatically organize files in a directory based on their file extensions. This tool helps keep your folders tidy by moving files into designated subdirectories according to their type (e.g., images, documents, videos).

## How It Works

The script scans a specified directory and identifies the extension of each file. It then creates folders for common file categories (if they don't already exist) and moves the files into the appropriate folder.

For example:
- `.jpg`, `.png`, `.gif` files are moved to an `Images` folder.
- `.pdf`, `.docx`, `.txt` files are moved to a `Documents` folder.
- `.mp4`, `.mov`, `.avi` files are moved to a `Videos` folder.
- And so on for other common file types.

## Features

- **Automatic Sorting**: Sorts files into folders like `Images`, `Documents`, `Videos`, `Audio`, `Archives`, and `Others`.
- **Easy to Use**: Simply run the script and provide the path to the directory you want to organize.
- **Customizable**: Easily extend the script to handle new file extensions and categories.
- **Safe**: The script moves files, it does not delete them.

## Technologies Used

- **Python 3**
- **os module**: For interacting with the operating system, like accessing file paths.
- **shutil module**: For performing high-level file operations, like moving files.

## Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Rajs1236/File-Organizer.git
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd File-Organizer
    ```

3.  **Run the script:**
    Execute the script from your terminal and pass the path to the folder you want to clean up.

    ```bash
    python main.py "/path/to/your/folder"
    ```
    Replace `"/path/to/your/folder"` with the actual path of the directory you want to organize (e.g., `"/Users/YourUser/Downloads"`).

## Example

**Before:**


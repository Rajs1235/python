import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from tabulate import tabulate

def organize_files(target_folder):
    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Music': ['.mp3', '.wav', '.aac'],
        'Archives': ['.zip', '.tar', '.gz', '.rar'],
        'Executables': ['.exe', '.msi'],
        'Others': []
    }

    moved_files_count = {category: 0 for category in categories}
    moved_files_info = []

    for filename in os.listdir(target_folder):
        file_path = os.path.join(target_folder, filename)
        
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            moved = False
            
            for category, extensions in categories.items():
                if file_extension in extensions:
                    category_folder = os.path.join(target_folder, category)
                    os.makedirs(category_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_folder, filename))
                    moved_files_count[category] += 1
                    moved_files_info.append([filename, file_extension, category])
                    moved = True
                    break
            
            if not moved:
                others_folder = os.path.join(target_folder, 'Others')
                os.makedirs(others_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(others_folder, filename))
                moved_files_count['Others'] += 1
                moved_files_info.append([filename, file_extension, 'Others'])

    return moved_files_info, moved_files_count

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        moved_files_info, moved_files_count = organize_files(folder_path)
        display_results(moved_files_info, moved_files_count)

def display_results(moved_files_info, moved_files_count):
    result_window = tk.Toplevel(root)
    result_window.title("Organizing Results")

    # Display the table of moved files
    headers = ["File Name", "Format", "Category"]
    table = tabulate(moved_files_info, headers=headers, tablefmt="grid")
    
    result_text = tk.Text(result_window, wrap='word')
    result_text.insert(tk.END, "✅ Organizing complete!\n\n")
    result_text.insert(tk.END, table + "\n\n--- Summary ---\n")
    
    for category, count in moved_files_count.items():
        result_text.insert(tk.END, f"Moved {count} {category.lower()} file(s).\n")
    
    result_text.pack(expand=True, fill='both')
    result_text.config(state=tk.DISABLED)

# Create the main application window
root = tk.Tk()
root.title("Automated File Organizer")
root.geometry("300x150")

# Create a button to select the folder
select_button = tk.Button(root, text="Select Folder to Organize", command=select_folder)
select_button.pack(expand=True)

# Start the GUI event loop
root.mainloop()

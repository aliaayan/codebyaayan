import os
import shutil

# An automated file organizer script.
# This script scans a target folder and sorts all files into subfolders based on their extensions.

def organize_folder(folder_path):
    # Dictionary mapping folder categories to their file extensions
    extensions_map = {
        "Images": ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
        "Documents": ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
        "Videos": ['.mp4', '.avi', '.mkv', '.mov'],
        "Audio": ['.mp3', '.wav', '.aac'],
        "Archives": ['.zip', '.rar', '.tar', '.gz'],
        "Executables": ['.exe', '.msi', '.apk'],
        "Code": ['.py', '.html', '.css', '.js', '.cpp', '.json']
    }

    # Check if the folder path exists
    if not os.path.exists(folder_path):
        print(f"Error: The folder path '{folder_path}' does not exist.")
        return

    print(f"Organizing files in: {folder_path}...\n")

    # Loop through every item in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories, only process the files
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            moved = False

            # Check which category the file belongs to
            for category, extensions in extensions_map.items():
                if file_extension in extensions:
                    # Create the category folder if it doesn't exist yet
                    category_path = os.path.join(folder_path, category)
                    if not os.path.exists(category_path):
                        os.makedirs(category_path)

                    # Move the file into the new folder
                    shutil.move(file_path, os.path.join(category_path, filename))
                    print(f"Moved: {filename} -> {category}/")
                    moved = True
                    break
            
            # If the file type doesn't match our list, put it in an 'Others' folder
            if not moved and file_extension != '':
                others_path = os.path.join(folder_path, "Others")
                if not os.path.exists(others_path):
                    os.makedirs(others_path)
                shutil.move(file_path, os.path.join(others_path, filename))
                print(f"Moved: {filename} -> Others/")

    print("\nOrganization complete! Your folder is now perfectly clean.")

if __name__ == "__main__":
    print("Welcome to the Python Desktop File Organizer!")
    target = input("Enter the full path of the folder you want to clean up: ")
    organize_folder(target)

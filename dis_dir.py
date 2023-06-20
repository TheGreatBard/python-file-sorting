import os
import shutil
import ask_for_path

def move_files(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            destination_path = os.path.join(directory, filename)
            base_name, extension = os.path.splitext(filename)
            counter = 1

            # Find a new file name if the file already exists in the destination directory
            while os.path.exists(destination_path):
                new_filename = f"{base_name}_{counter}{extension}"
                destination_path = os.path.join(directory, new_filename)
                counter += 1

            shutil.move(file_path, destination_path)

def remove_empty_dirs(directory):
    removed_dirs = []
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            try:
                os.rmdir(dir_path)  # Remove empty directories
                removed_dirs.append(dir_path)
            except OSError:
                pass  # Directory is not empty, so skip

    return removed_dirs

def print_dir():
    print("Files have been moved successfully.")

    if removed_directories:
        print("The following directories have been removed:")
        for directory in removed_directories:
            print(directory)
    else:
        print("No empty directories found.")

path = ask_for_path.ask()
move_files(path)
removed_directories = remove_empty_dirs(path)
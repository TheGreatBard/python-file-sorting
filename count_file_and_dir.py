import os


def count_files_and_directories(path):
    # Initialize counters
    total_files = 0
    total_dirs = 0

    # Iterate over items in the directory
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            # If the item is a directory, increment the directory counter and recursively count its files and directories
            total_dirs += 1
            subfiles, subdirs = count_files_and_directories(item_path)
            total_files += subfiles
            total_dirs += subdirs
            print(f"Directory: {item} | Files: {subfiles} | Directories: {subdirs}")
        elif os.path.isfile(item_path):
            # If the item is a file, increment the file counter
            total_files += 1

    return total_files, total_dirs

def print_count(path):
    # Call the function to count files and directories
    file_count, dir_count = count_files_and_directories(path)

    # Print the total number of files and directories
    print("Total files:", file_count)
    print("Total directories:", dir_count)

# Ask for path
path = input("Enter Path: ")  # Ask user for path
print_count(path)

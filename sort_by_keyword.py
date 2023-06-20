import os
import shutil
import ask_for_path

def move_files_with_keyword(path, keyword):
    for root, dirs, files in os.walk(path):
        for filename in files:
            if keyword in filename:
                source_path = os.path.join(root, filename)
                target_dir = os.path.join(path, keyword)
                os.makedirs(target_dir, exist_ok=True)
                
                base_name, ext = os.path.splitext(filename)
                target_file = os.path.join(target_dir, filename)
                
                suffix = 1
                while os.path.exists(target_file):
                    new_name = f"{base_name}_{suffix}{ext}"
                    target_file = os.path.join(target_dir, new_name)
                    suffix += 1
                
                shutil.move(source_path, target_file)
                print(f"Moved: {filename} -> {target_file}")

def key():
    path = ask_for_path.ask()
    keyword = input("Enter the keyword: ")
    
    move_files_with_keyword(path, keyword)


key()

if __name__ == "__main__":
    key()

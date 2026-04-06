# path to making a file organiser
"""
listing files present in a directory
extracting the extensions based on "."
then accordingly making folder based on extensions
moving the files into the designated folders based on those extensions
"""
import os
import shutil

def create_folder(filepath, ext):
    folder_path = os.path.join(filepath, ext)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)



usr_input = input("File Directory to Sort : ").strip()
file_path = os.path.expanduser(usr_input)

if os.path.exists(file_path):
    skipped = 0
    print(file_path)
    content = os.listdir(file_path)
    for file in content:
        if file.startswith("."):
            skipped = skipped + 1
            continue
        
        full_path = os.path.join(file_path, file)
        if not os.path.isfile(full_path):
            continue

        if "." in file:
            name, ext = file.rsplit(".", 1)
            ext = ext.lower()
        else:
            ext = "no_extensions"

        print(f"{file} --> {ext}")
        create_folder(filepath=file_path, ext=ext)

        destination = os.path.join(file_path, ext, file)
        if os.path.exists(destination):
            print(f"[!] Skipping, {file} already exists !!")
            continue

        shutil.move(full_path, destination)        
else:
    print("[!] file path doesnt exist")
    exit(-1)

print(f"Hidden files : {skipped}")
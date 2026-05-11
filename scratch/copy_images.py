import os
import shutil

src_base = r'C:\Users\jacob\Downloads\PROYECTO-20260507T093210Z-3-001\PROYECTO'
dest_base = r'f:\conrutas\AppBeluso\public\assets\pois'

for folder in os.listdir(src_base):
    src_folder_path = os.path.join(src_base, folder)
    if os.path.isdir(src_folder_path):
        dest_folder_path = os.path.join(dest_base, folder)
        if not os.path.exists(dest_folder_path):
            os.makedirs(dest_folder_path)
            print(f"Created directory: {dest_folder_path}")
        
        for file in os.listdir(src_folder_path):
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                src_file_path = os.path.join(src_folder_path, file)
                dest_file_path = os.path.join(dest_folder_path, file)
                shutil.copy2(src_file_path, dest_file_path)
                print(f"Copied {file} to {folder}")

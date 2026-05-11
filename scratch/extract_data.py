import os
import json

base_path = r'C:\Users\jacob\Downloads\PROYECTO-20260507T093210Z-3-001\PROYECTO'
data = {}

for folder in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder)
    if os.path.isdir(folder_path):
        txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
        images = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        
        description = ""
        if txt_files:
            try:
                with open(os.path.join(folder_path, txt_files[0]), 'r', encoding='utf-8') as f:
                    description = f.read()
            except UnicodeDecodeError:
                try:
                    with open(os.path.join(folder_path, txt_files[0]), 'r', encoding='latin-1') as f:
                        description = f.read()
                except:
                    description = "Error reading description"
        
        data[folder] = {
            "description": description.strip(),
            "images": sorted(images)
        }

print(json.dumps(data, indent=2))

import os
import shutil

path = r'C:\\Users\\RS-2100\\Desktop\\Portfolio\\Python\\Files Tests\\example_folder2\\'
folder_names = ['CSV Files', 'Text Files', 'Image Files']

# Criação das pastas caso não existam
for folder in folder_names:
    os.makedirs(os.path.join(path, folder), exist_ok=True)

# Organização dos arquivos nas respectivas pastas
file_names = os.listdir(path)

for file in file_names:
    if file.endswith(".csv"):
        shutil.move(os.path.join(path, file), os.path.join(path, "CSV Files", file))
    elif file.endswith(".png"):
        shutil.move(os.path.join(path, file), os.path.join(path, "Image Files", file))
    elif file.endswith(".txt"):
        shutil.move(os.path.join(path, file), os.path.join(path, "Text Files", file))

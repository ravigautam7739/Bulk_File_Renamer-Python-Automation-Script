import os

folder_path = "C:/Users/ravir/OneDrive/Desktop/Test"

files = os.listdir(folder_path)

for i, file in enumerate(files):
    old_path = os.path.join(folder_path, file)

    if os.path.isfile(old_path):
        ext = os.path.splitext(file)[1]
        new_name = f"project_{i+1}{ext}"
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)

print("Renaming completed")
import os
import shutil

source_folder = "source_images"
destination_folder = "moved_images"

os.makedirs(destination_folder, exist_ok=True)

jpg_files = []

for file in os.listdir(source_folder):
    if file.lower().endswith(".jpg"):
        jpg_files.append(file)

print("=" * 40)
print("SMART JPG FILE ORGANIZER")
print("=" * 40)

print(f"\nFound {len(jpg_files)} JPG files\n")

for file in jpg_files:
    source_path = os.path.join(source_folder, file)
    destination_path = os.path.join(destination_folder, file)

    shutil.move(source_path, destination_path)

    print(f"Moved: {file}")

print("\nSuccessfully moved all JPG files!")
print("Destination Folder:", destination_folder)

print("\n===== SUMMARY =====")
print(f"Total Files Moved: {len(jpg_files)}")
print("Status: Completed Successfully")
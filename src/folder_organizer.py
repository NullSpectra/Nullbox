import shutil,os
from pathlib import Path

EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".md"],
    "Executables": [".exe", ".msi"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
}

def organize():
    folder_path = input("Enter the folder path: ").strip()
    path = Path(folder_path)

    if not path.exists() or not path.is_dir():
        print(f"[!] Folder '{folder_path}' doesn't exist or is not a valid folder.")
        return

    for item in path.iterdir():
        if item.is_file():
            move_file(item, path)

def move_file(file_path: Path, base_path: Path):
    ext = file_path.suffix.lower()
    category = "Others"

    for cat, ext_list in EXTENSIONS.items():
        if ext in ext_list:
            category = cat
            break

    target_dir = base_path / category
    target_dir.mkdir(parents=True, exist_ok=True)

    target_path = target_dir / file_path.name
    shutil.move(str(file_path), str(target_path))
    print(f"[*] Moved {file_path.name} → {category}/")

if __name__ == "__main__":
    organize()

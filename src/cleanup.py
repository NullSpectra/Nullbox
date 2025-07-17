import os
import shutil
import platform
import sys

def clear_folder(path):
    if not os.path.exists(path):
        print(f"{path} does not exist")
        return

    try:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            try:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.unlink(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            except Exception as e:
                print(f"Failed to delete {item_path}. Reason: {e}")
        print(f"✅ {path} cleaned.\n")
    except Exception as e:
        print(f"Error accessing {path}. Reason: {e}")

def main():
    if platform.system() != 'Windows':
        print("❌ This script only works on Windows.")
        input("Press Enter to exit...")
        sys.exit(1)

    temp_paths = [
        os.getenv("TEMP"),
        os.getenv("TMP"),
        "C:\\Windows\\Temp",
        "C:\\Windows\\Prefetch"
    ]

    for path in temp_paths:
        if path:
            clear_folder(path)

    print("\n✅ System temporary files cleaned successfully.")
    input("Press Enter to finish...")

if __name__ == "__main__":
    main()

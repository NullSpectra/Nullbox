import sys
import os

print("Welcome to Nullbox!\n")

print("Scripts")
print("----------")
print("1. Basic AI\n2. Cleanup\n3. Folder Organizer\n4. IP Info\n5. Link Shortener\n6. Password Generator\n7. YouTube Downloader\n8. ZIP Bruteforce\n9. Exit")

choice = input("Enter the number of the script you want to run: ")

script_map = {
    "1": "src/basic_ai.py",
    "2": "src/cleanup.py",
    "3": "src/folder_organizer.py",
    "4": "src/ipinfo.py",
    "5": "src/link_shortener.py",
    "6": "src/passgen.py",
    "7": "src/yt_dw.py",
    "8": "src/zip_brute.py"
}

if choice == "9":
    print("Exiting...")
    sys.exit(0)
elif choice in script_map:
    script_path = script_map[choice]
    if os.path.exists(script_path):
        with open(script_path, "r") as f:
            exec(f.read())
    else:
        print(f"Script not found: {script_path}")
else:
    print("Invalid choice.")


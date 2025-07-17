import pyzipper
import os

def zip_brute(zip_path, wordlist_path):
    if not os.path.isfile(zip_path):
        print("[!] ZIP file not found.")
        return

    if not os.path.isfile(wordlist_path):
        print("[!] Wordlist file not found.")
        return

    try:
        with pyzipper.AESZipFile(zip_path) as zip_file, open(wordlist_path, "r", encoding="utf-8", errors="ignore") as wordlist:
            for line in wordlist:
                password = line.strip()
                try:
                    zip_file.extractall(pwd=bytes(password, "utf-8"))
                    print(f"\n[✓] Password found: {password}")
                    return
                except (RuntimeError, pyzipper.zipfile.BadZipFile, pyzipper.zipfile.LargeZipFile):
                    print(f"[X] Tried: {password}")
                except Exception as e:
                    print(f"[!] Unexpected error with password '{password}': {e}")
    except Exception as e:
        print(f"[!!] Failed to read ZIP or wordlist: {e}")
    else:
        print("\n[XX] Password not found in the wordlist.")

def pause():
    input("Press Enter to continue...")

if __name__ == "__main__":
    zip_path = input("Enter path to ZIP file: ").strip()
    wordlist_path = input("Enter path to wordlist: ").strip()
    zip_brute(zip_path, wordlist_path)
    pause()

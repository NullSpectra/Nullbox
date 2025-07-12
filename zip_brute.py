import pyzipper

def zip_brute(zip_path, wordlist_path):
    try:
        zip_file = pyzipper.AESZipFile(zip_path)
    except:
        print("Zip file not found")
        return

    with open(wordlist_path, "r", encoding="utf-8") as wordlist:
        for line in wordlist:
            password = line.strip()
            try:
                zip_file.extractall(pwd=bytes(password, "utf-8"))
                print(f"[✓] Password: {password}")
                return
            except:
                print(f"[X] Tried: {password}")

    print("[XX] Password wasn't found.")

if __name__ == "__main__":
    zip_path = input("ZIP dosyasının yolu: ")
    wordlist_path = input("Wordlist dosyasının yolu: ")
    zip_brute(zip_path, wordlist_path)

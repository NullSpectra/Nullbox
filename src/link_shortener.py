import requests

def short(url: str) -> str:
    api_url = "http://tinyurl.com/api-create.php"
    params = {"url": url}

    try:
        response = requests.get(api_url, params=params)  # GET olmalı
        response.raise_for_status()
        return response.text  # JSON değil, düz metin
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    long_url = input("Enter URL: ").strip()
    if not long_url.startswith(("http://", "https://")):
        long_url = "http://" + long_url
    short_url = short(long_url)
    print(f"Shortened URL: {short_url}")

import socket,requests

def get_local_ip():
    return socket.gethostbyname(socket.gethostname())

def get_public_ip():
    try:
        return requests.get('https://api.ipify.org').text
    except requests.RequestException:
        return "ERROR"

def pause():
    input("Press any key to continue...")

if __name__ == "__main__":
    print("Local IP:", get_local_ip())
    print("Public IP:", get_public_ip())
    pause()
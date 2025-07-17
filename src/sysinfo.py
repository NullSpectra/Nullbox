import platform,psutil,socket,uuid,os

def set_system_info():
    global info_os, info_cpu, info_arch, info_ram, info_storage
    info_os = f"{platform.system()} {platform.release()} {platform.version()}"
    info_cpu = f"{platform.processor()} {platform.architecture()[0]}"
    info_arch = f"{platform.architecture()[0]}"
    info_ram = f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB"
    info_storage = f"{psutil.disk_usage('/').total / (1024 ** 3):.2f} GB"

def get_system_info():
    print("System Information")
    print("-" * 20)
    print(f"OS: {info_os}")
    print(f"CPU: {info_cpu}")
    print(f"Architecture: {info_arch}")
    print(f"RAM: {info_ram}")
    print(f"Storage: {info_storage}")

if __name__ == "__main__":
    set_system_info()
    get_system_info()
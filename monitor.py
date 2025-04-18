import psutil
import time

def get_cpu_ram_usage():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    return cpu, ram




if __name__ == "__main__":
    while True:
        cpu, ram = get_cpu_ram_usage()
        print(f"CPU usage: {cpu}% | Ram Usage: {ram}%")
        time.sleep(1)



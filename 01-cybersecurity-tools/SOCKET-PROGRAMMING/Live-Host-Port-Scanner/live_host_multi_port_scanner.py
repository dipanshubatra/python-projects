import socket as s
import threading
import ipaddress as ip
from tqdm import tqdm
import subprocess
import platform

print_lock = threading.Lock()
ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 8080]

def host_live(ip_address):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", str(ip_address)]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.returncode == 0

def scan(target_ip, port_main, bar):
    server = None
    try:
        if not host_live(str(target_ip)):
            bar.update(1)
            return

        server = s.socket()
        server.settimeout(2)
        if server.connect_ex((str(target_ip), port_main)) == 0:
            with print_lock:
                print(f"[+] Port {port_main} is OPEN on {target_ip}")
    except:
        pass
    finally:
        if server:    
            server.close()
        bar.update(1)

def main():
    target = input("Enter IP in CIDR form (e.g. 192.168.1.0/24): ")
    try:
        network = ip.ip_network(target, strict=False)
        hosts = list(network.hosts())
        total_tasks = len(hosts) * len(ports)
        bar = tqdm(total=total_tasks, desc="Scanning Ports", unit="port")
        tqdm.write(f"\n[~] Scanning {len(hosts)} hosts across {len(ports)} ports ({total_tasks} tasks)\n")

        threads = []
        for host in hosts:
            for port in ports:
                thread = threading.Thread(target=scan, args=(host, port, bar), daemon=True)
                thread.start()
                threads.append(thread)

        for t in threads:
            t.join()

        bar.close()
    except Exception as e:
        print("[!] Error:", e)

main()

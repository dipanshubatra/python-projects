import socket
import ipaddress as ip
from tqdm import tqdm
import subprocess
import platform
from concurrent.futures import ThreadPoolExecutor

ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 8080]
PING_TIMEOUT = "500"  # milliseconds for ping

def host_live(ip_address):
    system_type = platform.system().lower()
    if system_type == "windows":
        command = ["ping", "-n", "1", "-w", PING_TIMEOUT, str(ip_address)]
    else:
        command = ["ping", "-c", "1", "-W", "1", str(ip_address)]
    result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0

def scan_port(target_ip, port, bar):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.settimeout(1)
            if server.connect_ex((str(target_ip), port)) == 0:
                print(f"[+] Port {port} is OPEN on {target_ip}")
    except:
        pass
    finally:
        bar.update(1)

def main():
    target = input("Enter IP in CIDR form (e.g. 192.168.1.0/24): ")
    try:
        network = ip.ip_network(target, strict=False)
        hosts = list(network.hosts())

        print("[~] Checking live hosts...")
        live_hosts = []
        with ThreadPoolExecutor(max_workers=200) as executor:
            results = list(tqdm(executor.map(host_live, hosts), total=len(hosts), desc="Pinging Hosts", unit="host"))
        live_hosts = [host for host, alive in zip(hosts, results) if alive]

        print(f"[+] Found {len(live_hosts)} live hosts.")

        total_tasks = len(live_hosts) * len(ports)
        if total_tasks == 0:
            print("[!] No live hosts found. Exiting.")
            return

        bar = tqdm(total=total_tasks, desc="Scanning Ports", unit="port")
        with ThreadPoolExecutor(max_workers=200) as executor:
            for host in live_hosts:
                for port in ports:
                    executor.submit(scan_port, host, port, bar)
        bar.close()
        print("[✓] Scan completed.")

    except Exception as e:
        print("[!] Error:", e)

if __name__ == "__main__":
    main()


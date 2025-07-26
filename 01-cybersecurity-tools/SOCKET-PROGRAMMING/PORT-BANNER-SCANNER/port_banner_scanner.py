import socket
import threading
import queue
from tqdm import tqdm

print_lock = threading.Lock()
task_q = queue.Queue()
target = input("Enter the IP you want to scan: ")
n= int(input("enter how many upto ports"))
progress_bar = tqdm(total=n, desc="Scanning Ports", unit="port")
def scan():
    while True:
        try:
            port = task_q.get(timeout=3)     
        except queue.Empty:
            break

        try:
            sock = socket.socket()
            sock.settimeout(0.5)                
            if sock.connect_ex((target, port)) == 0:
                try:
                    banner = sock.recv(1024).decode(errors="ignore").strip()
                    with print_lock:
                        if banner:
                            tqdm.write(f"[{port:>5}] OPEN - {banner}")
                        else:
                            tqdm.write(f"[{port:>5}] OPEN - (no banner)")
                except socket.timeout:
                    with print_lock:
                        tqdm.write(f"[{port:>5}] OPEN - (no banner / timed out)")
        except Exception as e:
            pass
        finally:
            sock.close()
            task_q.task_done()
            progress_bar.update(1)
for _ in range(300):
    threading.Thread(target=scan, daemon=True).start()

for port in range(1, n+1):                      
    task_q.put(port)

task_q.join()                    
print("\r"+"  "*30,end="") 
progress_bar.close()       
print("Scan complete ✔️")

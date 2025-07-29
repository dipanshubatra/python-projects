
# 🧪 DNS Spoofing Tool (Python + Scapy + NetfilterQueue)

A powerful educational tool to **intercept and spoof DNS responses** in real-time.  
This project demonstrates how attackers can redirect traffic from a legitimate domain (e.g. `neverssl.com`) to a **malicious IP** using MITM tactics via Python.

---

[![📂 Open Code](https://img.shields.io/badge/📂%20Open%20DNS--Spoofing--Tool-blue?style=for-the-badge)](https://github.com/dipanshubatra/python-projects/blob/main/01-cybersecurity-tools/NETWORK-ATTACK-TOOLS/Dns-spoofing-tool/dns_spoofing.py)
[![🧾 Download ZIP](https://img.shields.io/badge/🧾%20Download%20ZIP-green?style=for-the-badge&logo=github)](https://github.com/dipanshubatra/python-projects/archive/refs/heads/main.zip)

---

## 🚀 Features

- 🎯 Spoofs a specific domain (e.g., `neverssl.com`)  
- 💡 Redirects DNS queries to a fake/malicious IP  
- 🧠 Uses NetfilterQueue for live packet capture  
- ⚙️ Scapy used to craft & modify DNS responses  
- 🧼 Clears checksum and length headers for valid packets  
- ⌨️ Graceful exit with `CTRL+C`  

---

## 📁 Folder Structure

```
dipanshubatra/
└── python-projects/
    └── 01-cybersecurity-tools/
        └── NETWORK-ATTACK-TOOLS/
            └── Dns-spoofing-tool/
                └── dns_spoofing.py
```

---

## 💻 How to Run

### 1️⃣ Download or Clone the Project

```bash
git clone https://github.com/dipanshubatra/python-projects.git
```

---

### 2️⃣ Navigate to the Tool Directory

```bash
cd python-projects/01-cybersecurity-tools/NETWORK-ATTACK-TOOLS/Dns-spoofing-tool
```

---

### 3️⃣ Install Required Packages

```bash
pip install scapy netfilterqueue
sudo apt install libnetfilter-queue-dev
```

---

### 4️⃣ Setup iptables Rules

```bash
sudo iptables -I FORWARD -j NFQUEUE --queue-num 0
```

✅ For local testing (optional):

```bash
sudo iptables -I OUTPUT -j NFQUEUE --queue-num 0
sudo iptables -I INPUT -j NFQUEUE --queue-num 0
```

---

### 5️⃣ Run the Tool

```bash
sudo python3 dns_spoofing.py
```

---

### 6️⃣ Cleanup

```bash
sudo iptables --flush
```

---

## 🧪 Sample Output

```bash
[+] DNS Spoofing started... Press CTRL+C to stop
[+] Spoofing: neverssl.com ➜ 142.250.193.142
```

---

## 🧠 Tech Stack

- Python 3.x  
- Scapy  
- NetfilterQueue  
- iptables (Linux only)

---

## ⚠️ Disclaimer

This tool is for **educational and authorized testing** purposes only.  
🚫 Never run it on public networks or without permission.

---

## 📄 License

MIT License — free and open source.

---

## 🙌 Credits

Built with ❤️ by [dipanshubatra](https://github.com/dipanshubatra)
```

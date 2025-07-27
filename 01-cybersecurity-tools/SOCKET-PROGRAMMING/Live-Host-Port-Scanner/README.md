# 🔍 Live Host Multi-Port Scanner (CIDR + Ping + Threads)

A beginner-friendly, high-speed port scanner that takes a CIDR IP range, checks which hosts are **live** using `ping`, and scans multiple common ports in parallel using Python’s `threading` and `socket` modules. A clean and efficient tool for internal network assessments.

---

[![📂 Open Code](https://img.shields.io/badge/📂%20Open%20Scanner--blue?style=for-the-badge)](https://github.com/dipanshubatra/python-projects/blob/main/01-cybersecurity-tools/SOCKET-PROGRAMMING/Live-Host-Port-Scanner/live_host_multi_port_scanner.py)
[![Download ZIP](https://img.shields.io/badge/Download-ZIP-green?style=for-the-badge)](https://github.com/dipanshubatra/python-projects/archive/refs/heads/main.zip)

---

## 🚀 Features

- 🧠 CIDR support (e.g., `192.168.1.0/24`)
- 🛰️ Detects only **live hosts** using platform-aware `ping`
- ⚡ Scans 14+ common ports in parallel using threads
- 🧵 Thread-safe print locking
- 📊 TQDM-based real-time progress bar
- 🧱 Works on Windows, Linux, and macOS

---

## 📁 Folder Structure

```
dipanshubatra/
└── python-projects/
    └── 01-cybersecurity-tools/
        └── SOCKET-PROGRAMMING/
            └── Live-Host-Port-Scanner/
                └── live_host_multi_port_scanner.py
```

---

## 💻 How to Run

### 1️⃣ Download the Project

> 📥 [Click here to Download ZIP](https://github.com/dipanshubatra/python-projects/archive/refs/heads/main.zip)

or clone it using Git:

```bash
git clone https://github.com/dipanshubatra/python-projects.git
```

---

### 2️⃣ Navigate to the Folder

```bash
cd python-projects/01-cybersecurity-tools/SOCKET-PROGRAMMING/Live-Host-Port-Scanner
```

---

### 3️⃣ Run the Scanner

```bash
python live_host_multi_port_scanner.py
```

Input example:

```text
Enter IP in CIDR form (e.g. 192.168.1.0/24): 192.168.1.0/24
```

---

## 🧪 Sample Output

```bash
[~] Scanning 254 hosts across 14 ports (3556 tasks)

Scanning Ports:  45%|██████████▊              | 1600/3556 [00:08<00:09, 210.00port/s]
[+] Port 80 is OPEN on 192.168.1.10
[+] Port 443 is OPEN on 192.168.1.10
[+] Port 22 is OPEN on 192.168.1.11
```

---

## 🧠 Tech Stack

- Python 3.x
- `socket`
- `threading`
- `ipaddress`
- `platform`, `subprocess`
- `tqdm`

---

## ⚠️ Disclaimer

This project is for educational and internal testing purposes only.  
Do not scan public networks or third-party systems without permission.

---

## 📄 License

MIT License — open-source and free to use.

---

## 🙌 Credits

Built with ❤️ by [dipanshubatra](https://github.com/dipanshubatra)

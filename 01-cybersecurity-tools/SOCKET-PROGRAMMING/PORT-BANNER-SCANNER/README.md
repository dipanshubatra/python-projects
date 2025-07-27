# 🛰️ Port Banner Scanner — Made by Dip_NYX

A blazing-fast, multithreaded port scanner with live banner grabbing. Built using Python's `socket`, `threading`, `queue`, and `tqdm` for smooth, real-time scanning.

---

[![📂 Open Code](https://img.shields.io/badge/📂%20Open%20Port%20Scanner--blue?style=for-the-badge)](https://github.com/dipanshubatra/python-projects/blob/main/01-cybersecurity-tools/SOCKET-PROGRAMMING/PORT-BANNER-SCANNER/port_banner_scanner.py)
[![Download ZIP](https://img.shields.io/badge/Download-ZIP-green?style=for-the-badge)](https://github.com/dipanshubatra/python-projects/archive/refs/heads/main.zip)


---

## ⚡ Features (with Deep Explanation)

### 🔎 1. High-Speed Port Scanner

Scan any target IP for open ports — blazing fast using **300 threads**.

* Scans from port `1` up to your given number  
* Efficient queue-based multithreading  
* Displays which ports are **OPEN**

---

### 🎯 2. Banner Grabbing

Identifies services running on open ports:

* Uses `socket.recv()` to grab service banners  
* Helps identify services like FTP, SSH, Apache, etc.  
* Handles timeouts and empty responses gracefully

---

### 📊 3. Live Progress Bar

Integrated with `tqdm` to show scanning progress:

* Real-time progress updates  
* Displays scanning rate and time remaining

---

### 🛡️ 4. Safe and Clean Output

* Locks output using `threading.Lock` for clean logs  
* Gracefully skips errors and closes sockets  
* Organized open ports with or without banners

---

## 🧠 Example Output

```bash
Enter the IP you want to scan: 127.0.0.1
enter how many upto ports: 100
Scanning Ports: 100%|███████████████████████████| 100/100 [00:02<00:00, 51.20port/s]
[   22] OPEN - SSH-2.0-OpenSSH_8.9
[   80] OPEN - Apache/2.4.52 (Ubuntu)
[  443] OPEN - (no banner / timed out)
Scan complete ✔️
```

---

## 🗂 Folder Structure

```bash
01-cybersecurity-tools/
└── SOCKET-PROGRAMMING/
    └── PORT-BANNER-SCANNER/
        ├── port_banner_scanner.py      # Main Scanner Script
        └── README.md                   # This file
```

---

## ⚙️ Requirements

Install `tqdm`:

```bash
pip install tqdm
```

> No external libraries needed beyond `tqdm`

---

## 🏁 How to Run

```bash
python port_banner_scanner.py
```

It will ask:

- 🔹 IP Address to scan  
- 🔹 Number of ports (e.g. 100, 1000, etc.)

---

## 📄 License

This project is under the **MIT License**.  
Use it freely for learning, testing, or cybersecurity practice.

---

## 👨‍💻 Made with ⚔️ by [Dip_NYX](https://github.com/dipanshunyx)

If you found this useful — drop a ⭐ on the repo and share it with your team.

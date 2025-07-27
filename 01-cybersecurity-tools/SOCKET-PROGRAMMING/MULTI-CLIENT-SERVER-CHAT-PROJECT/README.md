# 💬 Multi-Client Server Chat App (Python Socket + Threading)

A beginner-friendly socket programming project where multiple clients can connect to a server and chat with each other in real-time. Built using Python's `socket` and `threading` modules.

---

[![📂 Server Code](https://img.shields.io/badge/📂%20Open%20Server--blue?style=for-the-badge)](https://github.com/dipanshubatra/python-projects/blob/main/01-cybersecurity-tools/SOCKET-PROGRAMMING/MULTI-CLIENT-SERVER-CHAT-PROJECT/server.py)
[![📂 Client Code](https://img.shields.io/badge/📂%20Open%20Client--blue?style=for-the-badge)](https://github.com/dipanshubatra/python-projects/blob/main/01-cybersecurity-tools/SOCKET-PROGRAMMING/MULTI-CLIENT-SERVER-CHAT-PROJECT/client.py)
[![⬇️ Download ZIP](https://img.shields.io/badge/⬇️%20Download-All-Files-green?style=for-the-badge)](https://github.com/dipanshubatra/python-projects/archive/refs/heads/main.zip)

---

## 🚀 Features

- 📡 Multiple clients can chat simultaneously
- 👤 Unique name for each client
- 🔁 Broadcast messages to all clients
- 🔌 Graceful disconnection
- ⚙️ Built with pure Python sockets

---

## 📁 Folder Structure

dipanshubatra/
└── python-projects/
└── 01-cybersecurity-tools/
└── SOCKET-PROGRAMMING/
└── MULTI-CLIENT-SERVER-CHAT-PROJECT/
├── server.py
└── client.py

yaml
Copy
Edit

---

## 💻 How to Run

### 1️⃣ Clone or Download ZIP

> 📥 [Click here to Download ZIP](https://github.com/dipanshubatra/python-projects/archive/refs/heads/main.zip)

or clone using Git:

```bash
git clone https://github.com/dipanshubatra/python-projects.git
2️⃣ Start the Server
bash
Copy
Edit
cd python-projects/01-cybersecurity-tools/SOCKET-PROGRAMMING/MULTI-CLIENT-SERVER-CHAT-PROJECT
python server.py
You will see:

pgsql
Copy
Edit
server is listening ,,,,,,,,,,,
[+] New connection is added
3️⃣ Start the Client(s)
Open another terminal window:

bash
Copy
Edit
python client.py
Enter your name when asked:

yaml
Copy
Edit
enter your name: dipu
Then start chatting:

makefile
Copy
Edit
You: hello guys
On server terminal:

ruby
Copy
Edit
dipu :- hello guys
🧪 Sample Output (Multiple Clients)
pgsql
Copy
Edit
[Server Output]
server is listening ,,,,,,,,,,,
[+] New connection is added
[+] New connection is added
ram :- hello bro
shyam :- hi ram

[Client 1 Output]
enter your name: ram
You: hello bro

[Client 2 Output]
enter your name: shyam
You: hi ram
🧠 Tech Stack
Python 3.x

socket

threading

⚠️ Disclaimer
This project is for educational/demo purposes only. Not intended for production or public networks.

📄 License
MIT License — feel free to use and modify.

🙌 Credits
Built with ❤️ by dipanshubatra

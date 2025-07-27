# 🛡️ CyberSecurity Toolkit GUI — Made by Dip\_NYX

A powerful and stylish Python GUI toolkit for cybersecurity tasks. Built using `CustomTkinter`, this tool provides password storage, encryption, and admin-level controls — all in a single offline desktop app.

---
[![📂 Get Code](https://img.shields.io/badge/📂%20Open%20Code--blue?style=for-the-badge)](https://github.com/dipanshubatra/python-projects/blob/main/01-cybersecurity-tools/CyberSecurity-Toolkit-GUI/cyber_toolkit.py)
[![⬇️ Download ZIP](https://img.shields.io/badge/⬇️%20Download-ZIP-green?style=for-the-badge)](https://github.com/dipanshubatra/python-projects/archive/refs/heads/main.zip)

---

## 🧠 Features (with Detailed Explanation)

### 🔐 1. Password Saver Tool

Save your credentials (website/app name, username, and password) securely in a local `.txt` file.

* All data is saved in `save-password.txt`
* Designed to work **offline only** — nothing is uploaded online
* Prevents empty field saving with proper validation
* View saved data only after entering the correct **admin password**

---

### 👀 2. View Saved Passwords

You can view all previously saved credentials using the **"View saved password"** button.

* Requires **admin password** to unlock
* Opens a readable textbox with saved entries
* Includes an option to **🗑️ delete all passwords** if needed

---

### 🔑 3. Cipher Encoder/Decoder Tool

Encode or decode secret messages using a **custom symbol-based encryption system**:

* Uppercase letters → `⊙` codes
* Lowercase letters → `§` codes
* Spaces → `¤`
* Final result is **reversed and symbol-separated**

#### Example:

```text
HELLO → ⊙72#⊙69#⊙76#⊙76#⊙79 → reversed → ⊙79#⊙76#⊙76#⊙69#⊙72
```

You can also **decode back** using the Decoder tab.

---

### 🧑‍💻 4. Admin Panel

A secure control panel to:

* ✅ **Change master password**
* 🗑️ **Delete all saved credentials**
* 📊 **View total saved passwords and file size**
* Master password is saved locally in `admin-pass.txt`

---

### 🔐 5. Master Password System

Every major operation (view passwords, use encryption, access admin tools) requires correct admin authentication.

* Default password: `dipanshunyx`
* You can update this from the Admin Panel
* Ensures that unauthorized users cannot access or delete data

---

### 💡 6. Typing Animation Labels

All titles and headings have smooth animated "typing" effects for better UI feel.

* Built with a custom animation function using `.after()`

---

### 🎨 7. Beautiful Dark-Themed GUI

Built with `CustomTkinter` for:

* Rounded buttons
* Modern themes
* Tab layout (Encode / Decode / Admin / About)
* Animations and consistent layout

---

### 📋 8. About Tab + GitHub Link

The **About** section provides:

* Project version
* Credits to the developer (you)
* 🔗 Clickable GitHub profile link: [github.com/dipanshunyx](https://github.com/dipanshunyx)

---

## 🗂 Folder Structure

```
CyberSecurity-Toolkit-GUI/
├── cyber_toolkit.py          # Main GUI App
├── admin-pass.txt            # Master password storage
├── save-password.txt         # Saved credentials
├── README.md                 # This file
└── requirements.txt          # Required modules
```

---

## ⚙️ Requirements

Install all required packages:

```bash
pip install -r requirements.txt
```

Manual install:

```bash
pip install customtkinter
```

---

## 🏁 How to Run

1. **Clone the repo** or **Download ZIP**

```bash
git clone https://github.com/dipanshunyx/Python-Projects.git
cd Python-Projects/CyberSecurity-Toolkit-GUI
```

2. **OR Download ZIP**

* Go to [https://github.com/dipanshunyx/Python-Projects](https://github.com/dipanshunyx/Python-Projects)
* Click on `<> Code` button and select `Download ZIP`
* Extract it and open folder `CyberSecurity-Toolkit-GUI`

3. **Run the main file**

```bash
python cyber_toolkit.py
```

---

## 🧾 License

This project is under the **MIT License**.
Use it freely for educational or personal projects.

---

## 🧑‍💻 Made with ❤️ by [Dip\_NYX](https://github.com/dipanshunyx)

If you like this tool, don’t forget to ⭐ star the repo and share it!

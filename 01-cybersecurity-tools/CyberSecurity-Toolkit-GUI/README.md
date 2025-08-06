# 🛡️ CyberSecurity Toolkit GUI — Made by Dip_NYX

A powerful and stylish Python GUI toolkit for cybersecurity tasks. Built using `CustomTkinter`, this tool provides password storage, encryption, and admin-level controls — all in a single offline desktop app.

---
[![📂 Get Code](https://img.shields.io/badge/📂%20Open%20Code--blue?style=for-the-badge)](https://github.com/dipanshubatra/python-projects/blob/main/01-cybersecurity-tools/CyberSecurity-Toolkit-GUI/cyber_toolkit.py)
[![⬇️ Download ZIP](https://img.shields.io/badge/⬇️%20Download-ZIP-green?style=for-the-badge)](https://github.com/dipanshubatra/python-projects/archive/refs/heads/main.zip)

---

## 🧠 Features (with Detailed Explanation)

### 🔐 1. Password Saver Tool
Save your credentials (website/app name, username, and password) securely in a local `.txt` file.

- All data is saved in `save-password.txt`
- Works **offline only**
- Prevents empty field saving with proper validation
- View saved data only after entering the correct **admin password**

---

### 👀 2. View Saved Passwords
Use the **"View saved password"** button to see stored credentials.

- Requires **admin password** to unlock
- Opens a textbox with saved entries
- Option to **🗑️ delete all passwords**

---

### 🔑 3. Cipher Encoder/Decoder Tool
Encode or decode secret messages using a **custom symbol-based encryption system**:

- Uppercase letters → `⊙` codes  
- Lowercase letters → `§` codes  
- Spaces → `¤`  
- Result is **reversed and symbol-separated**

**Example:**
HELLO → ⊙72#⊙69#⊙76#⊙76#⊙79 → reversed → ⊙79#⊙76#⊙76#⊙69#⊙72

yaml
Copy
Edit

Decoder tab can reverse the cipher back to readable text.

---

### 🧑‍💻 4. Admin Panel
Secure control panel to:

- ✅ Change master password
- 🗑️ Delete all saved credentials
- 📊 View total saved passwords and file size

*Master password saved locally in `admin-pass.txt`*

---

### 🔐 5. Master Password System

- Default password: `dipanshunyx`
- Required for viewing passwords, admin access, encoding
- Changeable from Admin Panel
- Prevents unauthorized access or deletion

---

### 💡 6. Typing Animation Labels

- Smooth animated typing for labels and headings
- Implemented using `.after()` method in Tkinter

---

### 🎨 7. Beautiful Dark-Themed GUI

Built using `CustomTkinter`:

- Rounded buttons
- Modern design
- Tab layout: Encode / Decode / Admin / About
- Consistent layout and dark theme

---

### 📋 8. About Tab + GitHub Link

- Project version
- Developer credits
- 🔗 Clickable GitHub profile link: [github.com/dipanshunyx](https://github.com/dipanshunyx)

---

## 🗂 Folder Structure

python-projects/
└── 01-cybersecurity-tools/
└── CyberSecurity-Toolkit-GUI/
├── cyber_toolkit.py # Main GUI App
├── admin-pass.txt # Master password storage
├── save-password.txt # Saved credentials
├── shiftvalue.txt # Cipher shift value
├── README.md # This file
└── requirements.txt # Required modules

yaml
Copy
Edit

---

## ⚙️ Requirements

Install all required packages:


pip install -r requirements.txt
Or manually:

bash
Copy
Edit
pip install customtkinter
##🏁 How to Run
Clone the repo or Download ZIP

bash
Copy
Edit
git clone https://github.com/dipanshunyx/Python-Projects.git
cd Python-Projects/01-cybersecurity-tools/CyberSecurity-Toolkit-GUI
OR Download ZIP

Go to: https://github.com/dipanshunyx/Python-Projects

Click on <> Code → Download ZIP

Extract and open folder CyberSecurity-Toolkit-GUI

Run the main file

bash
Copy
Edit
python cyber_toolkit.py
##🧾 License
This project is under the MIT License.
Use it freely for educational or personal projects.

##🧑‍💻 Made with ❤️ by Dip_NYX
If you like this tool, don’t forget to ⭐ star the repo and share it!

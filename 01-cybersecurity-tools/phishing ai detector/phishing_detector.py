import customtkinter as ctk
import joblib
import pandas as pd
import time
import pathlib

model = joblib.load("phish_detector.pkl")
features_names = model.feature_names_in_

def get_features(url):
    features = []
    features.append(1 if len(url) < 75 else -1)
    features.append(-1 if "@" in url else 1)
    features.append(1 if url.startswith("https") else -1)
    features.append(-1 if "-" in url else 1)
    features.append(-1 if url.count(".") > 3 else 1)
    bad_words = ["login", "bank", "secure", "update", "free", "verify"]
    features.append(-1 if any(word in url.lower() for word in bad_words) else 1)
    while len(features) < len(features_names):
        features.append(0)
    return pd.DataFrame([features], columns=features_names)

def check_url():
    url = entry_url.get().strip()
    if url == "":
        show_result("Please enter a URL", "orange")
        return
    show_result("Checking...", "cyan")
    time.sleep(1.2)
    features = get_features(url)
    prediction = int(model.predict(features)[0])
    if prediction == 1:
        show_result("⚠️ Phishing Website", "red")
        add_history(url, "Phishing")
    else:
        show_result("✅ Legit Website", "green")
        add_history(url, "Legit")

def show_result(text, color):
    label_result.configure(text=text, text_color=color)
    if text not in ("Checking...",):
        app.after(3000, lambda: label_result.configure(text=""))

def add_history(url, status):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    text_history.insert("end", f"{timestamp} | {status} | {url}\n")
    text_history.see("end")

def save_history():
    path = pathlib.Path("phish_history.txt")
    path.write_text(text_history.get("1.0", "end").strip())
    show_result("History saved!", "cyan")

def clear_history():
    text_history.delete("1.0", "end")
    show_result("History cleared", "cyan")

def load_samples():
    samples = [
        "http://secure-update-login.com/bankofamerica/login",
        "http://paypal-login-freeverify.com/account/update",
        "http://verify-login-secure.net/chasebank/login",
        "http://free-gift-card-amazon.com/login",
        "http://secure-bank-update.net/account/verify"
    ]
    for s in samples:
        text_history.insert("end", f"SAMPLE | {s}\n")
    show_result("Sample URLs loaded", "cyan")

def toggle_theme():
    mode = ctk.get_appearance_mode()
    ctk.set_appearance_mode("Light" if mode == "Dark" else "Dark")

def go_back():
    app.destroy()

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("PhishDetect")
app.geometry("600x600")
app.resizable(False, False)

frame = ctk.CTkFrame(app, width=560, height=560, corner_radius=18)
frame.place(relx=0.5, rely=0.5, anchor="center")

label_title = ctk.CTkLabel(frame, text="PhishDetect", font=("Segoe UI", 20, "bold"))
label_title.place(x=24, y=18)

btn_theme = ctk.CTkButton(frame, text="Toggle Theme", width=120, height=30, corner_radius=10, command=toggle_theme)
btn_theme.place(x=420, y=18)

entry_url = ctk.CTkEntry(frame, width=512, height=42, corner_radius=12, placeholder_text="Enter website URL here")
entry_url.place(x=24, y=64)

btn_check = ctk.CTkButton(frame, text="Check URL", width=200, height=44, corner_radius=12, command=check_url)
btn_check.place(x=190, y=120)

label_result = ctk.CTkLabel(frame, text="", font=("Segoe UI", 16, "bold"))
label_result.place(x=24, y=180)

frame_history = ctk.CTkFrame(frame, width=512, height=290, corner_radius=12)
frame_history.place(x=24, y=220)

label_hist = ctk.CTkLabel(frame_history, text="History", font=("Segoe UI", 14, "bold"))
label_hist.place(x=12, y=8)

text_history = ctk.CTkTextbox(frame_history, width=488, height=240, corner_radius=8, font=("Consolas", 11))
text_history.place(x=12, y=36)

btn_save = ctk.CTkButton(frame, text="Save", width=100, height=36, corner_radius=10, command=save_history)
btn_save.place(x=60, y=522)

btn_clear = ctk.CTkButton(frame, text="Clear", width=100, height=36, corner_radius=10, command=clear_history)
btn_clear.place(x=180, y=522)

btn_sample = ctk.CTkButton(frame, text="Samples", width=100, height=36, corner_radius=10, command=load_samples)
btn_sample.place(x=300, y=522)

btn_back = ctk.CTkButton(frame, text="Back", width=100, height=36, corner_radius=10, command=go_back)
btn_back.place(x=420, y=522)

app.mainloop()

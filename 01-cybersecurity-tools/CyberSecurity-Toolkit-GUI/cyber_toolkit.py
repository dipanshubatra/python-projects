import os
ADMIN_PASS_FILE = "admin-pass.txt"
DEFAULT_ADMIN   = "dipanshunyx"
import customtkinter as ctk
import tkinter.messagebox as mb
app = None
bt6 = None
app5 = None        
bt5 = None
app1 = None
bt2 = None
weblabel1 = None
bt3 = None
app4 = None
web5entry = None
bframe= None
app2 = None
app7  = None
web9entry =None
bt8 = None
text2 = None
web11entry =None
panel = None
################################################################################        
def animat_label(widgetlabel,texttotype,delay=100):
    def typeanimate(i=0):
        if i<len(texttotype):
            widgetlabel.configure(text=texttotype[:i+1])
            widgetlabel.after(delay,typeanimate,i+1)
    typeanimate()        



################################################################################
def view():
    global bframe
    if web5entry.get().lower() == 'dipanshunyx':
        try:
            with open("save-password.txt","r") as file:
                content = file.read()
        except FileNotFoundError:
            content = "no pass fiile not found "
        bt5.configure(state="disabled")
        app4.destroy()
        app3 = ctk.CTk()
        app3.title("saved passwords")
        app3.geometry("600x600")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        label1 = ctk.CTkLabel(app3,text="")
        label1.pack(pady=20)
        animat_label(label1,"your saved passowrds ")
        text = ctk.CTkTextbox(app3,width=500,height=250)
        text.insert("0.0",content)
        text.configure(state = 'disabled')
        text.pack(pady=10)
        bt_delete = ctk.CTkButton(app3, text="🗑️ Delete All Passwords", width=150, command=delete_saved_passwords)
        bt_delete.pack(pady=10)
        bt4 = ctk.CTkButton(app3,text="close",command=app3.destroy)
        bt4.pack(pady=10)
        app3.mainloop()
    else:
        global app5,bt6
        app5 = ctk.CTk()
        app5.title("wrong pass")
        app5.geometry("250x100")
        bt6 = ctk.CTkButton(app5,text="ok",command=app5.destroy)
        bt6.pack(pady=5)
        app5.mainloop()
def delete_saved_passwords():
    try:
        with open("save-password.txt", "w") as file:
            file.write("")
        confirm = ctk.CTk()
        confirm.title("Deleted ✅")
        confirm.geometry("400x120")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        label = ctk.CTkLabel(confirm, text="All saved passwords have been deleted.")
        label.pack(pady=10)
        btn = ctk.CTkButton(confirm, text="OK", command=confirm.destroy)
        btn.pack(pady=10)
        confirm.mainloop()
    except Exception as e:
        error = ctk.CTk()
        error.title("Error ❌")
        error.geometry("400x120")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        label = ctk.CTkLabel(error, text=f"Error: {e}")
        label.pack(pady=10)
        btn = ctk.CTkButton(error, text="OK", command=error.destroy)
        btn.pack(pady=10)
        error.mainloop()

def pass_saver():   
    global weblabel,bframe,app2,app
    if app2:
        app2.destroy()
    
    def check():
        global bt5,app1,bt2,weblabel1,bt3,app4,web5entry
        app4 = ctk.CTk()
        app4.geometry("300x250")
        app4.title("Checking are you a uknown person?")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        web5label = ctk.CTkLabel(app4,text="")
        web5label.pack(pady=20)
        animat_label(web5label,"Enter the admin pass to continue")
        web5entry = ctk.CTkEntry(app4,width=300,placeholder_text="***************",show='*')
        web5entry.pack(pady=20)
        bt5 = ctk.CTkButton(app4,text="fetch",command=view,corner_radius=100)
        bt5.pack(pady=20)
        app4.mainloop()
################################################################################   
     
    def hey():
        global app1,bt2,web3label 
        if webentry.get() == '' or web2entry.get() == "" or web4entry.get()=="" :
            app1 = ctk.CTk()
            app1.title("error❌")
            app1.geometry("500x150")
            ctk.set_appearance_mode("dark")
            ctk.set_default_color_theme('green')
            web3label = ctk.CTkLabel(app1,text="")
            web3label.pack(pady=10)
            animat_label(web3label,"enter all the fields")
            bt2 = ctk.CTkButton(app1,text="ok",command=app1.destroy,corner_radius=100)
            bt2.pack(pady=10)
            app1.mainloop()
        else:
            web = webentry.get()
            use= web2entry.get()
            use1 = web4entry.get()
            with open('save-password.txt','a') as file:
                file.write(f"Website name - {web} \n username/Id -{use}\n Password - {use1}\n {'-'*40}\n")
            sucess = ctk.CTk()
            sucess.title("saved✅")    
            sucess.geometry("500x150")
            ctk.set_appearance_mode("dark")
            ctk.set_default_color_theme("green")
            web4lablel = ctk.CTkLabel(sucess,text="",font=("Arial",26))
            web4lablel.pack(pady=10)
            animat_label(web4label,"Saved the file in save-password.txt")
            bt3 = ctk.CTkButton(sucess,text="ok",command=sucess.destroy,corner_radius=100)
            bt3.pack(pady=10)
            sucess.mainloop()
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")
    app = ctk.CTk()
    app.title("Dipanshunyx cyber tools ")
    app.geometry("600x500")
    label = ctk.CTkLabel(app, text="", font=('Arial Rounded MT Bold', 20))
    label.pack(pady=20)
    animat_label(label,'🔏Secure password tool')
    weblabel = ctk.CTkLabel(app,text='',font=("Arial",16))
    weblabel.pack(pady=(10,0))
    animat_label(weblabel,'(WEBSITE/APP) - NAME')
    webentry = ctk.CTkEntry(app,width=500,placeholder_text="e.g Insta,GMail,e.t.c")
    webentry.pack(pady=5)
    web2label = ctk.CTkLabel(app,text='',font=("Arial",16))
    web2label.pack(pady=(10,0))
    animat_label(web2label,"Username/Id")
    web2entry =  ctk.CTkEntry(app,width=500,placeholder_text="eg my_id,cyber@gmail.com,e.t.c.",show="*")
    web2entry.pack(pady=5)
    web4label = ctk.CTkLabel(app,text="",font=('Arial',16))
    web4label.pack(pady=(10,0))
    animat_label(web4label,"PASSWORD/KEY - ")
    web4entry = ctk.CTkEntry(app,width=500,placeholder_text="eg,1234,e.t.c",show= "*")
    web4entry.pack(pady=5)
    bframe = ctk.CTkFrame(app)
    bframe.pack(pady=20)
    bt1 = ctk.CTkButton(bframe,text="✅SAVE PASSWORD",width=150,command=hey,corner_radius=100)
    bt1.pack(pady=20)
    bt4 = ctk.CTkButton(bframe,text="View saved password",width=150,command=check,corner_radius=100)
    bt4.pack(pady=10)
    bt5 = ctk.CTkButton(bframe,text="Back To Tools",width=150,command=login,corner_radius=100)
    bt5.pack(pady=10)
    app.mainloop()
################################################################################    
def_char = [' ', 'Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh', 'Ii','Jj', 'Kk', 'Ll', 'Mm', 'Nn', 'Oo', 'Pp', 'Qq', 'Rr', 'Ss','Tt', 'Uu', 'Vv', 'Ww', 'Xx', 'Yy', 'Zz']
mainx = def_char.copy()
def cypher_nyx():
    global app2,app7,web9entry,text1,web11entry,text2,panel
    if app2:
        app2.destroy()
    if panel:
        panel.destroy()    
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")
    app7 = ctk.CTk()
    app7.title("CYPHER TOOL by DIPANSHU")
    app7.geometry("600x500")
    web8label = ctk.CTkLabel(app7,text="",font=("Ubuntu",22,"bold"))
    web8label.pack(pady=(10,0))
    animat_label(web8label,"CYPHER TOOL🧑‍💻")
    tabview1 = ctk.CTkTabview(app7,width=560,height=460,corner_radius=20)
    tabview1.pack(padx=20,pady=20)
    tabv1 = tabview1.add("ENCODE")
    tabv2 = tabview1.add("DECODE")
    tabv3 = tabview1.add("ADMiN")
    tabv4 = tabview1.add("ℹ️ About")
    web9label = ctk.CTkLabel(tabv1,text="",font=("Ubuntu",26,"bold"))
    web9label.pack(pady=(70,0))
    animat_label(web9label,"(Encode - 🔑)")
    web10label = ctk.CTkLabel(tabv2,text="",font=("Ubuntu",26,"bold"))
    web10label.pack(pady=(70,0))
    animat_label(web10label,"(Decode - 🔑)")
    web11label = ctk.CTkLabel(tabv3,text="",font=("Ubuntu",26,"bold"))
    web11label.pack(pady=(70,0))
    animat_label(web11label,"ADMIN🧕")
    web9entry= ctk.CTkEntry(tabv1,width=500,placeholder_text="Encode.......",corner_radius=15)
    web9entry.pack(pady=20)
    text1 = ctk.CTkTextbox(tabv1,width=500,height=50)
    text1.pack(pady=10)
    bt11 = ctk.CTkButton(tabv1,text="Encode",width=100,height=44,command=encode,corner_radius=50)
    bt11.pack(pady=(10,0))
    bt8 = ctk.CTkButton(tabv1,text="back",width=100,height=44,command=login,corner_radius=100)
    bt8.pack(pady=(10,0))
    admin_btn = ctk.CTkButton(tabv3, text="Open Admin Panel",
                          width=160, height=44, command=admin_panel,
                          corner_radius=100)
    admin_btn.pack(pady=(30, 0))
    bt12 = ctk.CTkButton(tabv3,text="back",width=100,height=44,command=login,corner_radius=100)
    bt12.pack(pady=(30,0))

    web11entry = ctk.CTkEntry(tabv2,width=500,placeholder_text="Enter text to Decode",corner_radius=15)
    web11entry.pack(pady=20)
    text2 = ctk.CTkTextbox(tabv2,width=500,height=50)
    text2.pack(pady=10)
    bt12 = ctk.CTkButton(tabv2,width=100,height=44,text="Decode",corner_radius=100,command=decodenyx)
    bt12.pack(pady=(10,0))
    bt9 = ctk.CTkButton(tabv2,width=100,height=44,text="Back",command=login,corner_radius=100)
    bt9.pack(pady=(10,0))
    about_text = "Created by Dipanshu aka DIP_NYX\nVersion 1.0\nEnjoy using the Cypher tool!"
    about_label = ctk.CTkLabel(tabv4, text=about_text, font=("Consolas", 14))
    about_label.pack(pady=(40, 10))

    github_label = ctk.CTkLabel(
    tabv4,
    text="🔗 Visit my GitHub: github.com/dipanshunyx",
    font=("Consolas", 13),
    text_color="skyblue",
    cursor="hand2")
    github_label.pack(pady=10)

    def open_github(event):
        import webbrowser
        webbrowser.open("https://github.com/dipanshunyx")

    github_label.bind("<Button-1>", open_github)

    app7.mainloop()
def encode():
    global web9entry,app7
    if web9entry.get() == "":
        mb.showerror('missing something.....','Enter something to encode into special character')
    else:
        result=[]
        encoded_history = []
        encoded = web9entry.get()
        for char in encoded:
            for  idx,pair in enumerate(mainx):
                if char in pair :
                    if char == ' ':
                        result.append(f'¤')
                    elif char.isupper():
                        result.append(f'⊙{idx+64}')
                    elif char.islower():
                        result.append(f'§{idx+64}')
                    break
        encodede = '#'.join(result)       
        encodede = encodede[::-1]
        encoded_history.append(encodede)
        return text1.insert('0.0',encodede)
################################################################################        
def decodenyx():
    global history_d,web11entry,text2
    if web11entry.get() == "":
        mb.showerror("missing input",'required field must be filled')
    else:
        history_d = []
        emp = ""
        hello =web11entry.get()
        hello = hello[::-1] 
        hello1 = hello.split("#")
        for char in hello1 :
            if char == '¤':
                emp+= " " 
            elif char.startswith('⊙') or char.startswith('§'):
                case = char[0]
                index = int(char[1:]) - 64
                if 0 <= index < len(mainx):
                    char = mainx[index][0] if case == "⊙" else mainx[index][1]
                    emp += char
        history_d.append(emp)
        return text2.insert("0.0",emp)
#####################################################################################
def login():
    global app2,app
    if app:    
        app.destroy()
    if app7:
        app7.destroy()    
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    app2 = ctk.CTk()
    app2.title("CYBER TOOLS MADE BY DIPANSHU")
    app2.geometry("600x500")

    heading_label = ctk.CTkLabel(app2, text="", font=('Ubuntu', 22, "bold"))
    heading_label.pack(pady=(20, 10))
    animat_label(heading_label, "🥳 DIP_NYX CYBER TOOLS 💀")

    tabview = ctk.CTkTabview(app2, width=560, height=460,corner_radius=50)
    tabview.pack(padx=20,pady=20)


    tab1 = tabview.add("🔐 Password Saver")
    tab2 = tabview.add("🔒 Encryption Tool")
    tab3 = tabview.add("ℹ️ About")

    label1 = ctk.CTkLabel(tab1, text="", font=("Arial", 30, "bold"))
    label1.pack(pady=40)
    animat_label(label1, "ID/PASS - SAVER 🔐")
    

    bt4 = ctk.CTkButton(tab1, text="START 🌟", width=120, height=64,command=pass_saver,corner_radius=100)
    bt4.pack(pady=20)


    label2 = ctk.CTkLabel(tab2, text="", font=("Arial", 30, "bold"))
    label2.pack(pady=40)
    animat_label(label2, "ENCRYPTION TOOL 🔐")

    bt5 = ctk.CTkButton(tab2, text="START 🌟", width=120, height=64,command=cypher_pass,corner_radius=100)
    bt5.pack(pady=20)


    about_text = "Created by Dipanshu aka DIP_NYX\nVersion 1.0\nEnjoy using the tools!"
    about_label = ctk.CTkLabel(tab3, text=about_text, font=("Consolas", 14))
    about_label.pack(pady=(40, 10))

    github_label = ctk.CTkLabel(
    tab3,
    text="🔗 Visit my GitHub: github.com/dipanshunyx",
    font=("Consolas", 13),
    text_color="skyblue",
    cursor="hand2"
    )
    github_label.pack(pady=10)

    def open_github(event):
        import webbrowser
        webbrowser.open("https://github.com/dipanshunyx")

    github_label.bind("<Button-1>", open_github)


    app2.mainloop()

def _load_admin_pass() -> str:
    """Read the current admin password from disk (creates file on first run)."""
    if not os.path.exists(ADMIN_PASS_FILE):
        with open(ADMIN_PASS_FILE, "w") as fh:
            fh.write(DEFAULT_ADMIN)
        return DEFAULT_ADMIN
    with open(ADMIN_PASS_FILE, "r") as fh:
        return fh.read().strip()

def _save_admin_pass(new_pass: str) -> None:
    """Persist a new admin password."""
    with open(ADMIN_PASS_FILE, "w") as fh:
        fh.write(new_pass.strip())

def _load_admin_pass() -> str:
    if not os.path.exists(ADMIN_PASS_FILE):
        with open(ADMIN_PASS_FILE, "w") as fh:
            fh.write(DEFAULT_ADMIN)
        return DEFAULT_ADMIN
    with open(ADMIN_PASS_FILE, "r") as fh:
        return fh.read().strip()

def _save_admin_pass(new_pass: str) -> None:
    with open(ADMIN_PASS_FILE, "w") as fh:
        fh.write(new_pass.strip())
#################################################################################
def admin_panel() -> None:
    global panel
    current_pass = _load_admin_pass()  


    def _launch_control_panel() -> None:   
        panel = ctk.CTk()
        panel.title("🔧 Admin Control Panel")
        panel.geometry("460x480")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")


        saved_cnt, file_size = 0, 0
        if os.path.isfile("save-password.txt"):
            with open("save-password.txt") as fh:
                saved_cnt = fh.read().count("----------------------------------------")
            file_size = os.path.getsize("save-password.txt")

        dash_lbl = ctk.CTkLabel(panel,
                                text=f"📊  Stored credentials: {saved_cnt}\n"
                                     f"💽  save-password.txt: {file_size} bytes",
                                font=("Consolas", 14), justify="left")
        dash_lbl.pack(pady=(25, 15))

        cp_frame = ctk.CTkFrame(panel, corner_radius=10)
        cp_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(cp_frame, text="Change master password",
                     font=("Ubuntu", 15)).pack(pady=(10, 5))

        new_pwd = ctk.CTkEntry(cp_frame, width=260, placeholder_text="New password",
                               show="*")
        confirm = ctk.CTkEntry(cp_frame, width=260, placeholder_text="Confirm password",
                               show="*")
        new_pwd.pack(pady=5)
        confirm.pack(pady=5)

        def _do_change() -> None:
            if not new_pwd.get() or not confirm.get():
                mb.showwarning("Missing", "Fill in both fields.")
            elif new_pwd.get() != confirm.get():
                mb.showerror("Mismatch", "Passwords don’t match.")
            else:
                _save_admin_pass(new_pwd.get())
                mb.showinfo("Success", "Master password updated ✅")
                nonlocal current_pass
                current_pass = new_pwd.get()
                new_pwd.delete(0, "end"); confirm.delete(0, "end")

        ctk.CTkButton(cp_frame, text="Update Password",
                      command=_do_change, width=160,
                      corner_radius=100).pack(pady=(5, 10))

        dz_frame = ctk.CTkFrame(panel, corner_radius=10)
        dz_frame.pack(pady=15, padx=20, fill="x")

        ctk.CTkLabel(dz_frame, text="Danger zone",
                     font=("Ubuntu", 15)).pack(pady=(10, 5))

        def _wipe_all() -> None:
            if mb.askyesno("Confirm", "Delete ALL saved passwords?"):
                delete_saved_passwords()
                mb.showinfo("Deleted", "All credentials removed.")
                dash_lbl.configure(text="📊  Stored credentials: 0\n"
                                        "💽  save-password.txt: 0 bytes")

        ctk.CTkButton(dz_frame, text="🗑️  Delete all passwords",
                      fg_color="#A30000", hover_color="#750000",
                      command=_wipe_all, width=200,
                      corner_radius=100).pack(pady=(5, 10))

        ctk.CTkButton(panel, text="Close", width=120,
                      command=panel.destroy,
                      corner_radius=100).pack(pady=10)

        panel.mainloop()
    verify = ctk.CTk()
    verify.title("Admin Login")
    verify.geometry("350x160")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    ctk.CTkLabel(verify, text="Enter admin password:",
                 font=("Ubuntu", 16)).pack(pady=(20, 10))
    pwd_entry = ctk.CTkEntry(verify, width=280, placeholder_text="********",
                             show="*")
    pwd_entry.pack(pady=5)

    def _check_pwd() -> None:              
        if pwd_entry.get() == current_pass:
            verify.destroy()
            _launch_control_panel()
        else:
            mb.showerror("Access denied", "Wrong password — try again!")

    ctk.CTkButton(verify, text="Continue", width=120,
                  command=_check_pwd, corner_radius=100).pack(pady=15)
    verify.mainloop()
def cypher_pass() -> None:
    """
    Gate‑keeper for the Cypher tool.
    Shows a tiny dialog asking for the master password; if it matches,
    launches `cypher_nyx()`, otherwise shows an error.
    """
    current_pass = _load_admin_pass()      # already defined above

    verify = ctk.CTk()
    verify.title("Cypher Login")
    verify.geometry("350x160")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    ctk.CTkLabel(
        verify,
        text="Enter master password to use the Cypher tool:",
        font=("Ubuntu", 16)
    ).pack(pady=(20, 10))

    pwd_entry = ctk.CTkEntry(
        verify,
        width=280,
        placeholder_text="********",
        show="*"
    )
    pwd_entry.pack(pady=5)

    def _check_pwd() -> None:
        if pwd_entry.get() == current_pass:
            verify.destroy()
            cypher_nyx()                  # open the Encode/Decode UI
        else:
            mb.showerror("Access denied", "Wrong password — try again!")

    ctk.CTkButton(
        verify,
        text="Continue",
        width=120,
        command=_check_pwd,
        corner_radius=100
    ).pack(pady=15)

    verify.mainloop()


login()    
####################################################################################################

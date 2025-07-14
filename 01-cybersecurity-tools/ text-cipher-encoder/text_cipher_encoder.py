import time 
import sys


def_char = [' ', 'Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh', 'Ii','Jj', 'Kk', 'Ll', 'Mm', 'Nn', 'Oo', 'Pp', 'Qq', 'Rr', 'Ss','Tt', 'Uu', 'Vv', 'Ww', 'Xx', 'Yy', 'Zz']
mainx = def_char.copy()


encoded_history = []
decoded_history = []

def encodenyx():
    strnyx = input("Enter the text to encode =>")
    result=[]
    for char in strnyx:
        for id,pair in enumerate(mainx):
            if char in pair :
                if  char == ' ':
                    result.append('¤')
                elif char.isupper():
                    result.append(f"⊙{id +73 }") 
                elif char.islower():
                    result.append(f'§{id+ 73}')
                break    
    encoded = '#'.join(result)
    encoded = encoded[::-1]
    encoded_history.append(encoded)
    animated_reveal(encoded)
    return encoded     

def animated_reveal(encoded):
    output = ""
    for i, char in enumerate(encoded):
        output += char
        if i < len(encoded) - 1:
            print(f"\r{output}*", end='', flush=True)
        else:
            print(f"\r{output}", end='', flush=True)
        time.sleep(0.05)
    print()           

def decodenyx():
    stnyx = input("Enter the text to Decode => ")
    stnyx = stnyx[::-1] 
    result = stnyx.split("#")
    empnyx = ""
    for char in result:
        if char == "¤":
            empnyx += " "
        elif char.startswith('⊙') or char.startswith('§'):
            case = char[0]
            index = int(char[1:]) - 73
            if 0 <= index < len(mainx):
                char = mainx[index][0] if case == "⊙" else mainx[index][1]
                empnyx += char                
    decoded_history.append(empnyx)
    animated_reveals(empnyx)
    return empnyx

def animated_reveals(empnyx):
    output = ""
    for i in empnyx:
        output += i
        print(f"\r{output}",end='',flush=True)
        time.sleep(0.05)
    print()     

def admin_panel():
    z = 'Welcome to Admin Panel'
    f = 'Enter admin password:'
    output = ""
    for i in z:
        output+=i
        print(f"\r{output}",end='',flush=True)
        time.sleep(0.05)
    print()
    for i in range(3):
        for dots in ['.','..','...']:
            print(f"\r ADMIN(Dipanshunyx) loading{dots}",end ='',flush=True)
            time.sleep(0.3)
    print("\r" +'  '*30,end ='')
    print()
    print() 
    for i in f:
        output+=i
        print(f"\r{output}",end='',flush=True)
        time.sleep(0.05)
    password = input("")
    if password != "dipanshunyx":
        print("❌ Access Denied!")
        return

    while True:
        print("\n--- Admin Menu ---")
        print("1. View Encode History")
        print("2. View Decode History")
        print("3. Clear History")
        print("4. Help / Cipher Info")
        print("5. Back to Main Menu")
        print("---------------------")
        choice = input("Choose option: ").strip()
        
        if choice == "1":
            print("\n🧾 Encoded History:")
            for i, item in enumerate(encoded_history, 1):
                print(f"{i}. {item}")
        elif choice == "2":
            print("\n🔓 Decoded History:")
            for i, item in enumerate(decoded_history, 1):
                print(f"{i}. {item}")
        elif choice == "3":
            encoded_history.clear()
            decoded_history.clear()
            print("✅ History cleared.")
        elif choice == "4":
            print("""
This is a custom text cipher tool.
- '⊙' represents uppercase letters.
- '§' represents lowercase letters.
- '¤' represents space.
- '#' separates characters.
Text is reversed before output for to make it mroe encrypt.
                  
            """)
        elif choice == "5":
            break
        else:
            print("❌ Invalid option.")

def main():
    while True:
        print("\n1. Encode")
        print("2. Decode")
        print("3. Exit")
        print("4. Admin Panel")
        choice = input("Choose (1/2/3/4): ").strip().lower()
        if choice == "1" or choice == "encode":
            encodenyx()
            time.sleep(1)
        elif choice == "2" or choice == "decode":
            decodenyx()
            time.sleep(1)
        elif choice == "3" or choice == "exit":
            k = 'Goodbye!'
            output = ''
            for i in k:
                output+= i
                print(f"\r{output}*",end='',flush=True)
                time.sleep(0.3)
            time.sleep(1)
            break
        elif choice == "4" or choice == "admin":
            admin_panel()
        else:
            print("❌ Invalid choice.")

main()

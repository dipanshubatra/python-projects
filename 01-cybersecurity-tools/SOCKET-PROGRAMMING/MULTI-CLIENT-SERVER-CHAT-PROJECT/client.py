import socket as s
import threading

def recive():
    while True:
        try:
            msg = client.recv(1024).decode()
            print('\r' + msg + '\nYou: ', end="")
        except:
            print("[error] disconnected")
            break

client = s.socket(s.AF_INET, s.SOCK_STREAM)
client.connect(("127.0.0.1", 9999))

print(client.recv(1024).decode().strip(), end='')
name = input("")
client.send(name.encode())

thread = threading.Thread(target=recive, daemon=True)
thread.start()

while True:
    mesg = input("You: ")
    if mesg.lower() == 'exit':
        client.send(f'{name} has left the chat'.encode())
        break
    client.send(f'{name} :- {mesg}'.encode())  

client.close()

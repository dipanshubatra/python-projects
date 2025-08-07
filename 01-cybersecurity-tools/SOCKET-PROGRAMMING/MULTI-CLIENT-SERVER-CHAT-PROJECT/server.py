import socket as s 
import threading

clients = []

def handle_client(conn, addr):
    msg1 = 'enter your name '
    conn.send(msg1.encode())
    name = conn.recv(1024).decode().strip()
    clients.append((conn, name))

    welcome = f'{name} became online now '
    broadcast(conn, welcome)

    while True:
        try:
            mseg = conn.recv(1024).decode()
            print(mseg)
            mseg1 = f'{name} :- {mseg}'
            broadcast(conn, mseg1)
        except:
            break

    bye = f'[-] {name} disconnected '
    broadcast(conn, bye)
    clients.remove((conn, name))
    conn.close()

def broadcast(send_conn, send_msg):
    for client in clients:
        try:
            if client[0] != send_conn:
                client[0].send(send_msg.encode())
        except:
            client[0].close()
            clients.remove(client)

server = s.socket(s.AF_INET, s.SOCK_STREAM)
server.bind(("127.0.0.1", 9999))
server.listen(5)
print('server is listening ,,,,,,,,,,,')
while True:
    conn, addr = server.accept()
    print(f'[+] New connection is added')
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()

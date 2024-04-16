import socket 
import threading
from math import pi

HEADER = 64
PORT = 5050
SERVER = 'localhost'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            area = float(msg)*float(msg)*pi
            area = str(round(area,3))
            print(f"[{addr}] {area}")
            if area == str(round(float(0),3)):
                connected = False
            else:
                conn.send(area.encode(FORMAT))
                
    conn.send("Connection Closed".encode(FORMAT))
    print("Connection with client was closed")
    conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        handle_client(conn,addr)


print("[STARTING] server is starting...")
start()

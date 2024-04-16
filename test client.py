import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = 'localhost'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(radius):
    radius_message = radius.encode(FORMAT)
    radius_length = len(radius_message)
    send_length = str(radius_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(radius_message)
    area = client.recv(2048).decode(FORMAT)
    if(area == "Connection Closed"):
        print(area)
    else:
        print("The area of the circle with radius",radius,"is:",area)
        main()


def main():
    radius = 1
    while radius > 0:
        radius = float(input("Enter the radius of the circle (Enter 0 to exit): "))
        radius = str(round(radius,3))
        send(radius)
        input()
        send(radius)
        input()
        send(radius)
        radius = float(radius)
main()
    

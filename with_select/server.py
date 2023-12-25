import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ipv4, tcp

s.bind((socket.gethostname(), 1234)) # ip, port

s.listen(5) # queue of connections

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
import socket
import pickle

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ipv4, tcp

s.bind((socket.gethostname(), 1234)) # ip, port

s.listen(5) # queue of connections

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    # any object
    d = {1: "Hey", 2: "There"}
    msg = pickle.dumps(d)

    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg

    clientsocket.send(msg)

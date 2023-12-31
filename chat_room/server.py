import socket

host = "127.0.0.1" # localhost
port = 7895

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(host, port)
server.listen()

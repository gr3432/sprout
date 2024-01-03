import socket

host = "127.0.0.1"
port = 7895

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((host, port))

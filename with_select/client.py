import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ipv4, tcp

# since client runs on the same machine we can use gethostname for ip
# but usually it should be the ip of the server
s.connect((socket.gethostname(), 1234)) 

msg = s.recv(1024) # chunk of data, returns a byte stream
print(msg.decode("utf-8"))
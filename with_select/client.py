import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ipv4, tcp

# since client runs on the same machine we can use gethostname for ip
# but usually it should be the ip of the server
s.connect((socket.gethostname(), 1234)) 

full_msg = ''
while True:
    msg = s.recv(8) # chunk of data, returns a byte stream
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")

print(full_msg)
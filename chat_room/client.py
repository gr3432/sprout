import socket

host = "127.0.0.1"
port = 7895

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((host, port))

def receive():
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if message == "NICK":
                pass
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break
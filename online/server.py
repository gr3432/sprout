import socket
from _thread import start_new_thread
from player import Player
import pickle
from game import Game

server = "192.168.1.149"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for connection, Server started")

connected = set()
games = {}
idCount = 0

def threaded_client(conn, p, gameId):
    pass

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    idCount += 1
    gameId = (idCount - 1) // 2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating new game...")
    else:
        games[gameId].ready = True
        p = 1

    # start_new_thread(threaded_client, (conn, currentPlayer))

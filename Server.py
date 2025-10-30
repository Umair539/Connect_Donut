import socket
import threading
from Game import Game
import pickle

server = "192.168.0.141"
port = 54187

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
    print(s.getsockname()[1])
except socket.error as e:
    print(str(e))

s.listen()
print("Waiting for a connection, Server Started")


def step(data, game):
    if data > 0:
        game.col = data - 1
        game.add()
        game.check()
        if game.w == 0:
            game.nextp()
    return game


def threaded_client(conn, IDx):
    game = games[IDx]
    ids = [id for id, g in games.items() if g is game]
    Player = int(ids.index(IDx) + 1)
    print(IDx, Player)

    try:
        conn.sendall(pickle.dumps(game))
        conn.sendall(pickle.dumps(Player))
    except Exception as e:
        print("Error sending initial data:", e)
        conn.close()
        return

    while True:
        try:
            data = pickle.loads(conn.recv(2048))

            if not data:
                print("Disconnected")
                break

            if data == -3:
                print(str(game.w) + " player " + str(Player))
                if game.w != 0:
                    print(f"Player {Player} requested restart")
                    game.restart()
                reply = game

            elif data > -3:
                reply = step(data, game)

            else:
                reply = game  # return current state

            print(str(game.w) + " " + str(game.p))
            conn.sendall(pickle.dumps(reply))

        except Exception as e:
            print("Error:", e)
            break

    print("Lost connection to ID: " + str(IDx))
    conn.close()
    Connected.remove(IDx)


games = {}

Connected = []
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    IDx = pickle.loads(conn.recv(2048))
    print(Connected)
    Connected.append(IDx)

    if IDx not in games:
        if len(games) % 2 == 1:
            last_key = list(games.keys())[-1]
            games[IDx] = games[last_key]
        else:
            games[IDx] = Game()

    client_thread = threading.Thread(target=threaded_client, args=(conn, IDx))
    client_thread.start()

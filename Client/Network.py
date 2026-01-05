import socket
import pickle


class Network:
    def __init__(self, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.141"
        self.port = port
        self.addr = (self.server, self.port)

    def connect(self, ID):
        try:
            self.client.connect(self.addr)
            self.client.send(pickle.dumps(ID))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)
            raise

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

    def receive(self):
        try:
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)
            raise

    def close(self):
        self.client.close()

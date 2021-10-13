from lab6.server.server import IP_ADDRESS, PORT, BUFFER_SIZE
import socket


class ClientController:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((IP_ADDRESS, PORT))

    def get_result(self):
        return self.socket.recv(BUFFER_SIZE).decode()

    def send_expression(self, expression):
        self.socket.sendall(str.encode(expression))
        return self.get_result()

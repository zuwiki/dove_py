import socket

class Transport(object):

    address = None
    socket = None
    handler = None

    MAX_CONNECTIONS = 1

    def __init__(self, address, handler):
        self.address = address
        self.handler = handler

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(address)

    def serve_forever(self):
        self.socket.listen(self.MAX_CONNECTIONS)

        while True:
            request = self.socket.accept()
            self.SocketHandler(request).run()

class SocketTransport(threading.Thread):
    def __init__(self):
        pass

if __name__ == '__main__':

    from dove.handlers import SocketHandler

    t = Transport(address, Handler)
    t.serve_forever()

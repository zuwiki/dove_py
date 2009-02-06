import socket

from dove.handler import Handler

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
            # returns (socket, (client_ip, client_port))
            request = self.socket.accept()
            self.handler(request).start()

class SocketTransport(threading.Thread):

    def __init__(self, request):
        self.request = request
        threading.Thread.__init__(self)

    def run(self):
        sockfile = self.request[0].makefile()

        json = ""
        for line in sockfile:
            if line:
                json += line

        print json


if __name__ == '__main__':

    t = Transport(address, SocketTransport)
    t.serve_forever()

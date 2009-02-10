import socket
import threading

from handler import Handler

class Transport(object):

    address = None
    socket = None
    handler = None

    MAX_CONNECTIONS = 5

    def __init__(self, address, handler):
        self.address = address
        self.handler = handler

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP stream socket
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Re-use this address
        self.socket.bind(address)

    def serve_forever(self):
        self.socket.listen(self.MAX_CONNECTIONS)

        while True:
            # returns (socket, (client_ip, client_port))
            request = self.socket.accept()
            self.handler(request).start()

class SocketTransport(threading.Thread):

    def __init__(self, request, handler):
        self.request = request
        self.handler = handler

        threading.Thread.__init__(self)

    def run(self):
        sockfile = self.request[0].makefile()

        json = self.get_input()
        result = Handler(json)
        
        # TODO: Accept multiple results
        self.request[0].send(result)
        self.request[0].close()

    def get_input(self):
        json = ""
        for line in sockfile:
            if line == '\r\n':
                break

            json += line

        return json.rstrip('\r\n')

if __name__ == '__main__':
    address = ('0.0.0.0', 4644)

    t = Transport(address, SocketTransport)
    t.serve_forever()

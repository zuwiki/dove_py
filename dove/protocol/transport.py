import socket
import threading

from handler import Handler

class Transport(object):
    '''
    Provides a layer to communicate to the outside world. Currently it's just a socket interface
    but soon it'll be an HTTP interface as well.
    '''

    MAX_CONNECTIONS = 5

    address = None
    handler = None

    socket = None

    def __init__(self, address, handler):
        '''
        Saves the binding address and request handler and initializes the listening socket.
        '''
        self.address = address
        self.handler = handler

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP stream socket
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Re-use this address
        self.socket.bind(address)

    def serve_forever(self):
        '''
        Starts listening and loops forever sending any requests to the request handler.
        '''
        self.socket.listen(self.MAX_CONNECTIONS)
        
        try:
            while True:
                # returns (socket, (client_ip, client_port))
                request = self.socket.accept()
                self.handler(request).start()

        except KeyboardInterrupt:
            print 'Exiting. Waiting for all client connections to close.'


class SocketHandler(threading.Thread):
    '''
    Takes a socket request and delegates requests/responses to the base handler.
    '''

    def __init__(self, request, handler):
        self.request = request
        self.handler = handler

        threading.Thread.__init__(self)

    def run(self):
        sockfile = self.request[0].makefile()

        json = self.get_input()
        result = Handler(json)
        
        # TODO: Accept multiple results
        # BUG: 543
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

    t = Transport(address, SocketHandler)
    t.serve_forever()

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
    debug = False

    def __init__(self, address, handler):
        '''
        Saves the binding address and request handler and initializes the listening socket.
        '''
        self.address = address
        self.handler = handler

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP stream socket
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Re-use this address
        self.socket.bind(address)
    
    # TODO: Bug 8d2
    def log(self, message):
        if (self.debug):
            print '>> ' + message

    def serve_forever(self):
        '''
        Starts listening and loops forever sending any requests to the request handler.
        '''
        self.socket.listen(self.MAX_CONNECTIONS)
        
        self.log('Listening on %s:%i' % self.address)

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

    def __init__(self, request):
        self.request = request
        self.handler = Handler()
        self.running = False

        threading.Thread.__init__(self)

    def run(self):
        self.sockfile = self.request[0].makefile()
        
        self.running = True
        while self.running:
            json = self.get_input()

            response = self.handler.handle(json, self)
            self.request[0].send("%s"%response)
        
        self.request[0].close()

    def get_input(self):
        json = ""
        for line in self.sockfile:
            if line.startswith('\r\n'):
                break

            json += line

        return json.rstrip('\r\n')

from SocketServer import TCPServer, StreamRequestHandler, ForkingMixIn, ThreadingMixIn

class ForkServer(ForkingMixIn, TCPServer):
    pass

class ThreadServer(ThreadingMixIn, TCPServer):
    pass

class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print 'Got connection from', addr
        self.wfile.write('Thank you for connecting')

#server = TCPServer(('', 1234), Handler)
#server = ForkServer(('', 1234), Handler)
server = ThreadServer(('', 1234), Handler)
server.serve_forever()

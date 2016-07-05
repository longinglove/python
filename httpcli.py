import asyncore,socket

class HTTPClient(asyncore.dispatcher):
    def __init__(self, host, path):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, 80))
        self.buffer='GET %s HTTP/1.0\r\n\r\n'%path

    def handler_connect(self):
        pass

    def handler_close(self):
        self.close()

    def handler_read(self):
        print self.recv(8192)

    def writable(self):
        return (len(self.buffer)>0)

    def handler_write(self):
        sent = self.send(self.buffer)
        self.buffer = self.buffer[sent:]

client = HTTPClient('www.python.org','/')
asyncore.loop()

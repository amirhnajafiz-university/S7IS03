# network imports
import socket



# Server is for creating a listener which can accept clients.
class Server:
    # constructor
    def __init__(self, address):
        # opening a socket
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.__start__(address)

    # start method will bind and start our server
    def __start__(self, address): 
        self.__sock.bind(address)
        self.__sock.listen(0)

        print(f"Server start listening on {address[0]}:{address[1]} ...")
    
    # handle method handles clients
    def handle(self):
        while True:
            connection, address = self.__sock.accept()

            print(f"==> {address[0]} connected on port {address[1]}")



# start server
if __name__ == "__main__":
    # creating a server instance
    server = Server(("0.0.0.0", 3232))

    # start accepting clients
    server.handle()
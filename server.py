# network imports
import socket
# system imports
import signal
import threading
# protocol imports
import json
from pprint import pprint

# socket imports
from network import read, write



# Server is for creating a listener which can accept clients.
class Server:
    # constructor
    def __init__(self, address):
        # opening a socket
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # for keeping the connections
        self.__sockets = []

        self.__start(address)

    # start method will bind and start our server
    def __start(self, address): 
        self.__sock.bind(address)
        self.__sock.listen(0)

        print(f"Server start listening on {address[0]}:{address[1]} ...")
    
    # handle method handles clients
    def handle(self):
        while True:
            connection, address = self.__sock.accept()

            print(f"==> {address[0]} connected on port {address[1]}")

            self.__sockets.append(connection)
    
    # get info reads user data from sockets
    def __get_info(self, index):
        sock = self.__sockets[index]
        info = json.loads(read(sock).decode('utf-8'))
        pprint(info)
    
    # close socket closes a client connection
    def __close_socket(self, index):
        self.__sockets[index].close()
        self.__sockets.pop(index)
    
    # print sockets generates sockets information for user
    def __print_sockets(self):
        print()

        sockets = [f"{s.getpeername()[0]}:{s.getpeername()[1]}" for s in self.__sockets]
        if len(sockets) < 1:
            return
        
        print("Enter [sysinfo/close] [index] to get peer system information or close connection:")
        for i, p in enumerate(sockets):
            print(f"\t[{i + 1}] {p}")
        
        print()
    
    # close server method shutdowns the server socket
    def close_server(self):
        self.__sock.close()

        exit(0)



# start server
if __name__ == "__main__":
    # creating a server instance
    server = Server(("0.0.0.0", 3232))

    # if kill signal sent, close server
    signal.signal(signal.SIGINT, server.close_server)

    # start accepting clients
    server.handle()
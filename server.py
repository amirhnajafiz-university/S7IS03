import socket
from pprint import pprint

from network import write, read



class Server:
    def __init__(self, address):
        self.__sockets = []
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.__start__(address)

    def __start__(self, address):    
        self.__sock.bind(address)
        self.__sock.listen(0)

        print(f"Server start listening on {address[0]}:{address[1]} ...")
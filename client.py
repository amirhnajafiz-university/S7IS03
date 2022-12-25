# network imports
import socket



# constant variables
HOST = 'localhost'
PORT = 3232



# start client
if __name__ == '__main__':
    # creating a new socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to server
    sock.connect((HOST, PORT))

    print(f"connected to {HOSTNAME} on port {PORTNUMBER}")

    sock.close()
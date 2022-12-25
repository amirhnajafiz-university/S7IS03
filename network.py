import struct



# write function takes a socket and a data which is an array of bytes
# then it will send data over that socket.
def write(sock, data: bytes):
    sock.sendall((struct.pack('!I', len(data)) + data))


# read function takes a socket and reads data from our socket into an
# array of bytes.
def read(sock):
    pass
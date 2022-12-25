import struct



# constant variables
TOKEN = '!I'


# write function takes a socket and a data which is an array of bytes
# then it will send data over that socket.
def write(sock, data: bytes):
    sock.sendall((struct.pack(TOKEN, len(data)) + data))


# read function takes a socket and reads data from our socket into an
# array of bytes.
def read(sock):
    # first we get the message size
    data_size = extract(sock, 4)
    if not data_size:
        return None

    # unpacking the message size
    size = struct.unpack(TOKEN, data_size)[0]

    return extract(sock, size)


# extract takes n bytes from socket or returns None if it reaches the end.
def extract(sock, number_of_bytes: int):
    # creating a buffer
    buffer = bytearray()

    # loop until you get all of data
    while len(buffer) < number_of_bytes:
        packet = sock.recv(number_of_bytes - len(buffer))
        if not packet:
            return None

        buffer.extend(packet)
    
    return buffer
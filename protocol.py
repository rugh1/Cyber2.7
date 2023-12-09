import socket

def send(connected_socket, msg):
    msg = hex(len(msg))[2:] + '!' + '!'.join(msg.split())
    connected_socket.send(msg.encode())

def recv(connected_socket):
    length = ''
    while '!' not in length:
        length += connected_socket.recv(1).decode()
    length = length[:-1]
    length = int(length, 16)
    msg = ''
    while len(msg) < length:
        msg += connected_socket.recv(1).decode()
    return msg.split('!')

if __name__ == '__main__':
    pass
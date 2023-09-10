#!/usr/bin/env python3
import socket

from common import HOST, PORT, DATA_SIZE

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"Hello server")
        data = s.recv(DATA_SIZE)

        print(data)

#!/usr/bin/env python3
import socket

from common import HOST, PORT, DATA_SIZE


def new_client(connection: socket.socket) -> None:
    with connection:
        while True:
            data = connection.recv(DATA_SIZE)
            if not data:
                break
            print(f"Received {data}")
            connection.sendall(b"Hello client")


if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, _ = s.accept()
            new_client(conn)

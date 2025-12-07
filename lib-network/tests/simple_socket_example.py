# https://stackoverflow.com/questions/71133919/python-socket-hangs-on-connect-accept
import socket
import argparse
import sys
import os
import re
import threading

PORT = 1234

def receive(port: int = PORT, buffer_size: int = 1024):
    host = ""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Address might be in a TIME_WAIT status, ignore this
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen()
    conn, addr = sock.accept()
    while True:
        data = conn.recv(buffer_size)
        print("recv", data)
        if not data:
            break
        print(data)
    
    conn.sendall(b"pong")
    conn.close()

def send(hostname: str = "127.0.0.1", destPort: int = PORT, content: str = b"test", buffer_size: int = 1024):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Address might be in a TIME_WAIT status, ignore this
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Removed bind
    sock.connect((hostname, destPort))
    sock.sendall(content)
    # shutdown might be redundant/unnecessary (tells connected host that we're done sending data)
    sock.shutdown(socket.SHUT_WR)
    while True:
        data = sock.recv(buffer_size)
        print("send: ", data)
        if len(data) == 0:
            break
    sock.close()
    
threading.Thread(target=receive,daemon=True).start()
send()
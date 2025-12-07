# https://stackoverflow.com/questions/71133919/python-socket-hangs-on-connect-accept
import socket
import argparse
import sys
import os
import re
import threading
import ssl
from time import sleep

from .gen_keys import gen_keys

def _load_verify_locations(context):
    # context.load_verify_locations('server_cert.crt')

    pass

class TcpServer(

):

    # verify a client using some shared password? gen invite links and anyone with the link can connect?
    # Probably a link.
    # uv run client.py --key=123121321
    # verify the hashed password.
    # I'd like to also verify the client cert if possible at some point.
    def __init__(self, cert_dir = None, host = '0.0.0.0'):
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        # TODO at some point enable this?
        # context.verify_mode = ssl.CERT_REQUIRED
        _load_verify_locations(context)

        # cert to share with others.

        if not cert_dir:
            cert_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'certs'))
        cert = os.path.abspath(os.path.join(cert_dir, 'public.crt'))
        key = os.path.abspath(os.path.join(cert_dir, 'private.key'))
        if not os.path.isfile(key):
            gen_keys(key, cert)
        
        context.load_cert_chain(cert, key)

        self._context = context
        self._host = host
        self._port = 9999
        self._buffer_size = 1024
                


        pass

    def start(self):
        print("start")
        host = self._host
        port = self._port
        buffer_size = self._buffer_size

        print("receive", self._host, self._port)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("created new socket")
        # Address might be in a TIME_WAIT status, ignore this
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        print("bind", (host, port))
        sock.bind((host, port))
        sock.listen()
        print("socket is listening", (host, port))
        sock = self._context.wrap_socket(sock, server_side=True)

        print("start accepting connections")
        conn, addr = sock.accept()
        while True:
            data = conn.recv(buffer_size)
            if not data:
                break
            print("received:",data)
        conn.close()

# def send(hostname: str = "127.0.0.1", destPort: int = 9999, content: str = b"test", buffer_size: int = 1024):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # Address might be in a TIME_WAIT status, ignore this
#     sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#     # Removed bind
#     sock.connect((hostname, destPort))
#     sock.sendall(content)
#     # shutdown might be redundant/unnecessary (tells connected host that we're done sending data)
#     sock.shutdown(socket.SHUT_WR)
#     while True:
#         data = sock.recv(buffer_size)
#         if len(data) == 0:
#             break
#     sock.close()
    
# threading.Thread(target=receive,daemon=True).start()
# send()
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

def _load_verify_locations(context, cert_dir):
    cert = os.path.abspath(os.path.join(cert_dir, 'public.crt'))

    context.load_verify_locations(cert)

    pass

class TcpClient(

):

    # verify a client using some shared password? gen invite links and anyone with the link can connect?
    # Probably a link.
    # uv run client.py --key=123121321
    # verify the hashed password.
    # I'd like to also verify the client cert if possible at some point.
    def __init__(self, cert_dir = None, host = '0.0.0.0'):

        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        context.verify_mode = ssl.CERT_REQUIRED

        if not cert_dir:
            cert_dir = os.path.abspath(
                os.path.join(os.path.dirname(__file__), 'certs'))
        

        _load_verify_locations(context, cert_dir)

        # cert to share with others.

        self._context = context

        self._buffer_size = 1024

        # self._host = host
        # self._port = 9999


        pass

    def send(self, content = 'ping'):

        print("send message:", content)
        sock = self._sock
        sock.sendall(content.encode('utf-8'))
        buffer_size = self._buffer_size
        # shutdown might be redundant/unnecessary (tells connected host that we're done sending data)
        sock.shutdown(socket.SHUT_WR)


        while True:
            print("awaiting response")
            # TODO response from request from client
            # list - list users
            # 
            data = sock.recv(buffer_size)
            if len(data) == 0:
                print("client received", data)
                break
        sock.close()

    def connect(self, host = '127.0.0.1', port = 9999):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Address might be in a TIME_WAIT status, ignore this
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        sock = self._context.wrap_socket(sock)

        print("client attempting connection ", (host, port))
        print("attempt 2")
        print("attempt 2")
        print("attempt 2")
        # Removed bind
        # success = sock.connect((host, port))
        sock.connect((host, port))
        # if not success:
        #     raise Exception("Failed to connect")
        self._sock = sock
        print("client connected")


    
# threading.Thread(target=receive,daemon=True).start()
# send()
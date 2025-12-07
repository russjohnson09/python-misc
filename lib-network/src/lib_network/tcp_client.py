# https://stackoverflow.com/questions/71133919/python-socket-hangs-on-connect-accept
import socket
import argparse
import sys
import os
import re
import threading
import ssl
from time import sleep
import json

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
    def __init__(self, host = '0.0.0.0', port = 9999, enable_ssl = True, cert_dir = None,):

        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        context.verify_mode = ssl.CERT_REQUIRED

        if not cert_dir:
            cert_dir = os.path.abspath(
                os.path.join(os.path.dirname(__file__), 'certs'))
        

        _load_verify_locations(context, cert_dir)

        # cert to share with others.

        self._host = host
        self._port = port
        self._context = context
        self._enable_ssl = enable_ssl

        self._buffer_size = 1024


        pass

    def close(self):
        sock = self._sock
        sock.close()

    def send(self, content: dict):

        print("send message:", content)
        sock = self._sock
        sock.sendall(json.dumps(content).encode('utf-8'))

        # sock.shutdown(socket.SHUT_WR)

        buffer_size = self._buffer_size
        # shutdown might be redundant/unnecessary (tells connected host that we're done sending data)

        data = sock.recv(buffer_size)

        print("client received response", data)
        # sock.close()
        return json.loads(data)

    def connect(self, host = '127.0.0.1', port = 9999):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Address might be in a TIME_WAIT status, ignore this
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        if self._enable_ssl:
            sock = self._context.wrap_socket(sock)

        print("client attempting connection ", (host, port))
        # Removed bind
        # success = sock.connect((host, port))
        sock.connect((host, port))
        # if not success:
        #     raise Exception("Failed to connect")
        self._sock = sock
        print("client connected")


    
# threading.Thread(target=receive,daemon=True).start()
# send()
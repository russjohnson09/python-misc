# https://stackoverflow.com/questions/71133919/python-socket-hangs-on-connect-accept
import socket
import argparse
import sys
import os
import re
import threading

from .gen_keys import gen_keys

def _load_verify_locations():
    cert = os.path.abspath(cert_dir, 'public.crt')

    context.load_verify_locations(cert)

    pass

class TcpClient(

):

    # verify a client using some shared password? gen invite links and anyone with the link can connect?
    # Probably a link.
    # uv run client.py --key=123121321
    # verify the hashed password.
    # I'd like to also verify the client cert if possible at some point.
    def __init__(self, cert_dir = None):
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        # TODO at some point enable this?
        # context.verify_mode = ssl.CERT_REQUIRED

        if not cert_location:
            cert_dir = os.path.abspath(os.path.dirname(__file__), 'certs')

        _load_verify_locations(context, cert_dir)

        # cert to share with others.

        self._context = context

        pass

    def send(hostname: str = "127.0.0.1", destPort: int = 9999, content: str = b"test", buffer_size: int = 1024):
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
            if len(data) == 0:
                break
        sock.close()
    
# threading.Thread(target=receive,daemon=True).start()
# send()
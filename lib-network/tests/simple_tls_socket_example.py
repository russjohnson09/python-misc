# https://stackoverflow.com/questions/71133919/python-socket-hangs-on-connect-accept
import socket
import argparse
import sys
import os
import re
import threading
import ssl
from time import sleep

# I think for myself, the setup I want is my computer as the host
# My computer will also have a client connection to this host
# Another person I'm playing chess with will have their own client connection.
# The server just relays messages.

# A simple IM might be a good thing to test with.

# im.ihateiceforfree.com
# This is the host but it just points to my machine.

def _load_verify_locations(context):
    context.load_verify_locations('server_cert.crt')
    context.load_verify_locations('client_cert.crt')

def receive(port: int = 9999, buffer_size: int = 1024):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

    context.verify_mode = ssl.CERT_REQUIRED
    # context.load_verify_locations('selfsigned.crt', 'client_cert.crt')'

    _load_verify_locations(context)

    context.load_cert_chain('selfsigned.crt', 
    'private.key')

    host = ""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Address might be in a TIME_WAIT status, ignore this
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen()

    sock = context.wrap_socket(sock, server_side=True)

    conn, addr = sock.accept()
    while True:
        data = conn.recv(buffer_size)
        if not data:
            break
        print("received:",data)
    conn.close()

def send(hostname: str = "127.0.0.1", destPort: int = 9999, content: str = b"test", buffer_size: int = 1024):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Address might be in a TIME_WAIT status, ignore this
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain('client_cert.crt', 'client_key.key')

    #https://stackoverflow.com/questions/61307557/self-signed-certificate-with-python-ssl-socket
    context.load_verify_locations('selfsigned.crt')
    context.verify_mode = ssl.CERT_REQUIRED


    # context.check_hostname = True

    sock = context.wrap_socket(sock)

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
    
threading.Thread(target=receive,daemon=True).start()
threading.Thread(target=send,daemon=True).start()

sleep(1)
exit(0)
# send()


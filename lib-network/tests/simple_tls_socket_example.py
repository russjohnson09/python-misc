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

# I think for myself, the setup I want is my computer as the host
# My computer will also have a client connection to this host
# Another person I'm playing chess with will have their own client connection.
# The server just relays messages.

# A simple IM might be a good thing to test with.

# im.ihateiceforfree.com
# This is the host but it just points to my machine.
PORT = 1234

def _load_verify_locations(context):
    context.load_verify_locations('server_cert.crt')
    context.load_verify_locations('client_cert.crt')

def receive(port: int = PORT, buffer_size: int = 1024):
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
        # assume the buffer size is large enough for the entire message

        data = conn.recv(buffer_size)
        print("received:",data)
        msg = json.loads(data)
        print("received message:", msg)
        break
        # if not data:
            # break
        # print("received:",data)

    conn.sendall(json.dumps({"msg": "pong"}).encode('utf-8'))

    sleep(1)
    conn.sendall(json.dumps({"type": "healthcheck"}).encode('utf-8'))

    # conn.close()

def send(hostname: str = "127.0.0.1", destPort: int = PORT, content: str = b"test", buffer_size: int = 1024):
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
    sock.sendall(json.dumps({"msg": "ping"}).encode('utf-8'))
    # shutdown might be redundant/unnecessary (tells connected host that we're done sending data)
    


    # sock.sendall(b'')
    # print("shutdown", socket.SHUT_WR)
    # sock.shutdown(socket.SHUT_WR)

    # wait on next message from server
    data = sock.recv(buffer_size)
    print("client:", data)
    msg = json.loads(data)

    print("client received message:", msg)

    print("client waiting for next packet")
    data = sock.recv(buffer_size)
    msg = json.loads(data)
    print("client received message:", msg)

    # print("close socket")
    # sock.close()
    
threading.Thread(target=receive,daemon=True).start()
threading.Thread(target=send,daemon=True).start()

sleep(5)
exit(0)
# send()


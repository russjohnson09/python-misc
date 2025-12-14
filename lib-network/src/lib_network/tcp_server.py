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


enable_ssl = True

class TcpServer(

):

    _messages = []

    # verify a client using some shared password? gen invite links and anyone with the link can connect?
    # Probably a link.
    # uv run client.py --key=123121321
    # verify the hashed password.
    # I'd like to also verify the client cert if possible at some point.
    def __init__(self, host = '0.0.0.0', port = 9999, cert_dir = None):
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)


        self._enable_ssl = enable_ssl


        if not cert_dir:
            cert_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'certs'))
        cert = os.path.abspath(os.path.join(cert_dir, 'public.crt'))
        key = os.path.abspath(os.path.join(cert_dir, 'private.key'))
        if not os.path.isfile(key):
            gen_keys(key, cert)
        
        context.load_cert_chain(cert, key)

        self._context = context
        self._host = host
        self._port = port
        self._buffer_size = 1024
        pass

    def _connection_loop(self, conn):

        sock = self._sock
        buffer_size = self._buffer_size

        data = b''
        while True:
            # data = b''
            data_chunk = conn.recv(buffer_size)
            print("server received chunk:", data_chunk)
            if not data_chunk: # client closed its connection
                return False
            data += data_chunk
            if b'\n' in data_chunk:
                break
        
        print("server received:", data)

        payload = json.loads(data)
        print("server received payload:", payload)

        if payload.get('msg') == 'close':
            return False
        
        if payload.get('type') == 'get_messages':
            conn.sendall((json.dumps({"type": "get_messages","messages": self._messages}) + "\n").encode('utf-8'))

            return True
        if payload.get('type') == 'im':
            self._messages.append(payload.get('msg'))
            conn.sendall((json.dumps({"type": "get_messages","messages": self._messages}) + "\n").encode('utf-8'))

            return True

        print("server send", (json.dumps({"msg": "pong"}) + "\n"))
        conn.sendall((json.dumps({"msg": "pong"}) + "\n").encode('utf-8'))
        return True
    
    def _accept_connection(self):
        sock = self._sock
        while True:
            # thread accept connection to allow multiple clients
            # update the fetching of data from a client to look for newline
            conn, addr = sock.accept()

            print("server accepted connection from ", addr)

            # TODO 
            while True:
                try:
                    if not self._connection_loop(conn):
                        conn.close()
                        break
                except Exception as e:
                    pass

    def start(self):
        print("start")
        host = self._host
        port = self._port

        print("receive", self._host, self._port)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("created new socket")
        # Address might be in a TIME_WAIT status, ignore this
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        print("bind", (host, port))
        sock.bind((host, port))
        sock.listen()
        print("socket is listening", (host, port))
        if self._enable_ssl:
            sock = self._context.wrap_socket(sock, server_side=True)
        self._sock = sock
        print("server accepting connections")

        i = 0
        # require multiple threads for each client connection
        while i < 3:
            i += 1
            threading.Thread(
                target=self._accept_connection,
                args=()
                # target=tcp_server.receive
                ,daemon=True
                # https://docs.python.org/3/library/threading.html
                # A thread can be flagged as a “daemon thread”. The significance of this flag is that the entire Python program exits when only daemon threads are left. The initial value is inherited from the creating thread. The flag can be set through the daemon property or the daemon constructor argument.

                ).start()
        # threading.Thread(
        #     target=self._accept_connection,
        #     args=()
        #     # target=tcp_server.receive
        #     ,daemon=True
        #     # https://docs.python.org/3/library/threading.html
        #     # A thread can be flagged as a “daemon thread”. The significance of this flag is that the entire Python program exits when only daemon threads are left. The initial value is inherited from the creating thread. The flag can be set through the daemon property or the daemon constructor argument.

        #     ).start()
        # threading.Thread(
        #     target=self._accept_connection,
        #     args=()
        #     # target=tcp_server.receive
        #     ,daemon=True
        #     # https://docs.python.org/3/library/threading.html
        #     # A thread can be flagged as a “daemon thread”. The significance of this flag is that the entire Python program exits when only daemon threads are left. The initial value is inherited from the creating thread. The flag can be set through the daemon property or the daemon constructor argument.

        #     ).start()
        self._accept_connection()



        return

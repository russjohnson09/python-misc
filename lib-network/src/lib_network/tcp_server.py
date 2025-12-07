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
import traceback

from .utils import receive_data_json

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

    def _receive_data(self, conn):
        sock = self._sock
        buffer_size = self._buffer_size
        data = b''
        while True:
            # data = b''
            # change this to base64 encoded and wait on a newline
            data_chunk = conn.recv(buffer_size)
            data += data_chunk

            if b'\x00' in data_chunk: # has null terminating byte
                break
        return data
    
    def send(self, conn, json_body: dict):
        print("send", json_body)
        # return
        conn.sendall(f"{json.dumps(json_body)}\n".encode('utf-8'))


    def _connection_loop(self, conn):

        # data = self._receive_data(conn)
        # print("server received:",data)

        payload = receive_data_json(conn) # json.loads(data)
        print("tcp_server received:", payload)

        if payload.get('type') == 'im':
            self._messages.append(payload.get('msg'))
            self.send(conn, {"type": "get_messages", "msg": self._messages})
            return True
        if payload.get('type') == 'get_messages':
            self.send(conn, {"type": "get_messages", "msg": self._messages})
            return True

        if payload.get('msg') == 'close':
            return False
        self.send(conn, {"msg": "pong"})
        return True

    def _next_connection(self):
        try:

            sock = self._sock
            conn, addr = sock.accept()

            # TODO 
            while True:
                # self._connection_loop(conn)
                if not self._connection_loop(conn):
                    conn.close()
                    return # done with loop
                conn.close()
        except Exception as e:
            # print("failed", e)
            # print(traceback.format_exc())

            return
    def start(self):
        try:

            print("start")
            host = self._host
            port = self._port

            print("receive", self._host, self._port)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:


                # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                print("created new socket")
                # Address might be in a TIME_WAIT status, ignore this
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

                print("bind", (host, port))
                sock.bind((host, port))
                sock.listen()
                print("socket is listening", (host, port))
                # if self._enable_ssl:
                #     sock = self._context.wrap_socket(sock, server_side=True)

                with self._context.wrap_socket(sock, server_side=True) as ssock:

                    self._sock = ssock
                    print("server accepting connections")

                    while True:
                        #    | ResourceWarning: unclosed <ssl.SSLSocket fd=1092, family=2, type=1, proto=0, laddr=('127.0.0.1', 9999), raddr=('127.0.0.1', 58474)>
                        # self._next_connection()
                        return
        except Exception as e:
            return
            

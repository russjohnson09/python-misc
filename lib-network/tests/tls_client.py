import socket
import ssl

from tls_server import HOST as SERVER_HOST
from tls_server import PORT as SERVER_PORT

# https://stackoverflow.com/questions/71133919/python-socket-hangs-on-connect-accept
HOST = "127.0.0.1"
PORT = 8443

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Address might be in a TIME_WAIT status, ignore this
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.load_default_certs()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client = context.wrap_socket(s)

# TODO these should be different keys and certs than the server?
# client = ssl.wrap_socket(client,
# keyfile="private.key", 
# certfile="selfsigned.crt"
# )

# Removed bind
client.connect((HOST, PORT))
client.sendall("Hello".encode("utf-8"))
# shutdown might be redundant/unnecessary (tells connected host that we're done sending data)
client.shutdown(socket.SHUT_WR)
while True:
    buffer_size = 1024
    data = client.recv(buffer_size)
    if len(data) == 0:
        break
client.close()
import socket
import ssl

hostname = 'www.python.org'
context = ssl.create_default_context()

# https://docs.python.org/3/library/ssl.html
with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version()) #TLSv1.3
import socket
import ssl

HOST = "127.0.0.1"
PORT = 60000

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# server = ssl.wrap_socket(
#     server, server_side=True, keyfile="path/to/keyfile", certfile="path/to/certfile"
# )

if __name__ == "__main__":
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('/path/to/certchain.pem', 
    '/path/to/private.key')

# https://docs.python.org/3/library/ssl.html
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
        sock.bind((HOST, PORT))
        sock.listen(5)
        with context.wrap_socket(sock, server_side=True) as ssock:
            conn, addr = ssock.accept()

    # server.bind((HOST, PORT))
    # server.listen(0)

    # while True:
    #     connection, client_address = server.accept()
    #     while True:
    #         data = connection.recv(1024)
    #         if not data:
    #             break
    #         print(f"Received: {data.decode('utf-8')}")
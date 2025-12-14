import socket
import ssl

HOST = "127.0.0.1"
PORT = 8443

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# server = ssl.wrap_socket(
#     server, server_side=True, keyfile="path/to/keyfile", certfile="path/to/certfile"
# )

if __name__ == "__main__":
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    # context.load_cert_chain('/path/to/certchain.pem', 
    # '/path/to/private.key')
    context.load_cert_chain('selfsigned.crt', 
    'private.key')
# https://docs.python.org/3/library/ssl.html
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
        print("has socket", sock)
        print(f"socket bind {(HOST,PORT)}")
        sock.bind((HOST, PORT))
        print(f"socket bound {(HOST,PORT)}")

        print("listen")
        # https://docs.python.org/3/library/socket.html#socket.socket.listen
        # sock.listen(5)
        sock.listen()
        print("listening")

        print("get secure context")
        with context.wrap_socket(sock, server_side=True) as ssock:
            print("has secure context")

            print("ssock accept")
            # https://docs.python.org/3/library/socket.html#socket.socket.accept
            conn, addr = ssock.accept()
            print(addr)
            while True:
                data = conn.recv(buffer_size)
                if not data:
                    break
                print(data)

    
    print("finished")
    exit(0)

    # server.bind((HOST, PORT))
    # server.listen(0)

    # while True:
    #     connection, client_address = server.accept()
    #     while True:
    #         data = connection.recv(1024)
    #         if not data:
    #             break
    #         print(f"Received: {data.decode('utf-8')}")
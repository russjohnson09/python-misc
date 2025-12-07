from lib_network import TcpServer, TcpClient
from time import sleep
import threading

def _start_tcp_thread(tcp_server):
    print("_start_tcp_thread")
    print(tcp_server)
    tcp_server.start()

# def _start_tcp_client(tcp_client):
#     print("_start_tcp_thread")
#     print(tcp_server)
#     tcp_server.start()

def _start_client(tcp_client):
    print("_start_client")
    tcp_client.connect()

    tcp_client.send()


def test_server():

    print(TcpServer)

    assert 1 == 1

    tcp_server = TcpServer()

    threading.Thread(
        target=_start_tcp_thread,
        args=(tcp_server,)
        # target=tcp_server.receive
        ,daemon=True
        # https://docs.python.org/3/library/threading.html
        # A thread can be flagged as a “daemon thread”. The significance of this flag is that the entire Python program exits when only daemon threads are left. The initial value is inherited from the creating thread. The flag can be set through the daemon property or the daemon constructor argument.

        ).start()

    sleep(1)
    tcp_client = TcpClient()

    threading.Thread(
        target=_start_client,
        args=(tcp_client,)
        # target=tcp_server.receive
        ,daemon=True
        # https://docs.python.org/3/library/threading.html
        # A thread can be flagged as a “daemon thread”. The significance of this flag is that the entire Python program exits when only daemon threads are left. The initial value is inherited from the creating thread. The flag can be set through the daemon property or the daemon constructor argument.

        ).start()
    

    sleep(2)

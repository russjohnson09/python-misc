from lib_network import TcpServer
from time import sleep
import threading

def _start_tcp_thread(tcp_server):
    print("_start_tcp_thread")
    print(tcp_server)
    tcp_server.start()

def test_server():

    print(TcpServer)

    assert 1 == 1

    tcp_server = TcpServer()

    threading.Thread(
        target=_start_tcp_thread,
        args=(tcp_server,)
        # target=tcp_server.receive
        ,daemon=True).start()

    sleep(2)

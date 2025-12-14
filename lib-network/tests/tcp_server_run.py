from lib_network import TcpServer, TcpClient
from time import sleep
import threading

def _start_tcp_thread(tcp_server):
    print("_start_tcp_thread")
    print(tcp_server)
    tcp_server.start()

print(TcpServer)

assert 1 == 1

tcp_server = TcpServer()

tcp_server.start()

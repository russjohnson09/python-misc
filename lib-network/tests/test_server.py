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

    response = tcp_client.send({"msg": "ping"})
    print(response)

    response = tcp_client.send({"msg": "ping"})
    print(response)
    # response = tcp_client.send({"msg": "close"})

    response = tcp_client.send({"msg": "ping", "meta": "123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"})
    print(response)

    # tcp_client.close()

    # constantly ping the server for the current state of the chess board.



#  uv run pytest -s | grep accepted
def test_server():

    print(TcpServer)

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

    
    _start_client(tcp_client)

    # threading.Thread(
    #     target=_start_client,
    #     args=(tcp_client,)
    #     # target=tcp_server.receive
    #     ,daemon=True
    #     # https://docs.python.org/3/library/threading.html
    #     # A thread can be flagged as a “daemon thread”. The significance of this flag is that the entire Python program exits when only daemon threads are left. The initial value is inherited from the creating thread. The flag can be set through the daemon property or the daemon constructor argument.

    #     ).start()
    
    # i = 0
    # while i < 10:
    #     i += 1
   
    #     tcp_client2 = TcpClient()

    #     threading.Thread(
    #         target=_start_client,
    #         args=(tcp_client2,)
    #         # target=tcp_server.receive
    #         ,daemon=True
    #         # https://docs.python.org/3/library/threading.html
    #         # A thread can be flagged as a “daemon thread”. The significance of this flag is that the entire Python program exits when only daemon threads are left. The initial value is inherited from the creating thread. The flag can be set through the daemon property or the daemon constructor argument.

    #         ).start()
    
    tcp_client2 = TcpClient()

    print('start 2')
    _start_client(tcp_client2)

    tcp_client3 = TcpClient()

    _start_client(tcp_client3)


    tcp_client.close()
    tcp_client2.close()
    tcp_client3.close()

    sleep(3)

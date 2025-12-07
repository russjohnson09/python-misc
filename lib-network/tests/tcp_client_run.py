from lib_network import TcpServer, TcpClient
from time import sleep


tcp_client = TcpClient()
tcp_client.connect()

tcp_client.send()

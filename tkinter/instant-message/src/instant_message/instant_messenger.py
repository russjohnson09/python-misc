from lib_network import TcpClient, TcpServer
import threading
# tkinter.messagebox.Message
from tkinter import messagebox
import platform
import os
import sys
import socket
import datetime
import time

import requests

# https://pypi.org/project/torch/
# https://stackoverflow.com/questions/64526139/how-does-one-get-the-model-of-the-gpu-in-python-and-save-it-as-a-string
# https://www.reddit.com/r/pygame/comments/voagr8/how_to_use_gpu_with_pygame/


# https://stackoverflow.com/questions/4842448/getting-processor-information-in-python
def _specs():
    return f"""
Platform: {platform.platform()}
System: {platform.system()}
Release: {platform.release()}
Version: {platform.version()}
Processor: {platform.processor()}
Python: {sys.version}
    """




def _ip_from_dns():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        name =s.getsockname()[0] # 192.168.1.3 This is just my local ip address
        s.close()
        return name
    except Exception as e:
        return ""

# IPv6: ? 2001:4860:7:30e::fd
# IPv4: ? 75.114.168.151
def _ip_info():
    return f"""
ip from 8.8.8.8: {_ip_from_dns()}
ip from checkip.amazonaws.com: {_public_ip()}
"""


class InstantMessenger():

    _loop_thread = None
    root = None

    start_time = time.time()
    host = '127.0.0.1'
    port = 9999

    tcp_server = None

    tcp_client = None

    public_ip = None

    def _get_public_api(self, use_cache = True):
        if not self.public_ip or not use_cache:
                
            print("request my ip")
            self.public_ip = requests.get('https://checkip.amazonaws.com').text.strip()
        return self.public_ip
        
    def _server_start(self):
        print("start in thread")
        # needs a new thread
        self.tcp_server.start()

        print("started server")
        pass

    def _loop(self):
        i = 0

        while True:
            i += 1
            # print(f"_loop {i}")
            use_cache = i % 10 != 0
            ip = self._get_public_api(use_cache)
            time.sleep(1)
            self.root.title(f"Rusty's IM {self.get_duration()}\t {ip}")

        pass


    def specs_popup(self):
        messagebox.showinfo("Specs", 
            _specs()
        )

        pass

    def ip_popup(self):
        messagebox.showinfo("Ip Info", 
            _ip_info()
        )

        pass

    def get_duration(self):
        return int(time.time() - self.start_time)

    def loop_start(self):

        self._loop_thread = threading.Thread(
            target=_loop_thread,
            args=(self,)
            # target=tcp_server.receive
            ,daemon=True
            # https://docs.python.org/3/library/threading.html
            # A thread can be flagged as a “daemon thread”. The significance of this flag is that the entire Python program exits when only daemon threads are left. The initial value is inherited from the creating thread. The flag can be set through the daemon property or the daemon constructor argument.
            )
        self._loop_thread.start()
        
        # TODO cache
        pass

    def server_start(self):
        self.tcp_server = TcpServer()
        print("server start")




        threading.Thread(
            target=_server_start,
            args=(self,)
            # target=tcp_server.receive
            ,daemon=True
            # https://docs.python.org/3/library/threading.html
            # A thread can be flagged as a “daemon thread”. The significance of this flag is that the entire Python program exits when only daemon threads are left. The initial value is inherited from the creating thread. The flag can be set through the daemon property or the daemon constructor argument.
            ).start()



    
    def client_init(self):
        self.tcp_client = TcpClient()


        print("init client")

        print("start connection")
        # tcp_client.connect()

        pass
    
    def client_connect(self):
        try:
            #     def connect(self, host = '127.0.0.1', port = 9999):

            self.tcp_client.connect(host=self.host, port=self.port)
            # ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

        except Exception as e:
            print("Failed to connect")
            # messagebox.Message()
            # https://www.geeksforgeeks.org/python/python-tkinter-messagebox-widget/
            messagebox.showerror("Failed", f"Failed to connect {self.host}:{self.port}\n{e}") 

            pass

        pass

instant_messenger = InstantMessenger()

def _server_start(im: InstantMessenger):
    print("new thread")
    im._server_start()

def _loop_thread(im: InstantMessenger):
    print("new thread")
    im._loop()
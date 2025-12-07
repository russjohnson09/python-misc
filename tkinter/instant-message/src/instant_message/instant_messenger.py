from lib_network import TcpClient, TcpServer
import threading
# tkinter.messagebox.Message
from tkinter import messagebox
import platform
import os
import sys

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

class InstantMessenger():

    host = '127.0.0.1'
    port = 9999

    tcp_server = None

    tcp_client = None

    def _server_start(self):
        print("start in thread")
        # needs a new thread
        self.tcp_server.start()

        print("started server")
        pass


    def specs_popup(self):
        messagebox.showinfo("Specs", 
        _specs()) 

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
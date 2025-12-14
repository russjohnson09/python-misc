import os

_root_repo_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../../'))
_default_asset_dir = os.path.abspath(os.path.join(_root_repo_dir, 'assets'))
os.environ['ASSET_DIR'] = _default_asset_dir

from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from lib_network import TcpServer
from instant_message import instant_messenger as im
import platform
from connect_four import ConnectFourBoard
import time
import threading



# https://www.pythonguis.com/tutorials/tkinter-basic-widgets/


# TypeError: _send_message() takes 0 positional arguments but 1 was given
def _send_message(*args):
    print("send message to server")
    # if no client then you must connect first.

    # PY_VAR0
    print(msg)
    value = msg.get()
    name_str = name.get()

    im.add_message(f"{name_str}: {value}")

    msg.set('')


    pass

def _start_server():
    if im.tcp_server:
        print("already started")
    # tcp_server = TcpServer()
    im.server_start()


def _start_connect_four_thread():
    connect_four_board = ConnectFourBoard()
    print("connect four thread")
    while True:
        if not connect_four_board.loop():
            return

def _start_connect_four():
    print("connect four")
    # TODO if I have a client connection then start up a game with that as well.
    threading.Thread(
        target=_start_connect_four_thread,
        args=()
        # target=tcp_server.receive
        ,daemon=True
        # https://docs.python.org/3/library/threading.html
        # A thread can be flagged as a “daemon thread”. The significance of this flag is that the entire Python program exits when only daemon threads are left. The initial value is inherited from the creating thread. The flag can be set through the daemon property or the daemon constructor argument.
        ).start()

def _client_connect():
    im.client_connect()



root = Tk()
root.title("Rusty's IM")

# This is truly ancient history, but menubars used to be implemented by creating a frame widget containing the menu items and packing it into the top of the window like any other widget. Hopefully, you don't have any code or documentation that still does this.



root.geometry("850x800")
mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))

im.root = root
msg = StringVar()

name = StringVar()
name_entry = ttk.Entry(mainframe, width=7, 
    textvariable=name)
name_entry.grid(column=0, row=0, sticky=(W, E))


name.set('NameHere')

def _specs_popup():
    print("specs")
#     Windows-10-10.0.19045-SP0
# Windows
# 10
# 10.0.19045
    print(platform.platform())
    print(platform.system())
    print(platform.release())
    print(platform.version())
    im.specs_popup()
    pass

def _ip_popup():
    im.ip_popup()

def _add_about_menu_items(menu_about: Menu):
    menu_about.add_command(label='Specs', command=_specs_popup)
    menu_about.add_command(label='Ip', command=_ip_popup)


def _add_about_menu(menubar: Menu):
    menu_about = Menu(menubar)
    _add_about_menu_items(menu_about)
    menubar.add_cascade(menu=menu_about, label='About')


    pass

def _add_menu(win):
    menubar = Menu(win)
    win['menu'] = menubar
    _add_about_menu(menubar)


# main_iterator = 0

def mainloop(root):
    # def iterating_func():

    #     im.loop()

    #     root.after(1000, iterating_func)

    root.after(0, im.loop_start())
    root.mainloop()
    # while True:
    #     root.update_idletasks()
    #     root.update()


def main():
    # win = Toplevel(root)


    # win = Toplevel(root)
    # win = Toplevel(mainframe)
    _add_menu(root)



    print("init client")
    im.client_init()

    # https://www.geeksforgeeks.org/python/python-tkinter-text-widget/

    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

    msg_entry = ttk.Entry(mainframe, width=7, 
        textvariable=msg)
    msg_entry.grid(column=0, row=11, sticky=(W, E))

    meters = StringVar()
    ttk.Label(mainframe, 
    textvariable=meters).grid(column=2, 
    row=2, sticky=(W, E))



    ttk.Button(mainframe, text="Connect Client", 
    command=_client_connect).grid(column=3, row=4, sticky=W)


    ttk.Button(mainframe, text="Start Server", 
    command=_start_server).grid(column=3, row=5, sticky=W)

    ttk.Button(mainframe, text="Connect Four", 
    command=_start_connect_four).grid(column=3, row=6, sticky=W)

    # ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
    # ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
    # ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)
    t = ScrolledText(mainframe,
        width = 90, 
        height = 20, 
        # wrap = "none"
    )
    # ys = ttk.Scrollbar(mainframe, 
    # orient = 'vertical', command = t.yview)
    # xs = ttk.Scrollbar(mainframe, 
    # orient = 'horizontal', command = t.xview)
    # t['yscrollcommand'] = ys.set
    # t['xscrollcommand'] = xs.set
    # t.insert('end', "Lorem ipsum...\n...\n...Lorem ipsum...\n...\n...Lorem ipsum...\n...\n...Lorem ipsum...\n...\n...Lorem ipsum...\n...\n...")

    im.scrolled_text = t
    
    t.grid(column = 0, row = 10, sticky = 'nwes')


    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    mainframe.columnconfigure(2, weight=1)
    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

    msg_entry.focus()


    root.bind("<Return>", _send_message)

    print("loop start")
    # root.mainloop()
    # https://stackoverflow.com/questions/29158220/tkinter-understanding-mainloop
    mainloop(root)




main()
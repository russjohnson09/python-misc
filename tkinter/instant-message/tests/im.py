from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from lib_network import TcpServer
from instant_message import instant_messenger as im
import platform
import os


# https://www.pythonguis.com/tutorials/tkinter-basic-widgets/


# TypeError: _send_message() takes 0 positional arguments but 1 was given
def _send_message(*args):
    print("send message to server")
    # if no client then you must connect first.

    # PY_VAR0
    print(msg)

    pass

def _start_tcp_thread(tcp_server):
    print("_start_tcp_thread")
    print(tcp_server)
    tcp_server.start()

def _start_server():
    if im.tcp_server:
        print("already started")
    # tcp_server = TcpServer()
    im.server_start()

def _client_connect():
    im.client_connect()



root = Tk()
root.title("Rusty's IM")

# This is truly ancient history, but menubars used to be implemented by creating a frame widget containing the menu items and packing it into the top of the window like any other widget. Hopefully, you don't have any code or documentation that still does this.



root.geometry("850x800")

msg = StringVar()

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

def _add_about_menu(menubar: Menu):
    menu_about = Menu(menubar)
    menu_about.add_command(label='Specs', command=_specs_popup)
    menubar.add_cascade(menu=menu_about, label='About')

    pass

def _add_menu(win):
    menubar = Menu(win)
    win['menu'] = menubar
    _add_about_menu(menubar)





def main():
    # win = Toplevel(root)
    mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))


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

    ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
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
    t.insert('end', "Lorem ipsum...\n...\n...Lorem ipsum...\n...\n...Lorem ipsum...\n...\n...Lorem ipsum...\n...\n...Lorem ipsum...\n...\n...")

    
    t.grid(column = 0, row = 10, sticky = 'nwes')


    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    mainframe.columnconfigure(2, weight=1)
    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

    msg_entry.focus()


    root.bind("<Return>", _send_message)

    root.mainloop()



main()
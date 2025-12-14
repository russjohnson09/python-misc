from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from lib_network import TcpServer
from instant_message import instant_messenger as im

# https://www.pythonguis.com/tutorials/tkinter-basic-widgets/

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(round(0.3048 * value, 4))
    except ValueError:
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

root.geometry("850x800")

def main():
    print("init client")
    im.client_init()

    # https://www.geeksforgeeks.org/python/python-tkinter-text-widget/

    mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

    feet = StringVar()
    feet_entry = ttk.Entry(mainframe, width=7, 
        textvariable=feet)
    feet_entry.grid(column=0, row=11, sticky=(W, E))

    meters = StringVar()
    ttk.Label(mainframe,
    textvariable=meters).grid(column=2, 
    row=2, sticky=(W, E))



    ttk.Button(mainframe, text="Calculate", 
    command=calculate).grid(column=3, row=3, sticky=W)

    ttk.Button(mainframe, text="Connect Client", 
    command=_client_connect).grid(column=3, row=4, sticky=W)


    ttk.Button(mainframe, text="Start Server", 
    command=_start_server).grid(column=3, row=5, sticky=W)

    ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
    # ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
    # ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)


# https://www.geeksforgeeks.org/python/python-tkinter-text-widget/
    # inputtxt = Text(root, height = 10,
    #                 width = 25,
    #                 bg = "light yellow")
    # inputtxt.pack()

    # ttk.Text(mainframe, 
    # text="is equivalent to").grid(
    #     column=1, row=2, sticky=E
    #     )
    # https://tkdocs.com/tutorial/text.html
    # https://docs.python.org/3/library/tkinter.scrolledtext.html
    # https://stackoverflow.com/questions/76654344/why-is-my-tkinter-scrollbar-is-not-showing-up-on-my-text-widget
    
    # https://github.com/roseman/tkdocs/blob/master/scrolledtext.py
    
    # https://stackoverflow.com/questions/42006805/python-scrolledtext-module
    t = ScrolledText(mainframe, width = 90, 
    
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

    feet_entry.focus()


    root.bind("<Return>", calculate)

    root.mainloop()



main()
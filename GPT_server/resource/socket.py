"""
Socket server classs
"""
import socketserver
import threading as th
from tkinter import END
from default_library.configuration import DataConfiguration
from resource.gui import gui


iplist = []
# you could use database to track ip address


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    Create a server socket
    """
    def handle(self):
        self.data = self.request.recv(1024).strip()
        gui_enable()
        user_ip = str(self.client_address[0])
        if user_ip not in iplist:
            gui.username_box.insert(END, (user_ip +"\n"))
            iplist.append(user_ip)
        gui.message_box.insert(END, ("User: "+ self.data.decode('utf-8')+"\n"))
        gui_disable()
    # End handle function
# End MyTCPHandler class


class ServerRunner(object):
    """
    A class controls MyTCPHandler
    """
    def __init__(self):
        """
        Rerturn:
            None
        """ 
        
        self.server = None
    # End init built in
    

    def end_connection(self):
        """
        Kill the connection
        """
        self.server.shutdown()
    # End end_conection function
        

    def start(self, config: DataConfiguration):
        """
        start running server
        """
        try:
            process_gui = th.Thread(target=gui.start)
            process_gui.start()
            with socketserver.TCPServer((config.host_address, config.port_number), 
                                        MyTCPHandler) as server:
                self.server = server
                self.server.serve_forever()
        except KeyboardInterrupt:
            print("Server stop")
    # End start function
# End ServerRunner class
        

def gui_enable():
    gui.message_box.config(state='normal')
    gui.username_box.config(state='normal')


def gui_disable(): 
    gui.message_box.config(state='disabled')    
    gui.username_box.config(state='disabled')


sr = ServerRunner()


if __name__ == "__main__":
    pass


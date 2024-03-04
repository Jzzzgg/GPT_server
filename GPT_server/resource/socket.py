import socketserver
from tkinter import Tk, END
from default_library.constants import HOST, PORT
from resource.gui import gui


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    Create a server socket
    """
    def handle(self):
        
        # self.request is the TCP socket connected to the client
        self.data = self.rfile.readline().strip()
        gui.username_box.config(state='normal')
        gui.message_box.config(state='normal')
        gui.username_box.insert(END, self.client_address[0])
        print("Received from {}:".format(self.client_address[0]))
        print(self.data)
        gui.message_box.insert(END, self.data)
        gui.username_box.config(state='disabled')
        gui.message_box.config(state='disabled')
    # End handle function
# End MyTCPHandler class


class ServerRunner(object):
    """
    A class controls MyTCPHandler
    """
    def __init__(self) -> None:
        """
        Rerturn:
            None
        """
        self.sever = None
    # End init built in
    

    def start(self) -> None:
        """
        start running server
        """
        gui.start()
        # Create the server, binding to localhost on port 9999
        with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
            # Activate the server; this will keep running until you
            # interrupt the program with Ctrl-C
            self.server = server
            # self.server.serve_forever()
    # End start function
    

    def end_connection(self) -> None:
        """
        Kill the connection
        """
        self.sever.shutdown()


sr = ServerRunner()


if __name__ == "__main__":
    pass


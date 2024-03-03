"""
Create a GUI to display message
"""

from tkinter import *
from default_library.constants import (BOTTOM, TOP, LEFT, RIGHT, BLACK)

class GUI(object):
    def __init__(self) -> None:
        """
        Create a tkinter windown
        Args: 
            None
        Return:"
            None
        """
        self.window = None
    # End init built-in
    

    def start(self) -> None:
        """
        Start GUI and draw window
        Args: 
            None
        Return:"
            None
        """
        self.window = Tk()
        self.draw_window()
        self.window.mainloop()
    # End start function
        
    
    def draw_window(self) -> None:
        """
        Layout of window
        Args:
            None
        Return:
            None
        """
        total_width = 120
        message_width = 104

        window = self.window
        window.title("ChatGPT server")

        frame = Frame(window, width=total_width+20)
        frame.pack()
        
        left_frame = LabelFrame(frame, text="Username", width=(total_width - message_width))
        left_frame.pack(side=LEFT)

        self.username_box = username_box = Entry(left_frame)
        username_box.config(state="disabled")
        username_box.pack(side=LEFT)

        right_frame = LabelFrame(frame, width=message_width, text="Messages")
        right_frame.pack(side=RIGHT)

        self.memessage_box = message_box = Text(right_frame)
        message_box.config(state="disabled")
        message_box.pack(side=LEFT)
    # End draw_window function
# End GUI class


gui = GUI()


if __name__ == "__main__":
    pass
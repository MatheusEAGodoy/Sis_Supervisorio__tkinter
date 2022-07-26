from tkinter import *

class Application:

    def __init__(self, master=None):
        self.container_01 = Frame(master)
        self.container_01.config(width=400,height=400,bg="Black")
        self.container_01.pack()
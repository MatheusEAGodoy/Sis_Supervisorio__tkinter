from tkinter import *
from src.Palete import *
from src.widgets.Relogio import Relogio

class Sis_sup_menu():
    def __init__(self, master=None, menu_height=0, menu_width=0):

        self.container_relogio = Frame(master)
        self.container_relogio.place(x=10,y=0)          # posicionamento do relogio
        Relogio(self.container_relogio,menu_height,100) # widget relogio
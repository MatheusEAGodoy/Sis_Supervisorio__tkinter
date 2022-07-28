from tkinter import *
from src.Palete import *
from src.widgets.Relogio import Relogio
from src.widgets.Custom_button import Custom_button
from src.widgets.X_button import X_button

class Sis_sup_menu():
    def __init__(self, master=None, menu_height=0, menu_width=0):

        self.container_relogio = Frame(master)
        self.container_relogio.place(x=10,y=10)          # posicionamento do relogio
        #Relogio(self.container_relogio,menu_height,100) # widget relogio
        self.botao = X_button(self.container_relogio)
        self.botao.configure()
        self.botao.bind()
        self.botao.pack()

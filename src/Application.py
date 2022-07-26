from tkinter import *
from src.Palete import *
from src.App_menu import *
from src.App_sinoptico import *

class Application:
    def __init__(self, master=None):
        menu_height = 100
        div_height = 5

        Screen_Width = master.winfo_screenwidth()    # largura da tela renderizada [pixels]
        Screen_Height = master.winfo_screenheight()   # altura da tela renderizada [pixels]
        
        main_screen_Height = Screen_Height - menu_height - div_height    # altura da tela principal

        self.container_01 = Frame(master)                                               # frame do menude navegação
        self.container_01.config(width=Screen_Width,height=menu_height,bg=bg_default)      # configuração de tamanho e cor do frame
        #self.container_01.config(highlightbackground=App_amarelo,highlightthickness=5)    # configuração de tamanho e cor da borda do frame
        self.container_01.pack_propagate(False)                                         # impede que o frame seja redimensionado
        self.container_01.pack()
        Sis_sup_menu(self.container_01,menu_height,Screen_Width)

        self.div = Frame(master)
        self.div.config(width=Screen_Width,height=div_height,bg=App_cinzaC)
        self.div.pack_propagate(False)                                         # impede que o frame seja redimensionado
        self.div.pack()

        self.container_02 = Frame(master)                                               # frame do menude navegação
        self.container_02.config(width=Screen_Width,height=main_screen_Height,bg=bg_default)# configuração de tamanho e cor do frame
        #self.container_02.config(highlightbackground=App_amarelo,highlightthickness=5)    # configuração de tamanho e cor da borda do frame
        self.container_02.pack_propagate(False)                                         # impede que o frame seja redimensionado
        self.container_02.pack()
        Sis_sup_sinoptico(self.container_02)
      



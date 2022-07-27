from tkinter import Frame, Label
from src.Palete import *
import time

class Relogio:
    def __init__(self, master=None, relogio_height=0, relogio_width=0):
        
        self.container_01 = Frame(master)
        self.container_01.config(width=relogio_width,height=relogio_height,bg=App_cinzaC)
        self.container_01.pack_propagate(False)
        self.container_01.pack()

        self.hora = Label(self.container_01, text="hora", font=("Segoe UI Variable", 25), foreground='white', background=bg_default)
        self.hora.place(x=0,y=0)

        self.data = Label(self.container_01, text="data", font=("Segoe UI Variable", 15), foreground='white', background=bg_default)
        self.data.place(x=0,y=50)

        self.Atualizar_relogio()
        
        
    def Atualizar_relogio(self):
        hora = time.strftime("%H")
        minuto = time.strftime("%M")
        dia_da_semana = time.strftime("%w")

        self.hora.config(text=hora + ":" + minuto)
        self.hora.after(1000, self.Atualizar_relogio)

        self.data.config(text=self.dia_semana(dia_da_semana))
    

    def dia_semana(self, x):
        if type(x) is not int:
            x = int(x)
        return {
            0:"Domingo",
            1:"Segunda",
            2:"Terça",
            3:"Quarta",
            4:"Quinta",
            5:"Sexta",
            7:"Sábado"
        }.get(x,"Not found")

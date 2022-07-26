from tkinter import *
from src.Application import Application


root = Tk()

#root.attributes('-fullscreen', True)   #Full screen sem barra superior
root.state('zoomed')                    #Full screen com barra superior


Application(root)


root.mainloop()
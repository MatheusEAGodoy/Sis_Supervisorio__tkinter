from tkinter import *

from src.widgets.Custom_button import Custom_button

class X_button(Custom_button):
    def __init__(self, master=None):
        Custom_button.__init__(self,master)
        

    def create_shape(self,x = 5,y = 5,x_size = 50,y_size = 25,radius = 50,color = "#000000",**kwargs): #round
        points = [
            x               ,y,
            x+radius        ,y,
            x+x_size-radius ,y,

            x+x_size        ,y,
            x+x_size        ,y+radius ,
            x+x_size        ,y+y_size-radius,

            x+x_size        ,y+y_size,
            x+x_size-radius ,y+y_size,
            x+radius        ,y+y_size,

            x               ,y+y_size,
            x               ,y+y_size-radius,
            x               ,y+radius
        ]

        return self.canva.create_polygon(points, smooth=True, fill=color)


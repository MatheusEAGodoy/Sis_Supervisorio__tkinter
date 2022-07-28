from tkinter import *

class Custom_button:
    def __init__(self, master=None):
        self.init_property()
        self.canva = Canvas(master, highlightthickness=0, cursor="hand2")
        self.configure()
        self.draw_init()
        self.bind()
        
        pass

    def init_property(self):
        #configuration default values
        self.bg = "#009900"             # canva bg color
        self.pressed_bg = "#0000bb"     # shape pressed color
        self.hover_bg = "#0000aa"       # shape hover color
        self.idle_bg = "#000099"        # shape idle color
        self.highlight = "#ffffff"      # shape highlight color
        self.highlightthickness = 0

        self.height = 50
        self.width = 100

    def configure(self,bg_color = None,height = None,width = None,hover_color = None,pressed_color = None,idle_color = None,highlight_color = None, highlight_thickness = None): 
        if bg_color is not None:            self.bg = bg_color
        if hover_color is not None:         self.hover_bg = hover_color
        if pressed_color is not None:       self.pressed_bg = pressed_color
        if idle_color is not None:          self.idle_bg = idle_color
        if highlight_color is not None:     self.highlight = highlight_color
        if highlight_thickness is not None: self.highlightthickness = highlight_thickness

        if height is not None:              self.height = height
        if width is not None:               self.width = width

        self.canva.config(bg = self.bg, height = self.height, width = self.width)
        #self.bind()

    def bind(self):
        self.canva.bind("<Button-1>",func = lambda x: self.draw_pressed())
        self.canva.bind("<Enter>",func = lambda x: self.draw_enter())
        self.canva.bind("<Leave>",func = lambda x: self.draw_idle())
        self.canva.bind("<ButtonRelease-1>",func = lambda x: self.draw_release())
        pass

    def pack(self):

        self.canva.pack()
        pass

    def place(self,posx=0,posy=0):
        self.canva.place(posx,posy)
    
    #==========================================================
    def draw_init(self):
        self.shape_bg = self.draw_bg(color = self.idle_bg)
        self.shape_fg = self.draw_fg(color = self.idle_bg)

    def draw_idle(self):
        self.draw_clear()
        self.shape_bg = self.draw_bg(color = self.idle_bg)
        self.shape_fg = self.draw_fg(color = self.idle_bg)

    def draw_enter(self, **kwargs):         #hover
        self.draw_clear()
        self.shape_bg = self.draw_bg(color = self.highlight)
        self.shape_fg = self.draw_fg(color = self.hover_bg)

    def draw_pressed(self, **kwargs):
        self.draw_clear()
        self.shape_bg = self.draw_bg(color = self.highlight)
        self.shape_fg = self.draw_fg(color = self.pressed_bg)

    def draw_release(self, **kwargs):
        self.draw_clear()
        self.draw_enter()
    
    def draw_clear(self):
        self.draw_delete(self.shape_bg)
        self.draw_delete(self.shape_fg)

    def draw_delete(self,shape):
        self.canva.delete(shape)
    
    def draw_bg(self,color = "#000000"):
        x1 = 0
        y1 = 0
        x_size1 = self.width
        y_size1 = self.height
        return self.create_shape(x1,y1,x_size1,y_size1, color = color)

    def draw_fg(self,color = "#000000"):
        x2 = 0 + self.highlightthickness
        y2 = 0 + self.highlightthickness
        x_size2 = self.width - 2*self.highlightthickness
        y_size2 = self.height - 2*self.highlightthickness
        return self.create_shape(x2,y2,x_size2,y_size2, color = color)

    def create_shape(self,x = 5,y = 5,x_size = 50,y_size = 25,color = "#000000",**kwargs):
        return self.canva.create_rectangle(x, y, x + x_size, y + y_size, fill=color,width=0)


#!/usr/bin/env python3
'''
Пример объектной организации кода
'''

from tkinter import *
from tkinter import colorchooser

class App(Frame):
    '''Base framed application class'''
    def __init__(self, master=None, Title="Application"):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.title(Title)
        self.grid(sticky=N+E+S+W)
        self.create()
        self.adjust()

    def create(self):
        '''Create all the widgets'''
        self.bQuit = Button(self, text='Quit', command=self.quit)
        self.bQuit.grid()

    def adjust(self):
        '''Adjust grid size/properties'''
        # TODO Smart detecting resizeable/still cells
        for i in range(self.size()[0]):
            self.columnconfigure(i, weight=12)
        for i in range(self.size()[1]):
            self.rowconfigure(i, weight=12)
        
class Paint(Canvas):
    '''Canvas with simple drawing'''
    def mousedown(self, event):
        '''Store mousedown coords'''
        self.x0, self.y0 = event.x, event.y
        self.cursor = None

    def mousemove(self, event):
        '''Do sometheing when drag a mouse'''
        if self.cursor:
            self.delete(self.cursor)
        self.cursor = self.create_line((self.x0, self.y0, event.x, event.y), fill=self.foreground.get())

    def mouseup(self, event):
        '''Dragging is done'''
        self.cursor = None
        #print(self.find_all())

    def __init__(self, master=None, *ap, foreground="black", **an):
        self.foreground = StringVar()
        self.foreground.set(foreground)
        Canvas.__init__(self, master, *ap, **an)
        self.bind("<Button-1>", self.mousedown)
        self.bind("<B1-Motion>", self.mousemove)
        self.bind("<ButtonRelease-1>", self.mouseup)

class MyApp(App):
    def askcolor1(self):
        ret = colorchooser.askcolor()[1]
        if (ret != None):
            self.Canvas1.foreground.set(ret)
            print(self.Canvas1.foreground.get())
            self.Frame.ShowColor1.configure(bg = self.Canvas1.foreground.get())
    
    def askcolor2(self):
        ret = colorchooser.askcolor()[1]
        if (ret != None):
            self.Canvas2.foreground.set(ret)
            print(self.Canvas2.foreground.get())
            self.Frame.ShowColor2.configure(bg = self.Canvas2.foreground.get())

    def create(self):
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, minsize = 60)
        self.columnconfigure(2, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 1)
        self.Canvas1 = Paint(self, foreground="Green")
        self.Canvas1.grid(row=0, column=0, sticky=N+E+S+W)
        self.Canvas2 = Paint(self, foreground="Red")
        self.Canvas2.grid(row=0, column=2, sticky=N+E+S+W)
        self.Frame = Frame(self, relief = SUNKEN, bd = 3)
        self.Frame.grid(row=0, column=1, sticky=N+E+S+W)
        self.Frame.columnconfigure(0, weight = 1)
        self.Frame.ShowColor1 = Button(self.Frame, textvariable=self.Canvas1.foreground, command=self.askcolor1, width = 10, bg = self.Canvas1.foreground.get())
        self.Frame.ShowColor1.grid(row=0, column=0, sticky=N+W)
        self.Frame.ShowColor2 = Button(self.Frame, textvariable=self.Canvas2.foreground, command=self.askcolor2, width = 10, bg = self.Canvas2.foreground.get())
        self.Frame.ShowColor2.grid(row=0, column=1, sticky=N+W)
        self.Frame.Quit = Button(self.Frame, text="Quit", command=self.quit, width = 10)
        self.Frame.Quit.grid(row=6, column=0, columnspan = 2, sticky=S+W)
        

app = MyApp(Title="Canvas Example")
app.mainloop()
#for item in app.Canvas.find_all():
#    print(*app.Canvas.coords(item), app.Canvas.itemcget(item, "fill"))


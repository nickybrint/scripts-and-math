from Tkinter import *
from PIL import Image, ImageTk
import Mandelbrot
import math


class App:

    
    def __init__(self, master):
        self.point1 = [-1, -1]
        self.point2 = [-1, -1]
        self.released = True
        self.IMAGE_WIDTH, self.IMAGE_HEIGHT = 500, 500
        self.iterations = 30.0
        self.currentWidth = 3.0
        self.topLeftCorner = [-1.5, 1.5]
        
        frame = Frame(master)
        frame.pack()

        #self.i = Image.open('C:\Users\User 1\Desktop\Mandelbrot Set\img\mandelbrot37.png')
        self.i = Mandelbrot.main(-1.5, 1.5, -1.5, self.IMAGE_WIDTH, self.IMAGE_HEIGHT, self.iterations)
        self.photo = ImageTk.PhotoImage(self.i)
        self.panel = Label(root, image=self.photo)
        self.panel.image = self.photo
        self.panel.pack()
        master.bind("<Button-1>", self.onClick)
        master.bind("<ButtonRelease-1>", self.onRelease)
        #master.bind("<B1-Motion>", self.drawBox)


    def onClick(self, event):
        self.point1 = [event.x, event.y]
        self.released = False

    def onRelease(self, event):
        self.point2 = [event.x, event.y]
        self.released = True
        if self.point1[0] == self.point2[0] or self.point1[1] == self.point2[0]:
            return
            
        newLeft = float(self.point1[0])/self.IMAGE_WIDTH*self.currentWidth + self.topLeftCorner[0]
        newRight = float(self.point2[0])/self.IMAGE_WIDTH*self.currentWidth + self.topLeftCorner[0]
        newBottom = -float(self.point2[1])/self.IMAGE_WIDTH*self.currentWidth + self.topLeftCorner[1]
        self.currentWidth = newRight - newLeft
        self.topLeftCorner = [newLeft, newBottom + self.currentWidth]
        self.iterations = math.log(90.0/self.currentWidth, 2)*10

        '''
        print newLeft, newRight, newBottom
        print self.currentWidth, self.topLeftCorner, self.iterations
        '''
        
        self.i = Mandelbrot.main( newLeft,
                                newRight,
                                newBottom,
                                self.IMAGE_HEIGHT,
                                self.IMAGE_WIDTH,
                                self.iterations )

        self.photo = ImageTk.PhotoImage(self.i)
        self.panel.configure(image = self.photo)
        self.panel.image = self.photo



        



root = Tk()
app = App(root)



    

root.mainloop()

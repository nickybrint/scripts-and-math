from Tkinter import *
from PIL import Image, ImageTk
import Mandelbrot
import math
import datetime


class App:
    '''
        Displays the Mandelbrot set.
        Allows user to zoom in on area with mouse click and drag.
        Sets height automatically to preserve aspect ratio.
    '''
    
    def __init__(self, master, menu):
        
        #store the windows
        self.master = master
        self.menu = menu
        
        #left of zoom selection
        self.point1 = [0, 0]
        #bottom right of zoom selection
        self.point2 = [0, 0]
        #current mouse position
        self.point3 = [0, 0]
        #whether zoom selection was cancelled
        self.cancelled = False
        #pixel dimensions
        self.IMAGE_WIDTH, self.IMAGE_HEIGHT = 600, 600
        #iterations for the mandelbrot generator
        self.iterations = 30.0
        #width (on graph) of the current view
        self.currentWidth = 3.0
        #position of frame (0, 0) in graph coordinates
        self.topLeftCorner = [-1.5, 1.5]

        #create the drawing area, a 'Canvas'
        self.panel = Canvas(master, width=self.IMAGE_WIDTH, height=self.IMAGE_HEIGHT)
        self.panel.pack()

        #generate an image of the Mandelbrot set
        self.i = Mandelbrot.main(-1.5, 1.5, -1.5, self.IMAGE_WIDTH, self.IMAGE_HEIGHT, self.iterations)
        #convert it into a Tk.PhotoImage
        self.photo = ImageTk.PhotoImage(self.i)
        #draw it on the Canvas
        self.panel.create_image((0, 0), anchor='nw', image=self.photo)

        #set up mouse controls
        master.bind("<Button-1>", self.onClick) #left-mouse click
        master.bind("<ButtonRelease-1>", self.onRelease) #left mouse release
        master.bind("<B1-Motion>", self.drawBox) #left mouse drag
        master.bind("<Button-3>", self.cancel) #right mouse click

        #add buttons to the menu
        self.button = Button(menu, text="Save to File", command=self.save)
        self.button.pack(side=LEFT)
        self.button = Button(menu, text="      Exit      ", command=self.quit)
        self.button.pack(side=LEFT)


    def onClick(self, event):
        self.point1 = [event.x, event.y]
        self.cancelled = False

    def onRelease(self, event):
        if self.cancelled:
            return

        self.point2 = [event.x, event.y]
        
        if self.point1[0] == self.point2[0] or self.point1[1] == self.point2[0]:
            return

        #calculate the region that the user selected  
        newLeft = float(self.point1[0])/self.IMAGE_WIDTH*self.currentWidth + self.topLeftCorner[0]
        newRight = float(self.point2[0])/self.IMAGE_WIDTH*self.currentWidth + self.topLeftCorner[0]
        newBottom = -float(self.point2[1])/self.IMAGE_WIDTH*self.currentWidth + self.topLeftCorner[1]
        if newLeft > newRight:
            temp = newLeft
            newLeft = newRight
            newRight = temp
        #new width
        self.currentWidth = newRight - newLeft 
        self.topLeftCorner = [newLeft, newBottom + self.currentWidth]
        #the deeper the user goes, the harder the Mandelbrot generator has to check each point
        self.iterations = math.log(90.0/self.currentWidth, 2)*10


        

        '''
        print newLeft, newRight, newBottom
        print self.currentWidth, self.topLeftCorner, self.iterations
        '''

        #generate new image
        self.i = Mandelbrot.main( newLeft,
                                newRight,
                                newBottom,
                                self.IMAGE_HEIGHT,
                                self.IMAGE_WIDTH,
                                self.iterations )
        #format it as a Tk.PhotoImage
        self.photo = ImageTk.PhotoImage(self.i)
        #draw it on the Canvas
        self.panel.create_image((0, 0), anchor='nw', image=self.photo)

    def drawBox(self, event):
        #redraw the background
        self.panel.create_image((0, 0), anchor='nw', image=self.photo)
        
        if not self.cancelled:
            self.point3 = [event.x, event.y]
            #put a box over the region the user selects
            self.panel.create_rectangle( self.point1[0],
                                        self.point3[1] - abs(self.point3[0] - self.point1[0]),
                                        self.point3[0],
                                        self.point3[1],
                                        fill="",
                                        outline="white" )
        
    #on right click
    def cancel(self, event):
        self.cancelled = True
        #redraw the background
        self.panel.create_image((0, 0), anchor='nw', image=self.photo)

    def save(self):
        #date_time = datetime.datetime.now().strftime("%H_%M_%m_%d_%y")
        location = ('x' + str(self.topLeftCorner[0])
                    + '_y' + str(self.topLeftCorner[1])
                    + '_width' + str(self.currentWidth) )
        #save the PIL-format image
        self.i.save('img\mandelbrot_' + location + '.jpg')

    def quit(self):
        #destroy both windows
        try:
            self.master.destroy()
        except:
            pass
        self.menu.destroy()

print "Loading..."
#the image displayer
root = Tk()
root.title("Mandelbrot Explorer")
#the menu
save_button = Tk()
save_button.title("")
save_button.geometry('+600+0')

app = App(root, save_button)
root.mainloop()

from Tkinter import *
import math
import time


class App:

    def __init__(self, master):

        #initialize physics settings
        self.now = lambda: int(time.time() * 1000)
        self.lastTime = self.now()
        self.ROD_LENGTH_METERS = 1.5
        self.GRAVITY = -10

        #initialize display settings
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = 600, 600
        self.METER_SIZE_PIXELS = 100
        self.ROD_LENGTH_PIXELS = self.ROD_LENGTH_METERS * self.METER_SIZE_PIXELS

        #initialize the window
        self.master = master
        self.panel = Canvas( master,
                            width=self.WINDOW_WIDTH,
                            height=self.WINDOW_HEIGHT )
        self.panel.pack()

        #position the rod
        self.theta = 0.7853 #45 degrees, in radians
        self.omega = 0.0    #radians/second

        #draw the rod
        self.line = self.panel.create_line(
                self.WINDOW_WIDTH/2,
                self.WINDOW_HEIGHT/2,
                self.WINDOW_WIDTH/2 + math.sin(self.theta)*self.ROD_LENGTH_PIXELS,
                self.WINDOW_HEIGHT/2 + math.cos(self.theta)*self.ROD_LENGTH_PIXELS,
                width=10
                        )


    def draw(self):
        '''
            redraw the rods
        '''
        
        dt = (self.now() - self.lastTime)/1000.0
        self.theta += self.omega*dt
        self.omega += 1.5 * self.GRAVITY * math.sin(self.theta) / self.ROD_LENGTH_METERS * dt
        self.panel.coords(
                self.line,
                self.WINDOW_WIDTH/2,
                self.WINDOW_HEIGHT/2,
                self.WINDOW_WIDTH/2 + math.sin(self.theta)*self.ROD_LENGTH_PIXELS,
                self.WINDOW_HEIGHT/2 + math.cos(self.theta)*self.ROD_LENGTH_PIXELS
                        )
        self.panel.update()
        self.lastTime = self.now()




root = Tk()
root.title("Double Pendulum")
app = App(root)
while True:
    app.draw()
    root.update_idletasks()
    root.update()
    time.sleep(0.02)
    
root.mainloop()

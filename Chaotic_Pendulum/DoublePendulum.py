from Tkinter import *
import math
import time


class App:

    def __init__(self, master):
        '''
        simulates a double pendulum:
        simulation is stable for a long time,
        but after a while, it mysteriously loses/gains energy
        depending on how many times I loop the
        two alpha calculations (they depend on each other).
        (floating-point errors?)
    '''

        #initialize physics settings
        self.now = lambda: int(time.time() * 1000)
        self.lastTime = self.now()
        self.ROD1_LENGTH_METERS = 1.5
        self.ROD2_LENGTH_METERS = 2.5
        self.GRAVITY = 10
        self.BALL1_MASS = 200.0
        self.BALL2_MASS = 100.0

        #initialize display settings
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = 600, 600
        self.METER_SIZE_PIXELS = 50
        self.ROD1_LENGTH_PIXELS = self.ROD1_LENGTH_METERS * self.METER_SIZE_PIXELS
        self.ROD2_LENGTH_PIXELS = self.ROD2_LENGTH_METERS * self.METER_SIZE_PIXELS
        self.BALL1_RADIUS = self.BALL1_MASS**(1.0/3.0) * 1.5
        self.BALL2_RADIUS = self.BALL2_MASS**(1.0/3.0) * 1.5

        #initialize the window
        self.master = master
        self.panel = Canvas( master,
                            width=self.WINDOW_WIDTH,
                            height=self.WINDOW_HEIGHT,
                             bg='#961414')
        self.panel.pack()

        #position the rods
        self.theta1 = 0.7853*4 #0.7853 is 45 degrees, in radians
        self.theta2 = 0.7853*4
        self.omega1 = 0.0    #radians/second
        self.omega2 = 0.0
        self.alpha1 = 0.0   #radians/second/second
        self.alpha2 = 0.0
        
        #draw the first pendulum
        #set the end-point
        x_1, y_1 = (self.WINDOW_WIDTH/2 + math.sin(self.theta1)*self.ROD1_LENGTH_PIXELS,
                    self.WINDOW_HEIGHT/2 + math.cos(self.theta1)*self.ROD1_LENGTH_PIXELS
                    )
        #draw the rod
        self.line1 = self.panel.create_line(
                self.WINDOW_WIDTH/2,
                self.WINDOW_HEIGHT/2,
                x_1 - self.BALL1_RADIUS,
                y_1 - self.BALL1_RADIUS,
                fill='white'
                )
        #draw the weight
        self.ball1 = self.panel.create_oval(
                x_1 - self.BALL1_RADIUS,
                y_1 - self.BALL1_RADIUS,
                x_1 + self.BALL1_RADIUS,
                y_1 + self.BALL1_RADIUS,
                fill='white'
                )
        #draw the second pendulum
        #set the end-point
        x_2, y_2 = (x_1 + math.sin(self.theta2)*self.ROD2_LENGTH_PIXELS,
                    y_1 + math.cos(self.theta2)*self.ROD2_LENGTH_PIXELS
                    )
        #draw the rod
        self.line2 = self.panel.create_line(
                x_1 + self.BALL1_RADIUS,
                y_1 + self.BALL1_RADIUS,
                x_2 - self.BALL2_RADIUS,
                y_2 - self.BALL2_RADIUS,
                fill='white'
                )
        #draw the weight
        self.ball2 = self.panel.create_oval(
                x_2 - self.BALL2_RADIUS,
                y_2 - self.BALL2_RADIUS,
                x_2 + self.BALL2_RADIUS,
                y_2 + self.BALL2_RADIUS,
                fill='white'
                )


    def draw(self):
        '''
            redraw the rods
        '''

        #it's not a game, so make dt constant
        dt = 0.03
        '''
        dt = (self.now() - self.lastTime)/1000.0
        self.lastTime = self.now()
        '''
        
        #update positions
        self.theta1 += self.omega1 * dt
        self.theta2 += self.omega2 * dt

        #update velocities
        #do long calculations here so they're not repeated
        SINE_DIFFERENCE = math.sin(self.theta1 - self.theta2)
        COSINE_DIFFERENCE = math.cos(self.theta1 - self.theta2)
        SINE_THETA1 = math.sin(self.theta1)
        SINE_THETA2 = math.sin(self.theta2)
        L2_OVER_L1 = self.ROD2_LENGTH_METERS / self.ROD1_LENGTH_METERS
        L1_OVER_L2 = self.ROD1_LENGTH_METERS / self.ROD2_LENGTH_METERS
        M2_OVER_MTOT = self.BALL2_MASS / (self.BALL1_MASS + self.BALL2_MASS)

        #so solution converges toward actual one
        for i in range(0, 5):
            self.alpha1 = (
                    - M2_OVER_MTOT * L2_OVER_L1 * (COSINE_DIFFERENCE * self.alpha2
                                                   + SINE_DIFFERENCE * self.omega2*self.omega2)
                    - self.GRAVITY * SINE_THETA1 / self.ROD1_LENGTH_METERS
                    )
            

            self.alpha2 = (
                    - L1_OVER_L2 * (COSINE_DIFFERENCE * self.alpha1 - SINE_DIFFERENCE * self.omega1*self.omega1)
                    - self.GRAVITY * SINE_THETA2 / self.ROD2_LENGTH_METERS
                    )
        
        self.omega1 += self.alpha1 * dt
        self.omega2 += self.alpha2 * dt

        
        #draw the first pendulum
        #set the end-point
        x_1, y_1 = (self.WINDOW_WIDTH/2 + math.sin(self.theta1)*self.ROD1_LENGTH_PIXELS,
                    self.WINDOW_HEIGHT/2 + math.cos(self.theta1)*self.ROD1_LENGTH_PIXELS
                    )
        #draw the rod
        
        self.panel.coords(
                self.line1,
                self.WINDOW_WIDTH/2,
                self.WINDOW_HEIGHT/2,
                x_1,
                y_1
                )
                
        #draw the weight
        self.panel.coords(
                self.ball1,
                x_1 - self.BALL1_RADIUS,
                y_1 - self.BALL1_RADIUS,
                x_1 + self.BALL1_RADIUS,
                y_1 + self.BALL1_RADIUS,
                )
        #draw the second pendulum
        #set the end-point
        x_2, y_2 = (x_1 + math.sin(self.theta2)*self.ROD2_LENGTH_PIXELS,
                    y_1 + math.cos(self.theta2)*self.ROD2_LENGTH_PIXELS
                    )
        #draw the rod
        
        self.panel.coords(
                self.line2,
                x_1,
                y_1,
                x_2,
                y_2
                )
                
        #draw the weight
        self.panel.coords(
                self.ball2,
                x_2 - self.BALL2_RADIUS,
                y_2 - self.BALL2_RADIUS,
                x_2 + self.BALL2_RADIUS,
                y_2 + self.BALL2_RADIUS
                )
        self.panel.update()
        #print self.alpha1, self.alpha2, self.omega1, self.omega2, self.theta1, self.theta2





root = Tk()
root.title("Double Pendulum")
app = App(root)
while True:
    app.draw()
    root.update_idletasks()
    root.update()
    time.sleep(0.03)
    
root.mainloop()

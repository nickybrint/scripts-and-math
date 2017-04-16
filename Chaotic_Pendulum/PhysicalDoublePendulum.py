from Tkinter import *
import math
import time


class App:
    '''
        simulates a physical double pendulum for a more satisfying chaotic experience
            (i.e. the rods are solid)

        bug:
        simulation is stable for a long time,
        but after a while, it mysteriously gains energy (floating-point errors?)
    '''

    def __init__(self, master):

        #initialize physics settings
        self.now = lambda: int(time.time() * 1000)
        self.lastTime = self.now()
        #these are the initial conditions you want to mess with
        self.ROD1_LENGTH_METERS = 1.0
        self.ROD2_LENGTH_METERS = 0.5
        self.GRAVITY = 10
        self.BAR1_MASS = 100.0
        self.BAR2_MASS = 100.0

        #initialize display settings
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = 600, 600 #pixels
        self.METER_SIZE_PIXELS = 190 #pixels/meter
        self.ROD1_LENGTH_PIXELS = self.ROD1_LENGTH_METERS * self.METER_SIZE_PIXELS
        self.ROD2_LENGTH_PIXELS = self.ROD2_LENGTH_METERS * self.METER_SIZE_PIXELS

        #initialize the window
        self.master = master
        self.panel = Canvas( master,
                            width=self.WINDOW_WIDTH,
                            height=self.WINDOW_HEIGHT,
                             bg='#E0FFFF')
        self.panel.pack()

        #position the rods
        #these are the initial conditions you want to mess with
        self.theta1 = 0.7853*3.95 #45 degrees, in radians
        self.theta2 = 0.7853*3.95
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
                x_1,
                y_1,
                width=6,
                fill='#2f4f4f'
                )

        #draw the second pendulum
        #set the end-point
        x_2, y_2 = (x_1 + math.sin(self.theta2)*self.ROD2_LENGTH_PIXELS,
                    y_1 + math.cos(self.theta2)*self.ROD2_LENGTH_PIXELS
                    )
        #draw the rod
        self.line2 = self.panel.create_line(
                x_1,
                y_1,
                x_2,
                y_2,
                width=6,
                fill='#2f4f4f'
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
        MTOT = (self.BAR1_MASS + 3*self.BAR2_MASS)

        #loop so solution converges toward actual one
        for i in range(0, 100):
            #solution to Euler-Lagrange equations
            self.alpha1 = (
                        -0.5 / MTOT * (
                        L2_OVER_L1 * self.BAR2_MASS * (self.alpha2 * COSINE_DIFFERENCE + 2*self.omega2*self.omega2 * SINE_DIFFERENCE)
                        + self.GRAVITY * SINE_THETA1 * (self.BAR1_MASS + 2*self.BAR2_MASS) / self.ROD1_LENGTH_METERS
                        )
                    )
            

            self.alpha2 = (
                    - 1 / 3.0 * L1_OVER_L2 * (COSINE_DIFFERENCE * self.alpha1 - SINE_DIFFERENCE * self.omega1*self.omega1)
                    - 0.5 * self.GRAVITY * SINE_THETA2 / self.ROD2_LENGTH_METERS
                    )

        #update velocities
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
                
        self.panel.update()
        #print self.alpha1, self.alpha2, self.omega1, self.omega2, self.theta1, self.theta2





root = Tk()
root.title("Double Physical Pendulum")
app = App(root)
while True:
    app.draw()
    try:
        #root.update_idletasks()
        root.update()
    except:
        break
    time.sleep(0.03)
    
root.mainloop()

import pylab as pl
import math
class flying_cannon:
    """
    Calculation of the trajectory of the cannon
    Home work of the second chapter done by He Yijun
    Question 2.7
    """
    def __init__(self,angle = 3.14/4 , velocity = 700,location_x = 0, location_y = 0, time_step = 0.01 , B_over_m =0.00004):
        # unit of time is s ; unit of angle is rad
        self.v_x = [velocity * math.cos(angle)]
        self.v_y = [velocity * math.sin(angle)]
        self.v=[velocity]        
        self.x = [location_x]        
        self.y = [location_y]
        self.t = [0]
        self.dt = time_step
        self.const = B_over_m
        self.g = 9.8
        print("Initial velocity ->", velocity)
        print("Initial angle of velocity ->", angle)
        print("Initial location of cannon shell ->", (location_x, location_y))
        print("time step -> ", time_step)
    def calculate(self):
        while not self.y[-1] < 0 :
            vx = self.v_x[-1] - self.v_x[-1] * self.v[-1] * self.const * self.dt
            vy = self.v_y[-1] - self.v_y[-1] * self.v[-1] * self.const * self.dt - self.g * self.dt         
            self.v_x.append(vx)
            self.v_y.append(vy)
            x = self.x[-1] + self.v_x[-1] * self.dt
            y = self.y[-1] + self.v_y[-1] * self.dt
            v = math.sqrt(self.v_x[-1] * self.v_x[-1] + self.v_y[-1] * self.v_y[-1])            
            self.x.append(x)
            self.y.append(y)
            self.t.append(self.t[-1] + self.dt)
            self.v.append(v)
        amend_y = -self.y[-2]/self.y[-1]
        amend_x = (self.x[-2]+amend_y*self.x[-1])/(amend_y + 1)        
        self.x.remove(self.x[-1])
        self.y.remove(self.y[-1])
        self.x.append(amend_x)
        self.y.append(0)
    def show_results(self):
        pl.plot(self.x, self.y, 'g', label='The trajectory of the cannon with wind drag')
        pl.xlim(0.0, 60000.0)
        pl.ylim(0.0, 20000.0)
        pl.xlabel('x ($m$)')
        pl.ylabel('y ($m$)')
        pl.legend(loc='best', shadow=True)
        pl.show()
    def store_results(self):
        myfile = open('flying_cannon', 'w')
        for i in range(len(self.t)):
            print(self.t[i],(self.x[i],self.y[i]), file = myfile)
        myfile.close()

a = flying_cannon()
a.calculate()
a.show_results()
a.store_results()

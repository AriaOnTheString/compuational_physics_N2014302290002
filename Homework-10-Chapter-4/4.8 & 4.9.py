import pylab as pl
import math
import numpy as np

class trajectory_of_planet : 
    def __init__(self, beta,x0 ,vy0) : 
        self.x = [x0]
        self.y = [0]
        self.vx = [0]
        self.vy = [vy0]
        self.t = [0]
        self.dt = 0.002
        self.beta = beta
    def calculate(self): 
        while self.t[-1]<=20:
            r=np.sqrt((self.x[-1])**2+(self.y[-1])**2)
            ox=-4*math.pi*math.pi*self.x[-1]/(r**self.beta)
            oy=-4*math.pi*math.pi*self.y[-1]/(r**self.beta)
            self.vx.append(self.vx[-1]+ox*self.dt)
            self.vy.append(self.vy[-1]+oy*self.dt)
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
        return self.x,self.y
    def plot(self):
        
        pl.plot(self.x, self.y)        
        pl.xlabel('x(AU)')
        pl.ylabel('y(AU)')

    def peroid(self):
        rt = []        
        for i in range(len(self.x)):
            if self.x[i-1] < self.x[i] and self.x[i] > self.x[i+1]:
                rt.append(self.t[i-1])
        return rt[1]
                
pl.subplot(1,2,1)
a = trajectory_of_planet(2,1,3*math.pi)
a.calculate()
a.plot()
pl.title('$\\beta = 2, v_y(0)=3\pi$')

pl.subplot(1,2,2)
a = trajectory_of_planet(3,1,3*math.pi)
a.calculate()
a.plot()
pl.title('$\\beta = 3, v_y(0)=3\pi$')
pl.show()
print(a.peroid())

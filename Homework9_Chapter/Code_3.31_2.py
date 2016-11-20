import pylab as pl
import math
import numpy as np

class the_billiaed_problem :
    def __init__(self, x_0, y_0, vx_0, vy_0):
        self.dt = 0.01
        self.x = [x_0]
        self.y = [y_0]
        self.vx = [vx_0]
        self.vy = [vy_0]
        self.T = 600
        self.t = [0]
    def calculation(self):
        while self.t[-1] <= self.T:
            dx = self.dt*self.vx[-1]
            dy = self.dt*self.vy[-1]
            self.x.append(self.x[-1]+dx)
            self.y.append(self.y[-1]+dy)
            self.vx.append(self.vx[-1])            
            self.vy.append(self.vy[-1])            
            self.t.append(self.t[-1]+self.dt)
            if  self.x[-1] < -10:
                self.x[-1],self.y[-1] = self.approximation('x>-1.0',self.x[-2], self.y[-2], self.vx[-1], self.vy[-1])
                self.vx[-1] = - self.vx[-1]
            elif self.x[-1] > 10:
                 self.x[-1],self.y[-1] = self.approximation('x<1.0',self.x[-2], self.y[-2], self.vx[-1], self.vy[-1])
                 self.vx[-1] = - self.vx[-1]
            elif self.y[-1] < -10:
                 self.x[-1],self.y[-1] = self.approximation('y>-1.0',self.x[-2], self.y[-2], self.vx[-1], self.vy[-1])
                 self.vy[-1] = -self.vy[-1]
            elif self.y[-1] > 10:
                 self.x[-1],self.y[-1] = self.approximation('y<1.0',self.x[-2], self.y[-2], self.vx[-2], self.vy[-2])
                 self.vy[-1] = -self.vy[-1] 
            elif self.x[-1]**2+self.y[-1]**2 < 25.0:
                 self.x[-1],self.y[-1] = self.approximation('x**2+y**2 > 25',self.x[-2], self.y[-2], self.vx[-2], self.vy[-2])
                 self.vx[-1],self.vy[-1] = self.reflection(self.x[-1], self.y[-1], self.vx[-2], self.vy[-2])


    def approximation(self,condition,x,y,vx,vy):
        vxa = vx/100.0
        vya = vy/100.0
        while eval(condition):
            x = x + vxa*self.dt
            y = y + vya*self.dt
        return x-vxa*self.dt,y-vya*self.dt
        
    def reflection(self,x,y,vx,vy):
        module = np.sqrt(x**2+y**2)  ### normalization
        x = x/module
        y = y/module
        v = np.sqrt(vx**2+vy**2)
        cos1 = (vx*x+vy*y)/v
        cos2 = (vx*y-vy*x)/v
        vt = -v*cos1
        vc = v*cos2 
        vx_n = vt*x+vc*y
        vy_n = vt*y-vc*x
        return vx_n,vy_n

    def plot1(self):
        pl.figure(figsize = (10,10))
        pl.plot(self.x , self.y)
        pl.xlabel('x $(m)$')
        pl.ylabel('y $(m)$')
        pl.title('Trajectory of a billiard on a square table')
        
    def plot2(self):
        p_x = []
        p_vx = []
        for i in range(len(self.x)):
            if (abs(self.y[i] - 0)<0.001):
                p_vx.append(self.vx[i])
                p_x.append(self.x[i])
        pl.plot(p_x, p_vx, '.')
        pl.xlabel('x $(m)$')
        pl.ylabel('vx $(m/s)$')
        pl.title('Corresponding Poincare section')
        
    def plot_boundary(self):
        theta = 0
        x = []
        y = []
        while theta < np.pi:
            x.append(5*np.cos(theta))
            y.append(5*np.sin(theta))
            theta+= 0.01
        pl.plot(x,y,'g.')
        while theta > np.pi and theta< 2*np.pi:
            x.append(5*np.cos(theta))
            y.append(5*np.sin(theta))
            theta+= 0.01
        pl.plot(x,y,'g.')
        
a = the_billiaed_problem(6, 6, 1,0.6 )
a.calculation()
a.plot1()
a.plot_boundary()
pl.show()
a.plot2()
pl.show()

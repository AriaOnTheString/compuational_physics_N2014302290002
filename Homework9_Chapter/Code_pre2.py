import pylab as pl
import math
import numpy as np

class the_billiaed_problem :
    def __init__(self, x_0, y_0, vx_0, vy_0):
        self.dt = 0.01
        self.alpha = 0.01
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
            self.vx.append(self.vx[-1])            
            self.vy.append(self.vy[-1])
            self.x.append(self.x[-1]+dx)
            self.y.append(self.y[-1]+dy)
            self.t.append(self.t[-1]+self.dt)
            if  self.x[-1] < -1.0:
                self.x[-1],self.y[-1] = self.approximation('x>-1.0',self.x[-2], self.y[-2], self.vx[-1], self.vy[-1])
                self.vx[-1] = - self.vx[-1]
            elif self.x[-1] > 1.0:
                 self.x[-1],self.y[-1] = self.approximation('x<1.0',self.x[-2], self.y[-2], self.vx[-1], self.vy[-1])
                 self.vx[-1] = - self.vx[-1]
            elif self.y[-1] < -1.0:
                 self.x[-1],self.y[-1] = self.approximation('y>-1.0',self.x[-2], self.y[-2], self.vx[-1], self.vy[-1])
                 self.vy[-1] = -self.vy[-1]
            elif self.y[-1] > 1.0:
                 self.x[-1],self.y[-1] = self.approximation('y<1.0',self.x[-2], self.y[-2], self.vx[-2], self.vy[-2])
                 self.vy[-1] = -self.vy[-1] 
            else:
                 pass
            self.t.append(self.t[-1] + self.dt)

    def approximation(self,condition,x,y,vx,vy):
        vxa = vx/100.0
        vya = vy/100.0
        while eval(condition):
            x = x + vxa*self.dt
            y = y + vya*self.dt
        return x-vxa*self.dt,y-vya*self.dt

    def plot1(self):
        pl.plot(self.x , self.y)
        pl.xlabel('x $(m)$')
        pl.ylabel('y $(m)$')
        pl.xlim(-1,1)
        pl.ylim(-1,1)
        pl.title('Trajectory of a billiard on a square table')
        
    def plot2(self):
        pl.plot(self.x, self.vx, '.')
        pl.xlabel('x $(m)$')
        pl.ylabel('vx $(m/s)$')
        pl.xlim(-1,1)
        pl.ylim(-0.4,0.4)
        pl.title('Corresponding Poincare section')
        
a = the_billiaed_problem(0.2, 0, 0.3141,0.2718 )
a.calculation()
a.plot1()
pl.show()
a.plot2()
pl.show()

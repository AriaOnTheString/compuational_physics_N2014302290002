import pylab as pl
import math
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

class lorenz_model:
    def __init__(self, r):
        self.dt = 0.0001
        self.r = r
        self.segma = 10
        self.b = 8/3
        self.x = [1]
        self.y = [0]
        self.z = [0]
        self.vx = [0]
        self.vy = [0]
        self.vz = [0]
        self.T = 50
        self.t = [0]
    def calculation(self):
        while self.t[-1] <= self.T:
            dx = self.dt*self.segma*(self.y[-1]-self.x[-1])
            dy = self.dt*(-self.x[-1]*self.z[-1]+self.r*self.x[-1]-self.y[-1])
            dz = self.dt*(self.x[-1]*self.y[-1]-self.b*self.z[-1])
            self.x.append(self.x[-1]+dx)
            self.y.append(self.y[-1]+dy)
            self.z.append(self.z[-1]+dz)
            self.t.append(self.t[-1]+self.dt)
    def plot1(self):
        pl.plot(self.t , self.z)
        pl.xlabel('time $(s)$')
        pl.ylabel('z $(m)$')
        pl.title('Lorenz model z versus time')
    def plot2(self):
        w=plt.subplot(111,projection='3d')
        plt.plot(self.x,self.y,self.z)
        w.set_xlabel('x $(m)$')
        w.set_ylabel('y $(m)$')
        w.set_zlabel('z $(m)$')
        plt.title('Trajectory of the Lorenz model')

a = lorenz_model(25)
a.calculation()
a.plot1()
pl.show()
a.plot2()
plt.show()

a = lorenz_model(25)
a.calculation()
a.plot1()
a = lorenz_model(10)
a.calculation()
a.plot1()
a = lorenz_model(5)
a.calculation()
a.plot1()
pl.show()

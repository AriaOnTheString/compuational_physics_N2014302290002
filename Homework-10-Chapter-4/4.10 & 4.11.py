import pylab as pl
import math
import numpy as np

class trajectory_of_planet : 
    def __init__(self, e) : 
        self.x = [0.47]
        self.y = [0]
        self.vx = [0]
        vy0=2*math.pi*math.sqrt((1-e)/(0.47*(1+e)))
        self.vy = [vy0]
        self.t = [0]
        self.dt = 0.00001
        self.alpha = 0.000000011
        self.r=[0.47]
        self.the=[0]
        self.tmax=[0]
        self.angle=[0]
    def calculate(self): 
        while self.t[-1]<=20:
            r=np.sqrt((self.x[-1])**2+(self.y[-1])**2)
            ox=-4*math.pi*math.pi*self.x[-1]/(r**3)-4*self.alpha*math.pi*math.pi*(self.x[-1])/(r**5)
            oy=-4*math.pi*math.pi*self.y[-1]/(r**3)-4*self.alpha*math.pi*math.pi*(self.y[-1])/(r**5)
            self.vx.append(self.vx[-1]+ox*self.dt)
            self.vy.append(self.vy[-1]+oy*self.dt)
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
            if self.x[-1]>=0 and self.y[-1]>=0:
                theta=np.arctan(self.y[-1]/self.x[-1])
            if self.x[-1]<=0 and self.y[-1]>=0:
                theta=math.pi+np.arctan(self.y[-1]/self.x[-1])
            if self.x[-1]<=0 and self.y[-1]<=0:
                theta=math.pi+np.arctan(self.y[-1]/self.x[-1])
            if self.x[-1]>=0 and self.y[-1]<=0:
                theta=2*math.pi+np.arctan(self.y[-1]/self.x[-1])
            self.r.append(r)
            self.angle.append(theta)
        for i in range(len(self.r)):
            if i!=0 and i!=len(self.r)-1 and self.r[i]>self.r[i-1] and self.r[i]>self.r[i+1]:
                self.the.append(self.angle[i])
                self.tmax.append(self.t[i])
        print(self.the)
        print(self.tmax)        
        velo=float((self.the[1]-self.the[0])/(self.tmax[1]-self.tmax[0])) 
        return velo


x=list(np.linspace(0.05,0.9,40))
y=[]
for i in x:
    a=trajectory_of_planet(i)    
    y.append(360*180*a.calculate()/math.pi)
pl.plot(x,y)
pl.xlim(0.05,0.95)
pl.title('precession velocity versus eccentricities')
pl.xlabel('eccentricity')
pl.ylabel('precession velocity(arc/yr)')
pl.show()

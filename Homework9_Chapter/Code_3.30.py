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
        self.T = 60
        self.t = [0]
    def calculation(self, alpha):
        while self.t[-1] <= self.T:
            dx = self.dt*self.vx[-1]
            dy = self.dt*self.vy[-1]
            self.x.append(self.x[-1]+dx)
            self.y.append(self.y[-1]+dy)
            self.vx.append(self.vx[-1])            
            self.vy.append(self.vy[-1])            
            self.t.append(self.t[-1]+self.dt)
            self.alpha=alpha
            if (np.sqrt( self.x[-1]**2+(self.y[-1]-self.alpha)**2 ) > 1.0) and self.y[-1] > self.alpha:
                self.x[-1],self.y[-1] = self.approximation('np.sqrt(x**2+(y-self.alpha)**2) < 1.0',self.x[-2], self.y[-2], self.vx[-1], self.vy[-1])
                self.vx[-1],self.vy[-1] = self.reflection1(self.x[-1],self.y[-1],self.vx[-1], self.vy[-1])
            elif (np.sqrt( self.x[-1]**2+(self.y[-1]+self.alpha)**2 ) > 1.0) and self.y[-1]<-self.alpha:
                self.x[-1],self.y[-1] = self.approximation('np.sqrt(x**2+(y+self.alpha)**2) < 1.0',self.x[-2], self.y[-2], self.vx[-1], self.vy[-1])
                self.vx[-1],self.vy[-1] = self.reflection2(self.x[-1],self.y[-1],self.vx[-1], self.vy[-1])
            elif (self.x[-1] < -1.0) and self.y[-1]>-self.alpha and self.y[-1]<self.alpha:
                self.x[-1],self.y[-1] = self.approximation('x>-1.0',self.x[-2], self.y[-2], self.vx[-2], self.vy[-2])
                self.vx[-1] = - self.vx[-1]
            elif (self.x[-1] > 1.0) and self.y[-1]>-self.alpha and self.y[-1]<self.alpha:
                self.x[-1],self.y[-1] = self.approximation('x<1.0',self.x[-2], self.y[-2], self.vx[-2], self.vy[-2])
                self.vx[-1] = - self.vx[-1]


    def approximation(self,condition,x,y,vx,vy):
        vxa = vx/100.0
        vya = vy/100.0
        while eval(condition):
            x = x + vxa*self.dt
            y = y + vya*self.dt
        return x-vxa*self.dt,y-vya*self.dt
        
    def reflection1(self, x, y, vx, vy):
        x = x/np.sqrt(x**2+(y-self.alpha)**2)
        y = (y-self.alpha)/np.sqrt(x**2+(y-self.alpha)**2)+self.alpha
        vxa = vx/np.sqrt(vx**2+vy**2)
        vya = vy/np.sqrt(vx**2+vy**2)
        cosda = x*vxa + (y-self.alpha)*vya
        sinda = (y-self.alpha)*vxa - x*vya
        vv = -np.sqrt(vx**2+vy**2)*cosda
        vh = np.sqrt(vx**2+vy**2)*sinda
        vxr = vv*x + vh*(y-self.alpha)
        vyr = vv*(y-self.alpha) - vh*x
        return vxr, vyr

    def reflection2(self, x, y, vx, vy):
        x = x/np.sqrt(x**2+(y+self.alpha)**2)
        y = (y+self.alpha)/np.sqrt(x**2+(y+self.alpha)**2)-self.alpha
        vxa = vx/np.sqrt(vx**2+vy**2)
        vya = vy/np.sqrt(vx**2+vy**2)
        cosda = x*vxa + (y+self.alpha)*vya
        sinda = (y+self.alpha)*vxa - x*vya
        vv = -np.sqrt(vx**2+vy**2)*cosda
        vh = np.sqrt(vx**2+vy**2)*sinda
        vxr = vv*x + vh*(y+self.alpha)
        vyr = vv*(y+self.alpha) - vh*x
        return vxr, vyr

    def plot1(self):
        pl.figure(figsize = (8,8))
        pl.plot(self.x , self.y)
        pl.xlabel('x $(m)$')
        pl.ylabel('y $(m)$')
        pl.xlim(-1,1)
        pl.ylim(-1,1)
        pl.title('Trajectory of a billiard on a square table')
        
    def plot2(self):
        pl.figure(figsize = (8,8))
        p_x = []
        p_vx = []
        for i in range(len(self.x)):
            if (abs(self.y[i] - 0)<0.001):
                p_vx.append(self.vx[i])
                p_x.append(self.x[i])
        pl.plot(p_x, p_vx, '.')
        pl.xlabel('x $(m)$')
        pl.ylabel('vx $(m/s)$')
        pl.xlim(-1,1)
        pl.ylim(-1.5,1.5)
        pl.title('Corresponding Poincare section')
        
a = the_billiaed_problem(0, 0, 1,0.6 )
a.calculation(0.01)
b = the_billiaed_problem(0.00001, 0, 1,0.6 )
b.calculation(0.01)
delta=[]
for i in range(len(a.x)):
    delta.append(np.sqrt((b.x[i]-a.x[i])**2+(b.y[i]-a.y[i])**2))
pl.semilogy(a.t,delta)
pl.xlabel('time $s$')
pl.ylabel('separation $m$')
pl.title('$\\alpha=0.01$')
pl.show()

a = the_billiaed_problem(0, 0, 1,0.6 )
a.calculation(0.1)
b = the_billiaed_problem(0.00001, 0, 1,0.6 )
b.calculation(0.1)
delta=[]
for i in range(len(a.x)):
    delta.append(np.sqrt((b.x[i]-a.x[i])**2+(b.y[i]-a.y[i])**2))
pl.semilogy(a.t,delta)
pl.xlabel('time $s$')
pl.ylabel('separation $m$')
pl.title('$\\alpha=0.1$')
pl.show()

a = the_billiaed_problem(0, 0, 1,0.6 )
a.calculation(0.001)
b = the_billiaed_problem(0.00001, 0, 1,0.6 )
b.calculation(0.001)
delta=[]
for i in range(len(a.x)):
    delta.append(np.sqrt((b.x[i]-a.x[i])**2+(b.y[i]-a.y[i])**2))
pl.semilogy(a.t,delta)
pl.xlabel('time $s$')
pl.ylabel('separation $m$')
pl.title('$\\alpha=0.001$')
pl.show()

a = the_billiaed_problem(0, 0, 1,0.6 )
a.calculation(0)
b = the_billiaed_problem(0.00001, 0, 1,0.6 )
b.calculation(0)
delta=[]
for i in range(len(a.x)):
    delta.append(np.sqrt((b.x[i]-a.x[i])**2+(b.y[i]-a.y[i])**2))
pl.semilogy(a.t,delta)
pl.xlabel('time $s$')
pl.ylabel('separation $m$')
pl.title('$\\alpha=0$')
pl.show()

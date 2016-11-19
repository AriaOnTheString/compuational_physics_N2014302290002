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
                self.x[-1],self.y[-1] = self.approximation('x<1.0',self.x[-2], self.y[-2], self.vx[-1], self.vy[-1])
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

    def plot1(self,plot):

        plot.plot(self.x , self.y)
        pl.xlabel('x $(m)$')
        pl.ylabel('y $(m)$')
        pl.xlim(-1,1)
        pl.ylim(-1,1)

        
    def plot2(self,plot):
        p_x = []
        p_vx = []
        for i in range(len(self.x)):
            if (abs(self.y[i] - 0)<0.001):
                p_vx.append(self.vx[i])
                p_x.append(self.x[i])
        plot.plot(p_x, p_vx, '.')
        pl.xlabel('x $(m)$')
        pl.ylabel('vx $(m/s)$')
        pl.xlim(-1,1)
        pl.ylim(-1.5,1.5)

        


sub1=pl.subplot(221)
a = the_billiaed_problem(0.2, 0, 1,0.6 )
a.calculation(0)
sub1.set_title('$\\alpha=0$')
a.plot1(sub1)


sub2=pl.subplot(222)
a = the_billiaed_problem(0.2, 0, 1,0.6 )
a.calculation(0.001)
sub2.set_title('$\\alpha=0.001$')
a.plot1(sub2)

sub3=pl.subplot(223)
a = the_billiaed_problem(0.2, 0, 1,0.6 )
a.calculation(0.01)
sub3.set_title('$\\alpha=0.01$')
a.plot1(sub3)


sub4=pl.subplot(224)
a = the_billiaed_problem(0.2, 0, 1,0.6 )
a.calculation(0.1)
sub4.set_title('$\\alpha=0.1$')
a.plot1(sub4)

pl.show()

sub5=pl.subplot(221)
a = the_billiaed_problem(0.2, 0, 1,0.6 )
a.calculation(0)
sub5.set_title('$\\alpha=0$')
a.plot2(sub5)

sub6=pl.subplot(222)
a = the_billiaed_problem(0.2, 0, 1,0.6 )
a.calculation(0.001)
sub6.set_title('$\\alpha=0.001$')
a.plot2(sub6)

sub7=pl.subplot(223)
a = the_billiaed_problem(0.2, 0, 1,0.6 )
a.calculation(0.01)
sub7.set_title('$\\alpha=0.01$')
a.plot2(sub7)

sub8=pl.subplot(224)
a = the_billiaed_problem(0.2, 0, 1,0.6 )
a.calculation(0.1)
sub2.set_title('$\\alpha=0.1$')
a.plot2(sub8)

pl.show()

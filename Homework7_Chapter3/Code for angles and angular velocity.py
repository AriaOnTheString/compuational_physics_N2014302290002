import pylab as pl
import math

class pendulums(): 
    def __init__(self,  length, time_step=0.001):        
        self.l=length
        self.dt=time_step
        self.t=[0]
    def calculation(self,  friction,initial_angle, initial_speed,magnitude_of_force, frequency_of_forth, total_time):
        self.angle=[initial_angle]
        self.q=friction
        self.FD=magnitude_of_force
        self.omegaD=frequency_of_forth
        self.T=total_time
        self.omega=[initial_speed]
        while self.t[-1] <= self.T: 
            self.omega.append(self.omega[-1]-9.8*math.sin(self.angle[-1])*self.dt/self.l-self.q*self.omega[-1]*self.dt+self.FD*math.sin(self.omegaD*self.t[-1])*self.dt) 
            self.angle.append(self.angle[-1]+self.omega[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
        return [self.t[-1],self.angle[-1]]
        
    def plotting(self, discription): 
        pl.plot(self.t,self.angle, label= discription)                   
        pl.xlabel('Time ($s$)')
        pl.ylabel('Angle ($rad$)')
        pl.legend(loc='best')
    def plottingv(self, discription): 
        pl.plot(self.t, self.omega, label= discription)
        pl.xlabel('Time ($s$)')
        pl.ylabel('Angular velocity ($rad/s$)')
    def adjust(self):
        self.adjust = []
        for i in range(len(self.angle)):
            if self.angle[i] > math.pi:
                a = self.angle[i] - 2*math.pi
            if self.angle[i] < -math.pi:
                a = self.angle[i] + 2*math.pi
            if self.angle[i] <= math.pi and self.angle[i] >= -math.pi:
                a = self.angle[i]
            self.adjust.append(a)
a=pendulums(9.8)
a.calculation(0.5,0.0000,0,1.2,2/3,150)
a.plotting('Initial angle = 0.0000rad')
b=pendulums(9.8)
b.calculation(0.5,0.0001,0,1.2,2/3,150)
b.plotting('Initial angle = 0.0001rad')
pl.show()

delta=[]
for i in range(len(a.angle)):
    delta.append(math.log((abs(a.angle[i]-b.angle[i])),math.e))
pl.plot(a.t,delta, label='Difference of angles')
pl.xlabel('Time ($s$)')
pl.ylabel('Angle ($1e^y rad$)')
pl.legend(loc='best')
pl.show()

pl.subplot(3,2,1)#
a=pendulums(9.8)
a.calculation(0.5,0.2,0,0,2/3,60)
a.plotting('Forced pendulum')
pl.text(40,0.15,r'$F_D=0$')
pl.title(r'Fig1.1 $\theta$ versus time with different $F_D$')
pl.xlim(0,)
pl.subplot(3,2,3)#
a=pendulums(9.8)
a.calculation(0.5,0.2,0,0.5,2/3,60)
a.plotting('')
pl.text(40,0.5,r'$F_D=0.5$')
pl.xlim(0,)
pl.ylabel(r'$\theta$(radius)',fontsize=15)
pl.subplot(3,2,5)#
a=pendulums(9.8)
a.calculation(0.5,0.2,0,1.2,2/3,60)
a.plotting('Forced pendulum')
pl.text(40,-2,r'$F_D=1.2$')
pl.xlim(0,)
pl.xlabel('time(seconds)',fontsize=15)
pl.subplot(3,2,2)#
a=pendulums(9.8)
a.calculation(0.5,0.2,0,0,2/3,60)
a.plottingv('Forced pendulum')
pl.text(40,0.05,r'$F_D=0$')
pl.title(r'Fig.1.2 $\omega$ versus time with different $F_D$')
pl.xlim(0,)
pl.subplot(3,2,4)#
a=pendulums(9.8)
a.calculation(0.5,0.2,0,0.5,2/3,60)
a.plottingv('Forced pendulum')
pl.text(40,0.5,r'$F_D=0.5$')
pl.xlim(0,)
pl.ylabel(r'$\omega$(radius/second)',fontsize=15)
pl.subplot(3,2,6)#
a=pendulums(9.8)
a.calculation(0.5,0.2,0,1.2,2/3,60)
a.plottingv('Forced pendulum')
pl.text(40,1.0,r'$F_D=1.2$')
pl.xlim(0,)
pl.xlabel('time(seconds)',fontsize=15)
pl.show()

pl.subplot(2,1,1)
a=pendulums(9.8)
a.calculation(0.5,0.2,0,1.2,2/3,60)
a.adjust()
pl.plot(a.t, a.adjust, label='Forced pendulum')
pl.text(30,1.0,'adjusted'+'\n$F_D=1.2$')
pl.title(r'Fig.1.3 $\theta$ versus time')
pl.xlim(0,)
pl.ylabel(r'$\theta$(radius)',fontsize=15)
pl.subplot(2,1,2)
a=pendulums(9.8)
a.calculation(0.5,0.2,0,1.2,2/3,60)
a.plotting('Forced pendulum')
pl.text(40,-2,'unadjusted'+'\n$F_D=1.2$')
pl.xlim(0,)
pl.xlabel('time(seconds)',fontsize=15)
pl.ylabel(r'$\theta$(radius)',fontsize=15)
pl.show()

a=pendulums(9.8)
a.calculation(0.5,0.0000,0,1.2,2/3,150)
a.plotting('Damping factor = 0.5')
b=pendulums(9.8)
b.calculation(0.51,0.0000,0,1.2,2/3,150)
b.plotting('Damping factor = 0.51')
c=pendulums(9.8)
c.calculation(0.49,0.0000,0,1.2,2/3,150)
c.plotting('Damping factor = 0.49')
pl.show()

delta1=[]
for i in range(len(a.angle)):
    delta1.append(a.angle[i]-b.angle[i])
pl.plot(a.t,delta1, label='Difference of angles of $q=0.5$ and $q=0.51$')
pl.xlabel('Time ($s$)')
pl.ylabel('Angle ($rad$)')
pl.legend(loc='best')
pl.show()

delta2=[]
for i in range(len(a.angle)):
    delta2.append(a.angle[i]-c.angle[i])
pl.plot(a.t,delta2, label='Difference of angles of $q=0.5$ and $q=0.49$')
pl.xlabel('Time ($s$)')
pl.ylabel('Angle ($rad$)')
pl.legend(loc='best')
pl.show()

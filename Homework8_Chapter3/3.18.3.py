import pylab as pl
import math

class pendulums(): 
    def __init__(self,  length, time_step):        
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
            omega=self.omega[-1]-9.8*math.sin(self.angle[-1])*self.dt/self.l-self.q*self.omega[-1]*self.dt+self.FD*math.sin(self.omegaD*self.t[-1])*self.dt            
            self.omega.append(omega) 
            angle=self.angle[-1]+self.omega[-1]*self.dt
            while angle >math.pi:
                angle=angle-math.pi*2
            while angle <-math.pi:
                angle=angle+math.pi*2
            self.angle.append(angle)
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
       
pl.subplot(2,2,1)
a=pendulums(9.8, 3*math.pi/1000)
a.calculation(0.5,0.2,0,1.465,2/3, 3*math.pi*2000)
showangle=[]
showomega=[]
for i in range(10000,len(a.t)):
        if ((2/3)*(a.t[i]))%(2*(math.pi))<0.001 :
            showangle.append(a.angle[i])
            showomega.append(a.omega[i])
pl.plot(showangle, showomega,'.',label='$2/3t=2\pi n$')
pl.xlabel('Angle ($rad$)')
pl.ylabel('Angular ($rad/s$)')
pl.xlim(0,3)
pl.ylim(-4,0)
pl.legend(loc='best')

pl.subplot(2,2,2)
a=pendulums(9.8, 3*math.pi/1000)
a.calculation(0.5,0.2,0,1.465,2/3,3*math.pi*2000)
showangle=[]
showomega=[]
for i in range(10000,len(a.t)):
        if ((2/3)*(a.t[i])-math.pi/4)%(2*(math.pi))<0.001 :
            showangle.append(a.angle[i])
            showomega.append(a.omega[i])
pl.plot(showangle, showomega,'.',label='$2/3t=2\pi n+\pi/4$')
pl.xlabel('Angle ($rad$)')
pl.ylabel('Angular ($rad/s$)')
pl.xlim(-2,2)
pl.ylim(-2,0)
pl.legend(loc='best')

pl.subplot(2,2,3)
a=pendulums(9.8, 3*math.pi/1000)
a.calculation(0.5,0.2,0,1.465,2/3,3*math.pi*2000)
showangle=[]
showomega=[]
for i in range(10000,len(a.t)):
        if ((2/3)*(a.t[i])-math.pi/2)%(2*(math.pi))<0.001 :
            showangle.append(a.angle[i])
            showomega.append(a.omega[i])
pl.plot(showangle, showomega,'.',label='$2/3t=2\pi n+\pi/2$')
pl.xlabel('Angle ($rad$)')
pl.ylabel('Angular ($rad/s$)')
pl.xlim(-1,2)
pl.ylim(-2,2)
pl.legend(loc='best')

pl.subplot(2,2,4)
a=pendulums(9.8, 3*math.pi/1000)
a.calculation(0.5,0.2,0,1.465,2/3,3*math.pi*2000)
showangle=[]
showomega=[]
for i in range(10000,len(a.t)):
        if ((2/3)*(a.t[i])-3*math.pi/4)%(2*(math.pi))<0.001 :
            showangle.append(a.angle[i])
            showomega.append(a.omega[i])
pl.plot(showangle, showomega,'.',label='$2/3t=2\pi n+3\pi/4$')
pl.xlabel('Angle ($rad$)')
pl.ylabel('Angular ($rad/s$)')
pl.xlim(0,3)
pl.ylim(-1,2)
pl.legend(loc='best')

pl.show()   

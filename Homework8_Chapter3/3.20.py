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
       
FD=[]
for i in range(1500): 
    FD.append(1.35+0.0001*i)
    a=pendulums(9.8, 3*math.pi/1000)
    a.calculation(0.5,0.2,0,FD[-1],2/3, math.pi*1910)
    showangle=[]
    showFD=[]
    for i in range(301,429):
        
        showangle.append(a.angle[i*1000])
        showFD.append(FD[-1])
    pl.plot(showFD, showangle,'.')
pl.xlabel('$F_D$')
pl.ylabel('Angle ($rad$)')
pl.legend(loc='best')

pl.show()   

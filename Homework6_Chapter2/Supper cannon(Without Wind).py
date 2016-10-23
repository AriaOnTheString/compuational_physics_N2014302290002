import pylab as pl
import math
class super_cannon(object) : 
    def __init__(self, aim_x=float(input('coordinate x :')), aim_y=float(input('coordinate y :')),  time_step = 0.01):        
        self.t = [0]
        self.dt = time_step
        self.g = 9.8 
        self.aimx=aim_x
        self.aimy=aim_y
    def calculate(self, angle , velocity,  B_2_over_m, choice_of_correction, T0):
        self.x = [0]
        self.y = [0]
        self.B2overm = B_2_over_m
        self.vdefault=float(velocity)
        self.adefault=float(angle)
        self.v_x = [self.vdefault * math.cos(self.adefault)]
        self.v_y = [self.vdefault * math.sin(self.adefault)]
        self.v = [velocity]
        y0,a,alpha=10**4,6.5*10**(-3),2.5
        if choice_of_correction < 0:            #negative for isothermal approximation
           def rho(height) :
               return math.exp(-height/y0)
        else:                   #non-negative for adiabatic approximation
           def rho(height):
               return (1- a * height / T0) ** alpha
        while self.y[-1] >= self.aimy or self.v_y[-1] >=0 :
              a_x3, a_y3=-self.B2overm* rho(self.y[-1]) *self.v[-1]*self.v_x[-1] , -9.8-self.B2overm* rho(self.y[-1]) *self.v[-1]*self.v_y[-1]
              self.x.append(self.x[-1]+self.v_x[-1]*self.dt)
              self.v_x.append(self.v_x[-1]+a_x3*self.dt)
              self.y.append(self.y[-1]+self.v_y[-1]*self.dt)
              self.v_y.append(self.v_y[-1]+a_y3*self.dt)
              self.t.append(self.t[-1]+self.dt)
              self.v.append((self.v_x[-1]**2+self.v_y[-1]**2)**0.5)
        pl.plot(self.x, self.y, label='The trajectory of the cannon')
        return self.x[-1]
    def scan_angle(self):
        d = [0]        
        test_angle = [0*1*3.1415926/180]
        for i in range(85):
            test_angle.append((90-i)*1*math.pi/180)
            d.append(self.calculate(test_angle[-1], 6000, 4*10**(-5), -1, 300))
            if d[-1]-d[-2] <= 0 : 
                break
        pl.xlabel('Horizon Distance x ($m$)')        
        pl.ylabel('Vertical Distance y ($m$)')
        pl.text(1000000,600000,'Without Wind')
        pl.title('The process of finding the proper initial angle')
        pl.show()
        print(test_angle[-2]*180/3.1415926)
        return test_angle[-2]
    def scan_velocity(self): 
        x = [0]
        test_velocity = [500]
        copy=self.scan_angle()
        for i in range(5500):
            test_velocity.append(500+i)
            x.append(self.calculate(copy, test_velocity[-1], 4*10**(-5), -1, 300))
            if x[-1]-self.aimx >=0 :
                break
        pl.xlabel('Horizon Distance x ($m$)')
        pl.ylabel('Vertical Distance y ($m$)')
        pl.text(95000,5000,'Without Wind')        
        pl.title('The process of finding the proper initial velocity')
        pl.show()        
        print(test_velocity[-2])
        return test_velocity[-2]
    def plotting(self): 
        pl.plot(self.x, self.y, label='The trajectory of the cannon(300K)')
        pl.xlim(0.0,)
        pl.ylim(0.0,)
        pl.xlabel('Horizon Distance x ($m$)')
        pl.ylabel('Vertical Distance y ($m$)')
        pl.legend(loc='best', shadow=True)
        pl.show()
        
a=super_cannon()
t=a.scan_angle()
v=a.scan_velocity()
a.calculate(t,v,4*10**(-5), -1, 300)
a.plotting()

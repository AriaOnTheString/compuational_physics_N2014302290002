class flying_cannon:
    """
    Calculation of the trajectory of the cannon
    Home work of the second chapter done by He Yijun
    Question 2.7
    """
    def __init__(self,angle = 3.14/4 , velocity = 700,location_x = 0, location_y = 0, time_step = 0.001 , B_over_m = 0.00004, B_over_m_const = 0.00004):
        # unit of time is s ; unit of angle is rad
        self.v_x = [velocity * math.cos(angle)]
        self.v_y = [velocity * math.sin(angle)]
        self.v=[velocity]        
        self.x = [location_x]        
        self.y = [location_y]
        self.v_xno = [velocity * math.cos(angle)]
        self.v_yno = [velocity * math.sin(angle)]
        self.vno =[velocity]        
        self.xno = [location_x]        
        self.yno = [location_y]
        self.t = [0]
        self.dt = time_step
        self.const = [B_over_m * (293/300) ** 2.5]
        self.constno = [B_over_m_const * (273/300) ** 2.5]
        self.g = 9.8
        print("Initial velocity ->", velocity)
        print("Initial angle of velocity ->", angle)
        print("Initial location of cannon shell ->", (location_x, location_y))
        print("time step -> ", time_step)
    def calculate(self):
        while not self.y[-1] < 0 :
            vx = self.v_x[-1] - self.v_x[-1] * self.v[-1] * self.const[-1] * self.dt
            vy = self.v_y[-1] - self.v_y[-1] * self.v[-1] * self.const[-1] * self.dt - self.g * self.dt         
            self.v_x.append(vx)
            self.v_y.append(vy)
            x = self.x[-1] + self.v_x[-1] * self.dt
            y = self.y[-1] + self.v_y[-1] * self.dt
            v = math.sqrt(self.v_x[-1] * self.v_x[-1] + self.v_y[-1] * self.v_y[-1]) 
            c = (1 - 0.0065 * self.y[-1]/300)**(2.5) * self.const[0]
            self.const.append(c)            
            self.x.append(x)
            self.y.append(y)
            self.t.append(self.t[-1] + self.dt)
            self.v.append(v)
        amend_y = -self.y[-2]/self.y[-1]
        amend_x = (self.x[-2]+amend_y*self.x[-1])/(amend_y + 1)        
        self.x.remove(self.x[-1])
        self.y.remove(self.y[-1])
        self.x.append(amend_x)
        self.y.append(0)
    def calculate_c(self):
        while not self.yno[-1] < 0 :
            vxno = self.v_xno[-1] - self.v_xno[-1] * self.vno[-1] * self.constno[-1] * self.dt
            vyno = self.v_yno[-1] - self.v_yno[-1] * self.vno[-1] * self.constno[-1] * self.dt - self.g * self.dt         
            self.v_xno.append(vxno)
            self.v_yno.append(vyno)
            xno = self.xno[-1] + self.v_xno[-1] * self.dt
            yno = self.yno[-1] + self.v_yno[-1] * self.dt
            vno = math.sqrt(self.v_xno[-1] * self.v_xno[-1] + self.v_yno[-1] * self.v_yno[-1])            
            cno = (1 - 0.0065 * self.yno[-1]/300)**(2.5) * self.constno[0]
            self.constno.append(cno)            
            self.xno.append(xno)
            self.yno.append(yno)
            self.t.append(self.t[-1] + self.dt)
            self.vno.append(vno)
        amend_yno = -self.yno[-2]/self.yno[-1]
        amend_xno = (self.xno[-2]+amend_yno*self.xno[-1])/(amend_yno + 1)        
        self.xno.remove(self.xno[-1])
        self.yno.remove(self.yno[-1])
        self.xno.append(amend_xno)
        self.yno.append(0)
    def show_results(self):
        pl.plot(self.x, self.y, 'g', label='The trajectory of the cannon in summer(293K)')
        pl.plot(self.xno, self.yno, 'b', label='The trajectory of the cannon in winter(273K)')
        pl.xlim(0.0, 30000.0)
        pl.ylim(0.0, 10000.0)
        pl.xlabel('x ($m$)')
        pl.ylabel('y ($m$)')
        pl.legend(loc='best', shadow=True)
        pl.show()
    def store_results(self):
        myfile = open('flying_cannon', 'w')
        for i in range(len(self.t)):
            print(self.t[i],(self.x[i],self.y[i]),(self.xno[i],self.yno[i]), file = myfile)
        myfile.close()

a = flying_cannon()
a.calculate()
a.calculate_c()
a.show_results()
a.store_results()

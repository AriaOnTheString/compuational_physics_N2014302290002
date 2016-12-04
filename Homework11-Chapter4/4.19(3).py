import math
import pylab as pl
class Hyperion:
    def __init__(self, initial_speed, initial_theta):
        self.GM = 4 * math.pi ** 2
        self.xc = [1]
        self.yc = [0]
        self.vx = [0]
        self.vy = [initial_speed]
        self.T = 10
        self.dt = 0.0001
        self.N = int(self.T / self.dt)
        self.theta = [initial_theta]
        self.omega = [0]
        
    def Calculation(self):
        self.t = [0]
        self.rc = [1]
        for i in range(self.N):
            self.vx.append(self.vx[i] - self.GM * self.xc[i] / math.pow(self.rc[i], 3) * self.dt)
            self.vy.append(self.vy[i] - self.GM * self.yc[i] / math.pow(self.rc[i], 3) * self.dt)
            self.xc.append(self.xc[i] + self.vx[i + 1] * self.dt)
            self.yc.append(self.yc[i] + self.vy[i + 1] * self.dt)
            self.rc.append(math.sqrt(self.xc[i + 1] ** 2 + self.yc[i + 1] ** 2))
            self.omega.append(self.omega[i] - 3 * self.GM * (self.xc[i] * math.sin(self.theta[i]) - self.yc[i] * math.cos(self.theta[i])) * (self.xc[i] * math.cos(self.theta[i]) + self.yc[i] * math.sin(self.theta[i])) / math.pow(self.rc[i], 5) * self.dt)
            self.theta.append(self.theta[i] + self.omega[i + 1] * self.dt)
            while self.theta[i + 1] > math.pi:
                self.theta[i + 1] = self.theta[i + 1] - 2 * math.pi
            while self.theta[i + 1] <= -math.pi:
                self.theta[i + 1] = self.theta[i + 1] + 2 * math.pi
            self.t.append(self.t[i] + self.dt)

    def plot(self):
        pl.figure(figsize = (8, 8))
        pl.plot(self.t,self.theta )

        pl.ylabel('$\\theta$ (radians)')
        pl.xlabel('time (yr)')
        pl.title('Hyperion $\\theta$ versus time')
        pl.text(3.3, 13.5, 'Circular orbit')

A = Hyperion(2 * math.pi, 0)
A.Calculation()

B = Hyperion(2 * math.pi, 0.01)
B.Calculation()
C = []
for i in range(len(B.theta)):
    C.append(B.theta[i]-A.theta[i])
    
pl.semilogy(A.t,C,'.')
pl.ylabel('$\\Delta\\theta$ (radians)')
pl.xlabel('time (yr)')
pl.title('Hyperion $\\Delta\\theta$ versus time')

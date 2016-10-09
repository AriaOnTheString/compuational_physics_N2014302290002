import pylab as pl
class uranium_decay:
    """
    Simulation of radioactive decay
    Home work of the first chapter done by He Yijun
    Question 1.5
    """
    def __init__(self, number_of_nucleiA = 100,number_of_nucleiB = 0,number_of_nucleiC = 100, number_of_nucleiD = 50,number_of_nucleiE = 100,number_of_nucleiF = 30, time_constant = 1, time_of_duration = 5, time_step = 0.05):
        # unit of time is second
        self.n_uraniumA = [number_of_nucleiA]
        self.n_uraniumB = [number_of_nucleiB]        
        self.n_uraniumC = [number_of_nucleiC]        
        self.n_uraniumD = [number_of_nucleiD]
        self.n_uraniumE = [number_of_nucleiE]
        self.n_uraniumF = [number_of_nucleiF]
        self.t = [0]
        self.tau = time_constant
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)
        print("Initial number of nucleiA ->", number_of_nucleiA)
        print("Initial number of nucleiB ->", number_of_nucleiB)
        print("Initial number of nucleiC ->", number_of_nucleiC)
        print("Initial number of nucleiD ->", number_of_nucleiD)
        print("Initial number of nucleiE ->", number_of_nucleiE)
        print("Initial number of nucleiF ->", number_of_nucleiF)
        print("Time constant ->", time_constant)
        print("time step -> ", time_step)
        print("total time -> ", time_of_duration)
    def calculate(self):
        for i in range(self.nsteps):
            tmpA = self.n_uraniumA[i] + self.n_uraniumB[i] / self.tau * self.dt - self.n_uraniumA[i] / self.tau * self.dt
            tmpB = self.n_uraniumB[i] + self.n_uraniumA[i] / self.tau * self.dt - self.n_uraniumB[i] / self.tau * self.dt         
            tmpC = self.n_uraniumC[i] + self.n_uraniumD[i] / self.tau * self.dt - self.n_uraniumC[i] / self.tau * self.dt            
            tmpD = self.n_uraniumD[i] + self.n_uraniumC[i] / self.tau * self.dt - self.n_uraniumD[i] / self.tau * self.dt
            tmpE = self.n_uraniumE[i] + self.n_uraniumF[i] / self.tau * self.dt - self.n_uraniumE[i] / self.tau * self.dt
            tmpF = self.n_uraniumF[i] + self.n_uraniumE[i] / self.tau * self.dt - self.n_uraniumF[i] / self.tau * self.dt
            self.n_uraniumA.append(tmpA)
            self.n_uraniumB.append(tmpB)
            self.n_uraniumC.append(tmpC)
            self.n_uraniumD.append(tmpD)
            self.n_uraniumE.append(tmpE)
            self.n_uraniumF.append(tmpF)            
            self.t.append(self.t[i] + self.dt)
    def show_results(self):
        pl.plot(self.t, self.n_uraniumA, 'g', label='Number of nucleiA & B')
        pl.plot(self.t, self.n_uraniumB, 'g')
        pl.plot(self.t, self.n_uraniumC, 'b', label='Number of nucleiC & D')
        pl.plot(self.t, self.n_uraniumD, 'b')
        pl.plot(self.t, self.n_uraniumE, 'r', label='Number of nucleiE & F')
        pl.plot(self.t, self.n_uraniumF, 'r')
        pl.xlim(0.0, 3.0)
        pl.ylim(0.0, 100.0)
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei')
        pl.legend(loc='best', shadow=True)
        pl.show()
    def store_results(self):
        myfile = open('nuclei_decay_data.txt', 'w')
        for i in range(len(self.t)):
            print(self.t[i], self.n_uraniumA[i], self.n_uraniumB[i], file = myfile)
        myfile.close()

a = uranium_decay()
a.calculate()
a.show_results()
a.store_results()

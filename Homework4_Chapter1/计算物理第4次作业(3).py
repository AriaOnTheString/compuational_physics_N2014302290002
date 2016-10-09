class uranium_decay:
    """
    Simulation of radioactive decay
    Home work of the first chapter done by He Yijun
    Question 1.5
    """
    def __init__(self, number_of_nucleiA = 100,number_of_nucleiB = 0,number_of_nucleiC = 100, number_of_nucleiD = 0, time_constant = 1, time_of_duration = 5, time_step1 = 0.1, time_step2=0.001):
        # unit of time is second
        self.n_uraniumA = [number_of_nucleiA]
        self.n_uraniumB = [number_of_nucleiB]        
        self.n_uraniumC = [number_of_nucleiC]        
        self.n_uraniumD = [number_of_nucleiD]
        self.t1 = [0]
        self.t2 = [0]
        self.tau = time_constant
        self.dt1 = time_step1
        self.dt2 = time_step2
        self.time = time_of_duration
        self.nsteps1 = int(time_of_duration // time_step1 + 1)
        self.nsteps2 = int(time_of_duration // time_step2 + 1)
        print("Initial number of nucleiA ->", number_of_nucleiA)
        print("Initial number of nucleiB ->", number_of_nucleiB)
        print("Time constant ->", time_constant)
        print("time step1 -> ", time_step1)
        print("time step2 -> ", time_step2)
        print("total time -> ", time_of_duration)
    def calculate(self):
        for i in range(self.nsteps1):
            tmpA = self.n_uraniumA[i] + self.n_uraniumB[i] / self.tau * self.dt1 - self.n_uraniumA[i] / self.tau * self.dt1
            tmpB = self.n_uraniumB[i] + self.n_uraniumA[i] / self.tau * self.dt1 - self.n_uraniumB[i] / self.tau * self.dt1
            self.n_uraniumA.append(tmpA)
            self.n_uraniumB.append(tmpB)
            self.t1.append(self.t1[i] + self.dt1)
        for i in range(self.nsteps2):
            tmpC = self.n_uraniumC[i] + self.n_uraniumD[i] / self.tau * self.dt2 - self.n_uraniumC[i] / self.tau * self.dt2            
            tmpD = self.n_uraniumD[i] + self.n_uraniumC[i] / self.tau * self.dt2 - self.n_uraniumD[i] / self.tau * self.dt2
            self.n_uraniumC.append(tmpC)
            self.n_uraniumD.append(tmpD)            
            self.t2.append(self.t2[i] + self.dt2)
    def show_results(self):
        pl.plot(self.t1, self.n_uraniumA, 'g', label='Number of nucleiA & B')
        pl.plot(self.t1, self.n_uraniumB, 'g')
        pl.plot(self.t2, self.n_uraniumC, 'b', label='Number of nucleiC & D')
        pl.plot(self.t2, self.n_uraniumD, 'b')
        pl.xlim(0.0, 3.0)
        pl.ylim(0.0, 100.0)
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei')
        pl.legend(loc='best', shadow=True)
        pl.show()
    def store_results(self):
        myfile = open('nuclei_decay_data.txt', 'w')
        for i in range(len(self.t1)):
            print(self.t1[i],self.t2[i], self.n_uraniumA[i], self.n_uraniumB[i], file = myfile)
        myfile.close()
a = uranium_decay()
a.calculate()
a.show_results()
a.store_results()

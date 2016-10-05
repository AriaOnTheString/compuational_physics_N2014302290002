import pylab as pl
class uranium_decay:
    """
    Simulation of radioactive decay
    Home work of the first chapter done by He Yijun
    Question 1.5
    """
    def __init__(self, number_of_nucleiA = 100,number_of_nucleiB = 0, time_constant = 1, time_of_duration = 5, time_step = 0.05):
        # unit of time is second
        self.n_uraniumA = [number_of_nucleiA]
        self.n_uraniumB = [number_of_nucleiB]        
        self.t = [0]
        self.tau = time_constant
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)
        print("Initial number of nucleiA ->", number_of_nucleiA)
        print("Initial number of nucleiB ->", number_of_nucleiB)
        print("Time constant ->", time_constant)
        print("time step -> ", time_step)
        print("total time -> ", time_of_duration)
    def calculate(self):
        for i in range(self.nsteps):
            tmpA = self.n_uraniumA[i] + self.n_uraniumB[i] / self.tau * self.dt - self.n_uraniumA[i] / self.tau * self.dt
            tmpB = self.n_uraniumB[i] + self.n_uraniumA[i] / self.tau * self.dt - self.n_uraniumB[i] / self.tau * self.dt         
            self.n_uraniumA.append(tmpA)
            self.n_uraniumB.append(tmpB)            
            self.t.append(self.t[i] + self.dt)
    def show_results(self):
        pl.plot(self.t, self.n_uraniumA)
        pl.plot(self.t, self.n_uraniumB)
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei')
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

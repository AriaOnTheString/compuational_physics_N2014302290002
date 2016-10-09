import pylab as pl
import math
class uranium_decay:
    def __init__(self, number_of_nucleiA , number_of_nucleiB , time_constant , time_of_duration , time_step ):
        self.n_nucleiA=[number_of_nucleiA]
        self.n_nucleiB=[number_of_nucleiB]
        self.nA_true=[number_of_nucleiA]
        self.nB_true=[number_of_nucleiB]
        self.n=number_of_nucleiA+number_of_nucleiB
        self.t = [0]
        self.tau=time_constant
        self.dt=time_step
        self.time=time_of_duration
        self.nsteps = int(time_of_duration//time_step + 1)
        print("Initial number of nucleiA ->", number_of_nucleiA)
        print("Initial number of nucleiB ->", number_of_nucleiB)
        print("Time constant ->", time_constant)
        print("Time step ->", time_step)
        print("Total time ->", time_of_duration)
    def calculate(self):
        for i in range(self.nsteps):
            tmpA= self.n_nucleiA[i] + self.n_nucleiB[i] / self.tau * self.dt - self.n_nucleiA[i] / self.tau * self.dt
            tmpB= self.n_nucleiB[i] + self. n_nucleiA[i]/self.tau * self.dt - self.n_nucleiB[i]/ self.tau * self.dt
            self.n_nucleiA.append(tmpA)
            self.n_nucleiB.append(tmpB)
            self.t.append(self.t[i] +self.dt)
            tempA_true= self.n / 2 -math.exp(-2*self.t[i+1]/self.tau) * (self.n - 2*self.n_nucleiA[0])/2
            tempB_true= self.n-tempA_true
            self.nA_true.append(tempA_true)
            self.nB_true.append(tempB_true)
    def show_results(self):
        pl.plot(self.t, self.n_nucleiA, 'r--', label='Number of NucleiA')
        pl.plot(self.t, self.n_nucleiB, 'r--', label='Number of NucleiB')
        pl.plot(self.t, self.nA_true, 'g', label='Exact Number of NucleiA')
        pl.plot(self.t, self.nB_true, 'g', label='Exact Number of NucleiB')
        pl.xlabel('time($s$)')
        pl.ylabel('Number of Nuclei')
        pl.xlim(0.0, 3.0)
        pl.ylim(0.0, 100.0)
        pl.legend(loc='upper rigt', shadow=True)
        pl.show()
    def store_results(self):
        myfile = open('nuclei_decay_data.txt', 'w')
        for i in range(len(self.t)):
            print(self.t[i], self.n_uraniumA[i], self.n_uraniumB[i], file = myfile)
        myfile.close()

nA=int(input("number of nucleiA = "))
nB=int(input("number of nucleiB = "))
x=int(input("time_constant="))
y=int(input("time_of_duration="))
z=float(input("time_step="))

a=uranium_decay(nA, nB, x, y, z)
a.calculate()
a.show_results()
a.store_results

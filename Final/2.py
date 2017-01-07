from __future__ import division
import numpy as py
from copy import deepcopy
from cmath import *
from scipy import constants as const
import math
import matplotlib.pyplot as pl

class Mean_Field() : 
    def __init__(self, z, T, ds):
        self.s1 = [-1]
        self.s2 = [-1]
        self.func = []
        self.J_kB = 1
        self.z = z
        self.ds = ds
        self.T = T

    def left_side(self) :
        self.left=[self.s1[-1]]          
        while self.s1[-1] <= 1:       
              self.s1.append(self.s1[-1]+self.ds)
              self.left.append(self.s1[-1])  
        pl.plot(self.s1, self.left)        

    def right_side(self) : 
        self.right=[py.tanh(self.z * self.J_kB * self.s2[-1]/self.T)]        
        while self.s2[-1] <= 1:
              self.s2.append(self.s2[-1]+self.ds)
              self.right.append(py.tanh(self.z * self.J_kB * self.s2[-1]/self.T))              
        pl.plot(self.s2, self.right)

    def Newton_Raphson(self, approximation) :
        step = [0]
        approx = [approximation]
        for i in range(100):
            i = i + 1            
            step.append(i)
            approx.append(approx[-1] - (approx[-1]-math.tanh(self.z * self.J_kB * approx[-1]/self.T))/(1-(self.z * self.J_kB/self.T) / math.cosh(((self.z * self.J_kB/self.T)*approx[-1])**2)))
        pl.plot(step, approx)        
        



A = Mean_Field(4, 0.166, 0.0001)
A.Newton_Raphson(1.1)
pl.title('Solution $T=1$')



pl.ylabel('Approximation of Solution')
pl.xlabel('Steps')
pl.show()

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

        
pl.figure()
pl.subplot(321)
A = Mean_Field(4, 0.01, 0.0001)
A.left_side()
A.right_side()
pl.title('Solution of $<s>=tanh(zJ<s>/k_BT)$')
pl.text(-0.5, 0.5,'T=0.01')
pl.text(0.5, 0.5,'<s>')
pl.text(0.2, 0.8,'tanh')

pl.subplot(322)
A = Mean_Field(4, 1, 0.0001)
A.left_side()
A.right_side()
pl.title('Solution of $<s>=tanh(zJ<s>/k_BT)$')
pl.text(-0.5, 0.5,'T=1')
pl.text(0.5, 0.5,'<s>')
pl.text(0.2, 0.8,'tanh')

pl.subplot(323)
A = Mean_Field(4, 2, 0.0001)
A.left_side()
A.right_side()
pl.title('Solution of $<s>=tanh(zJ<s>/k_BT)$')
pl.text(-0.5, 0.5,'T=2')
pl.text(0.5, 0.5,'<s>')
pl.text(0.2, 0.5,'tanh')

pl.subplot(324)
A = Mean_Field(4, 3, 0.0001)
A.left_side()
A.right_side()
pl.title('Solution of $<s>=tanh(zJ<s>/k_BT)$')
pl.text(-0.5, 0.5,'T=3')
pl.text(0.5, 0.5,'<s>')
pl.text(0.3, 0.5,'tanh')

pl.subplot(325)
A = Mean_Field(4, 4, 0.0001)
A.left_side()
A.right_side()
pl.title('Solution of $<s>=tanh(zJ<s>/k_BT)$')
pl.text(-0.5, 0.5,'T=4')


pl.subplot(326)
A = Mean_Field(4, 5, 0.0001)
A.left_side()
A.right_side()
pl.title('Solution of $<s>=tanh(zJ<s>/k_BT)$')
pl.text(-0.5, 0.5,'T=5')





pl.xlabel('<s>')
pl.show()

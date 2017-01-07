import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as pl


boltzmann = 1.38e-23


def randomindex(size):
  'Returns random indices based on matrix size.'
  return np.random.randint(size)


def genmatrix(beta, size):
  'Generates the matrix: aligned for beta > 0.5, random for below.'
  matlist = []
  if beta < 0.5:
    matlist = [[np.random.choice([1,-1]) for i in range(size)] for i in range(size)]
  else:
    matlist = np.ones((size,size))
  return np.matrix(matlist)


def energyfromloc(value, location, matrix, field):
  'Calculates the energy contibution from one site in the matrix.'
  size = matrix.shape[0]
  E = 0
  i, j = location
  E -= value*matrix.item(i,j-1)         # left
  E -= value*matrix.item(i,(j+1)%size)  # right
  E -= value*matrix.item(i-1,j)         # up
  E -= value*matrix.item((i+1)%size,j)  # down
  E -= value*field
  return E


def energytot(matrix, field):
  '''
  Calculates the total energy of the matrix. Note, no double
  counting required as only the right and down interactions 
  are counted.
  '''
  size = matrix.shape[0]
  E = 0
  for (i,j), value in np.ndenumerate(matrix):
    E -= value*matrix.item(i,(j+1)%size)  # right
    E -= value*matrix.item((i+1)%size,j)  # down
    E -= value*field
  return E


def energydiff(location, matrix, field):
  'Calcuates delta E for a spin flip.'
  value = matrix.item(location)
  E = energyfromloc(value, location, matrix, field)
  value = -value
  newE = energyfromloc(value, location, matrix, field)
  return newE - E


il = []
maglist = []
energylist = []
spinlist = []
def iteration(matrix, beta, field):
  'Implementation of the Metropolis algorithm.'
  size = matrix.shape[0]
  i = j = 0
  k = 0
  print ('Equilibration...')
  while True:
    S = np.sum(matrix)
    E = energytot(matrix, field)
    M = S/(size**2)    
    print (M)
    location = (i,j)
    cur = matrix.item(location)
    for i in range(size-1):
        for j in range(size-1):
            Ediff = energydiff(location, matrix, field)
            exp = np.exp(-Ediff*beta)                      
            if Ediff < 0 :  # accepted
               E += Ediff
               S -= 2*cur
               M -= (2*cur)/float(size**2)
               matrix.itemset(location, -cur)
            else :  
               random = np.random.random()  # random between 0 and 1               
               if random <= exp: 
                   cur = matrix.item(location)
                   E += Ediff
                   S -= 2*cur
                   M -= (2*cur)/float(size**2)
                   matrix.itemset(location, -cur)
            j += 1
        i += 1  
    k += 1  # iteration counter    
    energylist.append(E)
    maglist.append(M)
    spinlist.append(S)
    il.append(k)
    if il[-1] == 10000:
        break



  # calculation of quantities of interest
  energy = np.mean(energylist)
  capacity = beta**2 * boltzmann * np.var(energylist) / size**2
  magnetisation = np.mean(maglist)
  chi = beta * np.var(spinlist) / size**2
  print ('Run over.')

  return energy, capacity, magnetisation, chi, matrix



    
    
def avgvalues(beta, field, size, runs):
  'Averages results from iteration() "runs" times.' 
  Elist = []
  Clist = []
  Mlist = []
  Chilist = []
  for i in range(runs):
    print ('Run %s:' % (i+1))
    matrix = genmatrix(beta, size)
    energy, capacity, mag, chi, resultmatrix = iteration(matrix, beta, field)
    Elist.append(energy)
    Clist.append(capacity)
    Mlist.append(mag)
    Chilist.append(chi)
  return np.mean(Elist), np.mean(Clist), np.mean(Mlist), np.mean(Chilist), resultmatrix
  
T = 6
beta = 1/T
matrix = genmatrix(beta, 10)
 
A=iteration(matrix, beta, 0)   

pl.plot(il, maglist, '.' )

pl.show()
print(A)

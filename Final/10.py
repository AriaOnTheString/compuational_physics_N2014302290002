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
def iteration(matrix, beta, field):
  'Implementation of the Metropolis algorithm.'
  size = matrix.shape[0]
  energylist = []

  spinlist = []
  E = energytot(matrix, field)
  S = np.sum(matrix)
  M = S/(size**2)
  eqlist = []
  prevavg = 0
  stable = False  # starts off unstable
  i = j = 0

  print ('Equilibration...')
  while True:
    
    i += 1  # iteration counter
    location = (randomindex(size),randomindex(size))
    Ediff = energydiff(location, matrix, field)
    random = np.random.random()  # random between 0 and 1
    exp = np.exp(-Ediff*beta)
    if Ediff < 0 or random < exp:  # accepted
      cur = matrix.item(location)
      E += Ediff
      S -= 2*cur
      M -= (2*cur)/float(size**2)
      matrix.itemset(location, -cur)
    else:  # rejected
      pass

    if not stable:
      eqlist.append(E)
      if len(eqlist) == 100000:
        avg = np.mean(eqlist)
        if np.abs((avg-prevavg)/avg) <= 0.01 or i >= 1000000:
          # equilibrium condition, or iteration cutoff point
          print ('Taking data...')
          stable = True
        prevavg = np.mean(eqlist)
        eqlist = []

    if stable:  # see what I did with the conditions? ;)
      j += 1  # results counter
      energylist.append(E)
      maglist.append(M)
      spinlist.append(S)
      il.append(j)
      if j == 10000: # 100000 steps taking data
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
  
pl.figure()
pl.subplot(611)
T = 1
beta = 1/T
matrix1 = genmatrix(beta, 10)
A1 = iteration(matrix1, beta, 0)
pl.plot(il, maglist, color='midnightblue')
il=[]
maglist=[]
pl.ylim(-1.2,1.2)
pl.title('Mahnetization $T=1$')


pl.subplot(612)
T = 2
beta = 1/T
matrix2 = genmatrix(beta, 10)
A2 = iteration(matrix2, beta, 0)
pl.plot(il, maglist, color='blue')
il=[]
maglist=[]
pl.ylim(-1.2,1.2)
pl.title('Mahnetization $T=2$')


pl.subplot(613)
T = 3
beta = 1/T
matrix3 = genmatrix(beta, 10)
A3 = iteration(matrix3, beta, 0)
pl.plot(il, maglist, color='mediumslateblue')
il=[]
maglist=[]
pl.ylim(-1.2,1.2)
pl.title('Mahnetization $T=3$')


pl.subplot(614)
T = 4
beta = 1/T
matrix4 = genmatrix(beta, 10)
A4 = iteration(matrix4, beta, 0)
pl.plot(il, maglist, color='darkviolet')
il=[]
maglist=[]
pl.ylim(-1.2,1.2)
pl.title('Mahnetization $T=4$')


pl.subplot(615)
T = 5
beta = 1/T
matrix5 = genmatrix(beta, 10)
A5 = iteration(matrix5, beta, 0)
pl.plot(il, maglist, color='deeppink')
il=[]
maglist=[]
pl.ylim(-1.2,1.2)
pl.title('Mahnetization $T=5$')


pl.subplot(616)
T = 6
beta = 1/T
matrix6 = genmatrix(beta, 10)
A6 = iteration(matrix6, beta, 0)
pl.plot(il, maglist, color='crimson')
pl.ylim(-1.2,1.2)
pl.title('Mahnetization $T=6$')

pl.show()

#Thiago dos Santos 218060051
#Thiago Bulhosa 119060005

from numpy.random import choice
from numpy import cumsum,zeros
import matplotlib.pyplot as plt

p_frente=[0.5,0.6,0.7,0.8,0.9]
p_tras=[0.5,0.4,0.3,0.2,0.1]
np=100
nb=100000
res= [zeros(shape=(np,nb)) for i in range(5)]

for i in range(5):
    res[i] = choice(a=[-1, 1], size=(np, nb), p=[p_tras[i], p_frente[i]])
    res[i][0,:] = 0
    res[i] = cumsum(res[i], axis=0)
    plt.hist(res[i][-1],bins=20,density=True,alpha=0.6)
plt.show()
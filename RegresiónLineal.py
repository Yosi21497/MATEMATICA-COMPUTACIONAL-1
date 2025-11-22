import numpy as np
import LIBRERIA as lib
import matplotlib.pyplot as plt
import numpy.polynomial as poly


'''Interpolación'''
x=np.array([2,3,4,5,7,9])
y=np.array([1,3,-4,-5,17,-19])

pol=lib.interpLagrange(x,y)

print(pol)
print(pol(x))

'''Gráfica'''
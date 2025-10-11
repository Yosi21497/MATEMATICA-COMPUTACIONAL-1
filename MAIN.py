import numpy as np
import LIBRERIA as lib

A=np.random.randint(-5,15,size=(3,3)) #para matriz aleatoria
print(A)

#lib.intercambiaFilas(A,0,3) #intercabiará la fila 0 con la fila 3
print(A)

lib.operacionFila(A,2,0,2)#fila a modificar,piboc,factor a la fila 2 le ha debido restar dos veces l fila piboc


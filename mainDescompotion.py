import numpy as np
import LIBRERIA as lib

n=5
A=np.random.rand(n,n)
b=np.random.rand(n,1)
#LU=lib.LUdecomposition(A)

#L=LU[0] #triangular inferior
#print("la matriz L es: \n",L)
#U=LU[1] #triangular superior
#print("la matriz U es: \n",U)

#print("A-LU: \n",A-L@U) #está bien cuando al multiplicar L por U es A 

#GENERAMOS SISTEMA DE ECUACIONES LINEALES POR LU

X=lib.SolveByLU(A,b) # Nos va dar el resultado de AX=b
print("AX-b: \n",(A@X-b))
print("||AX-b||_1: \n", np.linalg.norm(A@X-b))
import numpy as np
import LIBRERIA as lib
import time

#A=np.random.randint(-5,15,size=(3,3)) #para matriz aleatoria
#print("\n",A) #"\n" para darle espacio

n=3 #Tamaño del sistema lineal
A=np.random.rand(3,3) #para matriz aleatoria
print("Mi matriz A es: \n",A) 

b=np.random.rand(3,1) #para una matriz al azar de 3 filas por 1 columna
print("Mi matriz b es: \n",b)



#lib.intercambiaFilas(A,0,3) #intercabiará la fila 0 con la fila 3
#print(A)

#lib.operacionFila(A,2,0,2)#(A,fila a modificar,pibote,factor a la fila 2 le ha debido restar dos veces la fila del pibote)
#print("\n",A)


#lib.escalonaSimple(A)  #para hacer una matriz escalonada
#print("\n",A)

#lib.escalonaConPiv(A) #para hacer una matriz escalonada con pivote
#print("la matriz escalonada con Pivote es: \n",A) 


#lib.sustRegresiva(A,b) #para hacer una matriz escalonada con pivote
#print("la solución de la forma escalonada: \n",A) 

start_time = time.perf_counter() #para calcular el tiempo iniciado
sol=lib.GaussElimSimple(A,b)
print("Gauss Eliminación Simple: \n",sol)
print("La comprobación: \n",A@sol) #si la comprobación me da la matriz b igual a la que pusimos está bien. (recordemos que A*x=b )
end_time = time.perf_counter() #para calcular el tiempo final
elapsed_time= end_time - start_time #para calcular el tiempo total #elapsed=transcurrido
print("El tiempo en segundos en calcular es: \n",elapsed_time)

residuo=A@sol-b
print("El residuo es: \n", residuo)  #me tiene que dar cero, sino algo está mal
print("Norma del residuo es: \n", np.linalg.norm(residuo))  

hilbert1=lib.hilbert_matrix(3)
print("La matriz de Hilbert es: \n", hilbert1) 
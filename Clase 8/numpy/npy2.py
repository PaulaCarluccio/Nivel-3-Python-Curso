import numpy as np
a = np.array([[9, 1, 21],[19,22,33]])
#print(a)
#Reemplazar un elemento
a[1][0] = 55
print(a)
#Imprime las dimensiones
print(a.ndim)
#Imprime una tupla con la forma
print(a.shape)
#Imprime cantidad de elementos del primer nivel
print(len(a))
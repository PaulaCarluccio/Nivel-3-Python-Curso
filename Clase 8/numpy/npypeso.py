import numpy as np
import sys
#Comparar espacio que ocupa en memoria
datos1 = range(100)
print(datos1)
print(sys.getsizeof(datos1)*len(datos1))
datos2 = np.arange(100)
print(datos2.shape)
print(len(datos2))
print(datos2.size*datos2.itemsize)
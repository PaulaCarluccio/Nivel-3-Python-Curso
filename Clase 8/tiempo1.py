import time
inicio = time.time()
milista= []
for i in range(1000000):
 milista.append(i)
fin = time.time()
cuanto = (fin - inicio)
print(cuanto)
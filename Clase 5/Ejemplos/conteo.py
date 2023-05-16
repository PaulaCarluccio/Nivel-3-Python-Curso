#by todos
import re
datos =["ut","de","ca"] 
archivo = open("lorem.txt","r")
lorem = archivo.read()
lista =[]
for dato in datos:
    lista.append(re.findall(dato,lorem))
for a in lista:
    print(a[0] + " : " + str(len(a)))
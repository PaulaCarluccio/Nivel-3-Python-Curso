#By Pau
import re
texto= open("lorem.txt", "r")
v = texto.read()
lista = ["ut","de","ca"]
for i in lista:
    expresion = re.findall(i,v)
    print(i + ":" + str(len(expresion)))
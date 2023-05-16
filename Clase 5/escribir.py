#f = open("nuevo-ejemplo.txt", "w")
f = open("nuevo-ejemplo.txt", "a") # para agregar
f.write("Otro texto del Mundo")
#f.write("Mi texto\n") #para salto de línea
f.close()
f = open("nuevo-ejemplo.txt", "r")
print(f.read())
f.close()
import re
texto = "Mi texto"
encontrado = re.search("ex", texto)
#encontrado = re.match("ex", texto)
#encontrado = re.match("Mi texto", texto)
if (encontrado):
  print("Encontrado")
else:
  print("No Encontrado")
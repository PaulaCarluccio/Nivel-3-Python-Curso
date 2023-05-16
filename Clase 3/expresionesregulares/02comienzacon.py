import re
texto = "Mi texto"
encontrado = re.search("^Mi", texto)
#encontrado = re.match("^Mi", texto)
if (encontrado):  
  print("Encontrado")
else:
  print("No Encontrado")
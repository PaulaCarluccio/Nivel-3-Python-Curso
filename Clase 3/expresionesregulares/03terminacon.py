import re
texto = """Mi  
gran
texto"""

encontrado = re.search("to$", texto)
#encontrado = re.match("to$", texto)
if (encontrado):
  print("Encontrado")
else:
  print("No Encontrado")
#dataset con diccionarios
import pandas as pd
datos = {'producto': ["Pan", "Leche", "Arroz"], 'cantidad': [20, 14, 18]}
pdatos = pd.DataFrame(datos)
print(pdatos)
#print(pdatos["producto"])
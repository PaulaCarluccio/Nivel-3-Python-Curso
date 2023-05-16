#dataset con diccionarios
import numpy as np
import pandas as pd
datos = {'producto': ["Pan", "Leche", "Arroz","Fideos"], 'cantidad': np.array([20, 14, 18,5]), 'ensucursal': True}
pdatos = pd.DataFrame(datos)
#print(pdatos)
#print(pdatos[["producto","ensucursal"]])
#print(pdatos["producto"][3])
#print(pdatos.loc[3])
#print(pdatos.loc[0:2,["producto","ensucursal"]])
print(pdatos.sort_values(by=['producto', 'cantidad'], ascending=[True, False]))
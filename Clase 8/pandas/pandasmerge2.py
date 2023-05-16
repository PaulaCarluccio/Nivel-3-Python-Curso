import pandas as pd
left = pd.DataFrame({'ciudad': ['Buenos Aires', 'Mendoza', 'Montevideo'], 'idpais': [1,1,2]})    
right = pd.DataFrame({'pais': ['Argentina','Uruguay','Brasil', 'Chile', 'Paraguay'], 'idpais': [1,2,3,4,5]})
resultado = left.merge(right, on='idpais', how="left") #left join
print(resultado)
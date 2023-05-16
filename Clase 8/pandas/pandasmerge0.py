import pandas as pd
s1 = pd.DataFrame({'superheroe': ['Superman', 'Capitan América', 'Spider-Man', 'Flash'],
                    'editorial': ['DC', 'Marvel', 'Marvel', 'DC']})
s2 = pd.DataFrame({'superheroe': ['Superman', 'Capitan América', 'Spider-Man', 'Flash'],
                    'creado': [1933, 1941, 1962, 1940]})

s3 = pd.merge(s1, s2)
s3ordenado = s3.sort_values(by=['creado'], ascending=[True])
print(s3)
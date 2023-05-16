import numpy as np
import pandas as pd
left = pd.DataFrame({'letra': ['A', 'B', 'C'], 'aleatorio': np.random.randn(3)})    
right = pd.DataFrame({'letra': ['B','C','D', 'E', 'F'], 'aleatorio': np.random.randn(5)})
#print(left)
#print(right)
resultado = left.merge(right, on='letra') #inner join
#resultado = left.merge(right, on='letra', how="left") #left join
#resultado = left.merge(right, on='letra', how="right") #right join
print(resultado)

#Ejemplos basados en https://stackoverflow.com/questions/53645882/pandas-merging-101
#Stock es stock en sucrusal
import pandas as pd
p1 = pd.DataFrame({'producto': ['Mouse', 'Teclado', 'Hub'], 
                    'cantidad': ['50', '15', '5'], 
                    'stock': [True,True,True]},                 
                    index = [0, 1, 2]) 
  
p2 = pd.DataFrame({'producto': ['Soporte', 'Cover', 'Cooler'], 
                    'cantidad': ['55', '12', '120'], 
                    'stock': [True,False,False]},
                    index = [3, 4, 5])   

p3 = pd.DataFrame({'producto': ['Fuente', 'Mother', 'Microprocesador','Memoria'], 
                    'cantidad': ['7', '9', '3', '33'], 
                    'stock': [True,False,True,True]},                     
                    index = [6, 7, 8, 9]) 


p4 = pd.DataFrame({'producto': ['TV', 'Smartphone'], 
                    'cantidad': ['7', '9'], 
                    'stock': [True],
                    'origen': ["AR","BR"]
                    },                     
                    index = [20,21]) 

p5 = pd.DataFrame({'producto': ['Cocina', 'Heladera'],                     
                    'stock': [True,False],
                    'origen': ["AR"]
                    },                     
                    index = [15,16]) 

#pconactenado = pd.concat([p1, p2, p3])                   
#print(pconactenado)
#pconactenado = pd.concat([p1, p2, p3,p4])
#pconactenado.fillna("Info no disponible",inplace=True)
#print(pconactenado)
#print(pconactenado.loc[20])
#print(pconactenado["producto"][20])
pconactenado = pd.concat([p1, p2, p3,p4,p5])
pconactenado["cantidad"].fillna(0, inplace=True)
pconactenado["origen"].fillna("Sin datos", inplace=True)
print(pconactenado)
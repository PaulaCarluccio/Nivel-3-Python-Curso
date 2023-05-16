from pandas import DataFrame
import matplotlib.pyplot as plt
   
datos = {'inflacion': [40,30,20,25,50,10,20,15.5,19],
        'years': [2020,2021,2022,2023,2024,2025,2026,2027,2028]
       }

df = DataFrame(datos,columns=['years','inflacion'])
#df['years'].astype(int)
df.plot(x ='years', y='inflacion', kind = 'scatter')
#plt.xlabel('Años', fontsize=18)
#plt.ylabel('Inflación', fontsize=16)
#df.plot(x ='years', y='inflacion', kind = 'bar', color='red')
#color='#0F00E0'
plt.savefig('grafico.png')
plt.show()
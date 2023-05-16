import matplotlib.pyplot as plt

items = 'Comida', 'Ropa', 'Impuestos', 'Otros'
gastos = [25, 10, 50, 15]
explode = (0, 0.2, 0, 0)  

fig1, ax1 = plt.subplots()
ax1.pie(gastos, explode=explode, labels=items,shadow=True, startangle=90)
ax1.axis('equal')

plt.show()
import re
txt = "Padre nuestro"
x = re.search("(pa|ma)dre", txt,re.IGNORECASE)

if (x):
 print("SI")
else:
 print("NO")    
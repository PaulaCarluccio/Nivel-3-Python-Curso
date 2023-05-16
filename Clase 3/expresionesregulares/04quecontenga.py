#Que contenga algunas de los caracteres
import re
txt = "Probando expresiones"
#x = re.search("[zy]", txt)
x = re.search("[ey]", txt)

if (x):
 print("SI")
else:
 print("NO")
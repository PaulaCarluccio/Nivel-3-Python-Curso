import re
# A partir de que lo encuentra (0|1|2|4) y 2 numeros
n = "sdafasdfer5a490"
x = re.search("((0|1|2|4)[0-9]{2}$)", n)

if (x):
 print("SI")
else:
 print("NO")
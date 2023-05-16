import numpy as np
import time

s = 5000000

l1 = range(s)
l2 = range(s)
a1 = np.arange(s)
a2 = np.arange(s)

start = time.time()
#https://www.programiz.com/python-programming/methods/built-in/zip
r = [(x,y) for x,y in zip(l1,l2)]
print(str(time.time() - start))
start2 = time.time()
r2 = a1+a2
print(str(time.time() - start2))
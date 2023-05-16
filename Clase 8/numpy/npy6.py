import numpy as np
# 2x3
a = np.array([(1,2,3),(4,5,6)])
print(a)
# 3x2
b = a.reshape(3,2)
print(b)
print(b.dtype)

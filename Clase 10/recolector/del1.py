import sys
a = 10
print(a)
print(sys.getrefcount(a))
del a
print(a)
import numpy as np

a = np.array([1,2,3])
b = a
b[0]= 100
print(a)  # output of a: [100   2   3]

# because we changed b and it was equal to a, a also got changed when we changed b
# so to avoid this use copy()

c = np.array([1,2,3])
d=c.copy()
d[0]=100
print(c) # output: [1 2 3]


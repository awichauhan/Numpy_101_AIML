import numpy as np

a = np.zeros(5) # all 0s matrix
print(a)  # output: [0. 0. 0. 0. 0.]

b = np.zeros([2,3])
print(b)

c = np.zeros((2,3,3))  #shape: matrix, row, column
print(c, "\n")

d = np.zeros((2,3,3,2))
print(d, "\n")

e= np.ones((2,2))
print(e, "\n")

f = np.full((2,2),99)
print(f)

g = np.full_like(a,4) # or the syntax could be np.full(a.shape,4)
print(g)

h = np.random.rand(2,3,3)  # random decimal number
print(h)

i = np.random.randint(2,3)
print(i)

j = np.random.randint(7,10, size = (2,3,3))
print(j)

k = np.identity(4)  #identity matrix
print(k)

l = np.array([[1,2,3]])
r1 = np.repeat(l,3,axis = 0)
print(r1)
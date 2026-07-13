import numpy as np

a = np.array([[10,20,30,40,50,60,70,80],[11,22,33,44,55,66,77,88]])  # had to define equal number of elements for both dimensions
print(a)

print(a[0,2])  # get a specific element: array[row index, column index]; output is 30

print(a[1,-2]) # second row, last second column (reverse order)

print(a[0, :]) # slicing; printing all column of one row

print(a[:, 7]) # get a specific column (from both rows)

# [startindex: endindex : stepsize]

print(a[0, 0:7:1]) # first row, start reading column from 0 index to 7th index with step size of 1; output: [10 20 30 40 50 60 70]
print(a[0:7:1]) # will start from first row, till 7th column, with step size of 1; output: [[10 20 30 40 50 60 70 80], [11 22 33 44 55 66 77 88]]
print(a[0,1:-2:2])  # start from first row, from 1st column to last second column with step size of 2; output: [20 40 60]


a[1,7] = 99  # changing specific value
print(a[1,:]) # output: [11 22 33 44 55 66 77 99]


#3D examples

b = np.array([
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]
])

 # getting specific element from 3D array:
print(b[0,1,1])  # to print 4 (first matrix, 2nd row, 2nd column)
print(b[:,1,:]) # output: [[3 4],[7 8]]  basically 2nd row from both matrix and columns

b[:,0,:] = [[9,9],[8,8]]  # replacing 1st row of both matrix
print(b)
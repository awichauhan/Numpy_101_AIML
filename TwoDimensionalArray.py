import numpy as np

TwoDMatrix = np.array([
    [10,20,30],
    [40,50,60]
])

print("2D Array is \n", TwoDMatrix)
print("Shape", TwoDMatrix.shape)
print("Dimension", TwoDMatrix.ndim)
print("Type of array: ", TwoDMatrix.dtype)  #int64 type
print("Item size is: ", TwoDMatrix.itemsize) # itemsize is 8
print("array size is: ", TwoDMatrix.size) # number of elements is 6
print("total memory size of array: ", TwoDMatrix.size * TwoDMatrix.itemsize) # total memory size of array is 48 (8*6)
print("total memory size of array: ", TwoDMatrix.nbytes)  # total mem size can be represented as number of bytes "nbytes"; nbytes are 48
# shape = (rows, columns), here it is (2,3)


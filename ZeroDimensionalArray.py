import numpy as np

value = np.array(10 , dtype="int16")  # specifying data type while initializing; int16 as we know that the values will be smaller
print(value)
print("Dimensions", value.ndim)
print("Shape", value.shape)
print("datatype: ", value.dtype)

print("Memory size being used is: ", value.itemsize)  #int16 will have itemsize of 2 bytes; int32 will have 4 bytes
print(" total size is: ", value.size)  # number of elements
print("total memory size: ", value.size * value.itemsize)

# This contains only one scalar value.
# It has no axis, so it is called a 0D array.


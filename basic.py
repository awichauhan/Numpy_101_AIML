import numpy as np

numbers = np.array([10, 20, 30])    # n- dimensional array #
# np.array() converts a Python list into a NumPy array.

print(numbers)
print(type(numbers))
print(numbers * 2)

print("Dimensions", numbers.ndim)  # number of dimensions
print("Shape:", numbers.shape) # size along each dimension
print("Number of elements:", numbers.size) # total number of elements
print("Data type:", numbers.dtype) # data type stored in the array


# numpy is a multidimensional array library
# list is slow; numpy is fast
# numpy uses fixed type
#numpy will cast 5 (binary: 00000101) into Int32 (00000000 00000000 00000000 00000101) basically memory size of 4 bytes
# also u can use Int16 representation (00000000 00000101) i.e., 2 bytes; for even small value use Int8, which will use 1 bytes

# when lists are used, it uses built in integer type of python that consists of object valyes, obj type, reference count and size of integer value.
# obj valu= long (8byte), refe count = 4 bytes, basically lot of memory size for just one single integer.

#numpy is faster to read as it uses less bytes of memory.. less bytes to read for computer
# no type checking each element as it stores only single type, lists can store many types of elements, so it has to iterate over each element to know its type

#numpy utilizes continuous memory location unlike lists
# SIMD vector processing.. single instruction multiple value.. perform computation on all values in one go

# effective cache utilization (discontinuous memory location)
# it can be a MATLAB

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
import numpy as np

ThreeDArray = np.array([
    [
        [10,20,30],
        [40,50,60],
        [70,80,90]
    ],
    [
      [10,20,30],
        [40,50,60],
        [70,80,90]
    ]
])

print("3D Array is \n", ThreeDArray)
print("Shape", ThreeDArray.shape)
print("Dimension", ThreeDArray.ndim)


# shape is (2, 3, 3); means : shape = (matrices, rows, columns)

# NumPy converts the integers into floating-point numbers so that the entire array has a common data type.

ThreeDFloatArray = np.array([
    [
        [10.2,4,5],
        [20,5,6]
    ],
    [
        [30,60,30],
        [2.5,60,70]
    ]
])

print(ThreeDFloatArray)
print(type(ThreeDFloatArray))
print(ThreeDFloatArray.dtype)

# because of one element, entire array datatype is changed to floattype


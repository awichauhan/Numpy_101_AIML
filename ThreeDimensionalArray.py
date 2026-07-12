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


# shape is (2, 3, 3); means :
# 2 matrices
# 2 rows in each matrix
# 3 columns in each row
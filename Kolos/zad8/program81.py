import numpy as np


my_array = np.array([x for x in range(10, 39, 2)])
# print(my_array)
# print(my_array.shape)

# my_array.resize(3)
print(my_array)

print(my_array*2)

for i in range(0, my_array.shape[0]):
    if my_array[i] % 6 == 2:
        my_array[i] = 0
print(my_array)

my_array1 = np.array([[1, 0, 3], [3, 2, 0], [2, 3, 1]])
print(my_array1[1][1])
def change(A, x):
    B = A
    for i in range(0, B.shape[1]):
        for j in range(0, B.shape[0]):
           y = B[i][j]
           if y == 0:
               B[i][j] = x
    return B

print(change(my_array1, 3))
import numpy as np

A = np.array([[1, 1, 2], [2, 1, 0], [4, 1, 2]])
B = np.array([[2, 5, 7], [2, 8, 0], [4, 3, 1]])

print(A+B)
#   Iloczny
print(np.dot(A, B))
#   Iloczny po elemencie
print(A*B)
#   Transpozycja
print(np.transpose(A))
#   Odwrócenie
print(np.linalg.inv(A))
#   el. do 5 potęgi
print(A**5)
#   A do 5
print(np.linalg.matrix_power(A, 5))
#   Wyznacznik
print(np.linalg.det(B))
#   B do -3
print(np.linalg.matrix_power(B, -3))

E = np.array([[1, 5], [2, 1]])
F = np.array([[2, 1], [2, 8]])

# E/F
print(E/F)
print(E//F)
print(E%F)

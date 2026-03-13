import numpy as np

n = int(input("mnter size of square matrix: "))
matrix = np.random.randint(1, 10, size=(n, n))

print('original matrix ',matrix)


for i in range(n):
    matrix[i][i], matrix[i][n-i-1] = matrix[i][n-i-1], matrix[i][i]

print("matrix after swapping diagonals:")
print(matrix)
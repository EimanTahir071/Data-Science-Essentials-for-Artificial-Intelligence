import numpy as np

# Create a 4x4 matrix
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15,16]])

print("Matrix:")
print(matrix)

# Calculate sum of rows
row_sums = np.sum(matrix, axis=1)
print("\nSum of rows:", row_sums)

# Calculate sum of columns
col_sums = np.sum(matrix, axis=0)
print("Sum of columns:", col_sums)
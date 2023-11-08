import numpy as np

def generate_hilbert_matrix(n):
    hilbert_matrix = np.zeros((n, n))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            hilbert_matrix[i-1][j-1] = 1 / (i + j - 1)
    return hilbert_matrix

# Getting input from the user...
n = int(input("Enter the value of n: "))

# Generating the Hilbert matrix...
result_matrix = generate_hilbert_matrix(n)
print("The Hilbert matrix is:")
print(result_matrix)

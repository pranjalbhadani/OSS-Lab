import numpy as np

def input_matrix():
    print("Enter the size of the square matrix (n):")
    n = int(input())
    print(f"Enter the elements of the {n}x{n} matrix row-wise, separated by spaces:")

    matrix = []
    for i in range(n):
        row = list(map(float, input().split()))
        while len(row) != n:
            print(f"Please enter exactly {n} elements for row {i+1}:")
            row = list(map(float, input().split()))
        matrix.append(row)
    return np.array(matrix)

mat = input_matrix()

rank = np.linalg.matrix_rank(mat)
trace = np.trace(mat)
det = np.linalg.det(mat)

print("\nInput matrix:")
print(mat)
print(f"\nRank of the matrix: {rank}")
print(f"Trace of the matrix: {trace}")
print(f"Determinant of the matrix: {det}")

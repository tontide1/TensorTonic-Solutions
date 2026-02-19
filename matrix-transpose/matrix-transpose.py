import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    # A [[1, 2, 3], [4, 5, 6]]
    N = len(A)
    M = len(A[0])

    res_matrix = np.zeros((M, N)) # khởi tạo ma trận 

    for i in range (N):
        for j in range (M):
            res_matrix[j][i] = A[i][j]

    return res_matrix
    
    pass

import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    row = len(A)
    col = len(A[0])

    trace = 0
    
    if row == 1 and row == col:
        return float(A[0][0])
    else:
        for i in range (row):
            for j in range (col):
                if i == j:
                    trace += A[i][j]

        return trace
    pass

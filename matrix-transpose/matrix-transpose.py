import numpy as np
def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.asarray(A, dtype=float)
    n, m = A.shape

    AT = np.zeros((m, n), dtype=A.dtype)

    for i in range(n):
        for j in range(m):
            AT[j, i] = A[i, j]


    return AT
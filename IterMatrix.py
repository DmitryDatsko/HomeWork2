import numpy as np

def iter_matrix_mul(arr_a, arr_b):
    if(np.shape(arr_a)[0] == np.shape(arr_b)[0]):
        return np.dot(arr_a.transpose(), arr_b)
    else:
        return np.arange(0)
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[1, 2], [3, 4]])

print(iter_matrix_mul(A, B))

A = np.array([[1, 2], [4, 5], [6, 7]])
B = np.array([[1, 2], [3, 4]])

print(iter_matrix_mul(A, B))
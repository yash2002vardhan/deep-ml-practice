"""
Write a Python function that computes the dot product of a matrix and a vector. The function should return a list representing the resulting vector if the operation is valid, or -1 if the matrix and vector dimensions are incompatible. A matrix (a list of lists) can be dotted with a vector (a list) only if the number of columns in the matrix equals the length of the vector. For example, an n x m matrix requires a vector of length m.
"""

import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
    arr1 = np.array(a)
    arr2 = np.array(b)

    if arr1.shape[1] != arr2.shape[0]:
        return -1
    
    else: 
        return np.dot(arr1, arr2)


print(matrix_dot_vector([[1, 2], [3, 4]], [5, 6]))

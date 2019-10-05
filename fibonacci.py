# Runtime: O(log(N))
import numpy as np
from numpy.linalg import matrix_power
import random as rd

def fibonacci(n):
    initial_vector = np.array([[1],[0]])  # Vector with the first two members of the sequence
    fib_matrix = np.array([[1,1],         # Matrix representing the fibonacci transform
                           [1,0]])
    result = matrix_power(fib_matrix, n) * initial_vector  # Compute the corresponding number
    return(result[0,1])


# DEMONSTRATE ways to use the function:
for i in range(5):
    n = rd.randint(0,92)
    print('F(', n, ') = ', fibonacci(n), sep='')    
print('The Golden Ratio is approximately', fibonacci(92)/fibonacci(91))

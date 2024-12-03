# Array Operations
import numpy as np

# Arithmetic Operations
a1 = np.arange(20)
a2 = np.linspace(100, 200, 20)
print(a1 + a2)  # Element-wise addition
print(a1 * a2)  # Element-wise multiplication
print(np.add(a1, a2))  # Same as `a1 + a2`

# Comparison Operations
a3 = np.random.randint(5, size=15)
a4 = np.random.randint(5, size=15)
print(a3 == a4)  # Boolean array showing True where elements match
print(a3 < a4)   # Boolean array showing True where a3[i] < a4[i]
print(a3 >= a4)  # Boolean array showing True where a3[i] >= a4[i]

# Scalar Multiplication
a5 = np.arange(100).reshape(10, 10)
a6 = np.diag(np.arange(10))
print(a5 * a6)
# Multiplies each diagonal element of a6 with the corresponding row/column in a5.
# Non-diagonal elements become 0.

# Matrix Multiplication
# Basics
print(np.matmul([[1, 2], [3, 4]], [[10, 100], [1000, 10000]]))
# Output:
# [[2010 20010]
#  [4030 40030]]

# Using the @ Operator
a = np.array([[1, 2], [3, 4]])
b = np.array([[10, 100], [1000, 10000]])
print(a @ b)  # Performs the same as np.matmul(a, b)

# Examples
# (3,1) @ (1,3) -> (3,3)
print(np.matmul([[1], [2], [3]], [[100, 1000, 10000]]))
# Output:
# [[  100   1000  10000]
#  [  200   2000  20000]
#  [  300   3000  30000]]

# (3,2) @ (2,3) -> (3,3)
print(np.matmul([[1, 2], [3, 4], [5, 6]], [[1, 10, 100], [1000, 10000, 100000]]))
# Output:
# [[ 2001 20010 200100]
#  [ 4003 40030 400300]
#  [ 6005 60050 600500]]

# Mixed 1D/2D Cases
print(np.matmul([10, 20], [1, 2]))  # Dot product of 1D arrays
# Output: 50
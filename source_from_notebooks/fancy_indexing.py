# Fancy Indexing
import numpy as np

# Indexing with Lists or Arrays
a = np.array([12, 34, 56, 78, 90])
print(a[[0, 3, 4]])
# Output: array([12, 78, 90])

# Index Reuse
print(a[[0, 1, 0, 2]])
# Output: array([12, 34, 12, 56])
# Repeated indices appear multiple times in the result.

# Fancy Indexing for Multi-dimensional Arrays
b = np.arange(50).reshape(5, -1) * 10
print(b[[1, 2, 2], [3, 5, 6]])
# Output: array([130, 250, 260])
# Selects elements at (1,3), (2,5), and (2,6).

# Using np.ix_ for Advanced Selection
rows = [1, 2, 3]
cols = [1, 2, 5, 6, 8]
print(np.ix_(rows, cols))
# Output: A tuple of index arrays for advanced indexing:
# (array([[1],
#        [2],
#        [3]]), array([[1, 2, 5, 6, 8]]))

print(b[np.ix_(rows, cols)])
# Output: A submatrix containing only the specified rows and columns:
# array([[110, 120, 150, 160, 180],
#        [210, 220, 250, 260, 280],
#        [310, 320, 350, 360, 380]])
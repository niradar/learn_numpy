# Modifying Arrays
import numpy as np
from matplotlib import pyplot as plt

# Bulk Assignment with Slices
a = np.arange(10)  # Array: [0, 1, 2, ..., 9]
a[3:6] = 999  # Assign 999 to indices 3, 4, 5
# Result: array([  0,   1,   2, 999, 999, 999,   6,   7,   8,   9])

a[1:4] += 1000  # Add 1000 to indices 1, 2, 3
# Result: array([   0, 1001, 1002, 1999,  999,  999,    6,    7,    8,    9])

# Replacement with Another Array
b = np.random.random(10)  # Random array of size 10
b[3:7] = np.arange(4)  # Replace slice with values from np.arange(4)
# Example result: array([... 0.0, 1.0, 2.0, 3.0, ...])
print(b)

# Element-wise Operations
c = np.arange(15)  # Array: [0, 1, 2, ..., 14]
c[5:] *= 10  # Multiply elements from index 5 onward by 10
# Result: array([ 0, 1, 2, 3, 4, 50, 60, 70, ..., 140])
print(c)

c[3:7] **= 2  # Square elements at indices 3 through 6
# Result: array([   0,    1,    2,    9,   16, 2500, 3600,   70,   80,   90, ...])

# Image Manipulation
m = plt.imread("city.jpeg").astype(float).copy()  # Read an image and copy it
m /= 255  # Normalize pixel values to [0, 1]

# Modify the red channel
m[:, :, 0] *= 1.5  # Increase red channel intensity by 50%

# Add green block
m[100:300, 400:500] = [0, 1, 0]  # Green block in a rectangular region

# Add red block
m[50:200, 20:200] = [1, 0, 0]  # Red block in a different rectangular region

# Display the modified image
plt.imshow(m)

# Operations on Axes
a = np.arange(50).reshape(5, 10)  # Reshape into 5x10 matrix

# Total sum
print(a.sum())  # Result: 1225

# Sum along columns
print(a.sum(axis=0))  # Result: array([100, 105, ..., 145])

# Sum along rows
print(a.sum(axis=1))  # Result: array([ 45, 145, ..., 445])

# Maximum values along columns
print(a.max(axis=0))  # Result: array([40, 41, ..., 49])

# Row means
print(a.mean(axis=1))  # Result: array([ 4.5, 14.5, ..., 44.5])

# Sorting
b = np.random.random((100, 150))  # Random 2D array of size 100x150

# Sort each row
plt.imshow(np.sort(b), 'gray')  # Each row is sorted
plt.colorbar(orientation='horizontal', fraction=0.06)

# Sort each column
plt.imshow(np.sort(b, axis=0), 'gray')  # Each column is sorted
plt.colorbar(fraction=0.03)

# Sort all elements
plt.imshow(np.sort(b.ravel()).reshape(b.shape), 'gray')  # All elements are sorted
plt.colorbar()

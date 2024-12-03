import numpy as np

# Create a basic array
arr = np.array([1, 2, 3, 4, 5])

# Create a view using slicing
view = arr[1:4]

# Modifying the view also modifies the original array
view[0] = 99

print("Original array:", arr)  # [1, 99, 3, 4, 5]
print("View:", view)           # [99, 3, 4]




# Create a copy
copy = arr[1:4].copy()
copy[0] = 77

print("Original array:", arr)  # [1, 99, 3, 4, 5]
print("Copy:", copy)  # [77, 3, 4]



reshaped = arr.reshape((1, 5))  # Reshaping often returns a view if the data is contiguous
reshaped[0, 0] = 100
print("Original array:", arr)  # [100, 99, 3, 4, 5]




view = arr[1:4]
copy = arr[1:4].copy()

print(view.base is arr)  # True
print(copy.base is arr)  # False

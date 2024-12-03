import numpy as np

a = np.arange(500*500).reshape(500, 500)  # 500x500 Array
subarray = a[180:400, 250:450]  # Select a subarray
print(subarray.shape)  # (220, 200)

subarray[:] = 0 # Assign 0 to all elements in the subarray
print(a[180, 250])  # The original array is modified as well

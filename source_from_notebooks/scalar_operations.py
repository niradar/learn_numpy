import numpy as np

a = np.arange(10)  # Array: [0, 1, 2, ..., 9]
print("Original array:", a)

print("a + 100:", a + 100)  # Output: [100, 101, 102, ..., 109]
print("a * 2:", a * 2)  # Output: [0, 2, 4, ..., 18]
print("a / 2:", a / 2)  # Output: [0.0, 0.5, 1.0, ..., 4.5]
print("a ** 2:", a ** 2)  # Output: [0, 1, 4, ..., 81]
print("2 ** a:", 2 ** a)  # Output: [1, 2, 4, ..., 512]
print("a % 3:", a % 3)  # Modulo operation: [0, 1, 2, 0, 1, 2, 0, 1, 2, 0]
print("a % 5 >= 2:", a % 5 >= 2)  # Boolean array: [False, False, True, True, ..., True]

np.linspace(-3, 3, 7) / 0
# RuntimeWarning: divide by zero encountered in true_divide
# Output: [-inf, -inf, -inf, inf, inf, inf, inf]

x = np.linspace(-np.pi, np.pi, 50)  # 50 points between -π and π
y = np.sin(x)  # Compute sine for each x
print(y)

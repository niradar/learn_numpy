import numpy as np
from matplotlib import pyplot as plt

# Mathematical Functions
x = np.linspace(-np.pi, np.pi, 50)  # 50 points between -π and π
y = np.sin(x)  # Compute sine for each x

# Basic Plotting
# Single Plot
plt.plot(x, y)
plt.show()

# Multiple Plots
plt.plot(x, y, 'bp-', x, np.cos(x), 'go-')
# 'bp-': Blue line with pentagon markers for sine
# 'go-': Green line with circle markers for cosine
plt.show()

# Overlaying Multiple Lines
plt.plot(x, y)
plt.plot(x, y * 2)
plt.show()

# Loop-Based Plotting
# Multiple Lines in a Single Plot
n = 5
for i in range(n):
    plt.plot(x, y * i)

# Add Legends
for i in range(n):
    plt.plot(x, y * i, label=f"y * {i}")
plt.legend()
plt.show()

# Subplots
# Stacked Subplots
for i in range(n):
    plt.subplot(n, 1, i + 1)
    plt.plot(x, y * i)
    plt.title(f"y * {i}")
plt.show()

# Grid Layout Subplots
for i in range(n):
    plt.subplot(2, 3, i + 1)
    plt.plot(x, y * i)
    plt.title(f"y * {i}")

# Improve Layout with tight_layout
plt.tight_layout()

plt.show()


# Advanced Subplots with Shared Axes
fig, axes = plt.subplots(ncols=3, nrows=2, figsize=(12, 5), sharex='all', sharey='all')
for i, ax in enumerate(axes.flat):
    ax.plot(x, np.sin(x ** i))
    ax.set_title(f"$sin(y^{i})$")
fig.suptitle("THE FIGURE")
# plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

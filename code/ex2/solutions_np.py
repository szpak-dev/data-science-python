import numpy as np

# 1. Reverse a vector
vector = np.array([1, 2, 3, 4, 5])
reversed_vector = vector[::-1]

# 2. Create a 10x10 array with random values and find its mean, min, and max
array_10x10 = np.random.rand(10, 10)
mean_value = np.mean(array_10x10)
min_value = np.min(array_10x10)
max_value = np.max(array_10x10)

# 3. Create a 3D array with ones and surround it with zeros
array_3d = np.ones((3, 3, 3))
padded_array = np.pad(array_3d, pad_width=1, mode='constant', constant_values=0)

# 4. Find the closest value to a scalar in a vector
vector = np.array([1, 3, 7, 10, 12])
scalar = 8
closest_value = vector[np.abs(vector - scalar).argmin()]

# 5. Swap two rows in a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array_2d[[0, 1]] = array_2d[[1, 0]]

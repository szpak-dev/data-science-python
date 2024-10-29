import random

# 1. Reverse a vector
vector = [1, 2, 3, 4, 5]
reversed_vector = vector[::-1]

# 2. Create a 10x10 array with random values and find its mean, min, and max
array_10x10 = [[random.random() for _ in range(10)] for _ in range(10)]
mean_value = sum(sum(row) for row in array_10x10) / (10 * 10)
min_value = min(min(row) for row in array_10x10)
max_value = max(max(row) for row in array_10x10)

# 3. Create a 3D array with ones and surround it with zeros
array_3d = [[[1 for _ in range(3)] for _ in range(3)] for _ in range(3)]
padded_array = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            padded_array[i][j][k] = array_3d[i-1][j-1][k-1]

# 4. Find the closest value to a scalar in a vector
vector = [1, 3, 7, 10, 12]
scalar = 8
closest_value = min(vector, key=lambda x: abs(x - scalar))

# 5. Swap two rows in a 2D array
array_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
array_2d[0], array_2d[1] = array_2d[1], array_2d[0]

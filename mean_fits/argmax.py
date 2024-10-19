import numpy as np

# Create a 2D NumPy array
array_2d = np.array([[10, 12, 14], 
                     [11,  5,  9], 
                     [ 8, 15,  7]])

# Use np.argmax() to find the index of the maximum value in the flattened array
max_index_flat = np.argmax(array_2d)

# Convert the flattened index to a 2D index
max_index_2d = np.unravel_index(max_index_flat, array_2d.shape)

print(max_index_2d)

import numpy as np

def find_max_value_and_position(array):
    # Find the maximum value in the array
    max_value = np.max(array)
    
    # Find the position of the maximum value
    position = np.unravel_index(np.argmax(array), array.shape)
    
    return max_value, position

# Example usage
array = np.array([[1.5, 2.3, 3.1],
                  [4.2, 5.8, 6.7],
                  [7.4, 8.9, 9.6]])

max_value, position = find_max_value_and_position(array)
print(f"Maximum value: {max_value}")
print(f"Position: {position}")

import numpy as np

original = np.ones((3, 3))

print("Original array:")
print(original)

new_array = np.zeros((5, 5))

new_array[1:4, 1:4] = original

print("\n1 on the border and 0 inside in the array")
print("Output:")
print(new_array)

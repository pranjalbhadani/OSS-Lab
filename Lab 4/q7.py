import numpy as np

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

result = np.column_stack((array1, array2))

print("Column-wise stacked array:")
print(result)

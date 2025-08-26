import numpy as np
from collections import Counter

print("NumPy version:", np.__version__)


user_input = input("Enter a list of characters/integers separated by spaces: ")

input_list = user_input.split()

for i in range(len(input_list)):
    try:
        input_list[i] = int(input_list[i])
    except ValueError:
        pass

frequency = Counter(input_list)

print("Frequency of each element:")
for element, count in frequency.items():
    print(f"{element}: {count}")

binary_input = input("Enter a binary string (only 0s and 1s): ")

count_1 = binary_input.count('1')
count_0 = binary_input.count('0')

output = '1' * count_1 + '0' * count_0

print("Output:", output)

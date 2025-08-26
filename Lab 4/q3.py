def remove_nth_char(s, n):
    if n < 0 or n >= len(s):
        return "Error: Index out of range"
    
    return s[:n] + s[n+1:]

string_input = input("Enter a nonempty string: ")
index = int(input("Enter the index of the character to remove: "))

result = remove_nth_char(string_input, index)
print("Resulting string:", result)

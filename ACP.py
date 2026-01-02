# Test dictionary
test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

# Print the dictionary
print("Test Dictionary:", test_dict)

# Ask user to enter the frequency value to check
value = int(input("Enter the frequency value you want to check: "))

# Count how many words have this frequency
frequency_count = list(test_dict.values()).count(value)

# Print the result
print("The frequency of value", value, "is:", frequency_count)
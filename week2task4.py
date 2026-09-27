strings = ["hello", "python", "world"]

# Convert each string into list of characters
result = list(map(list, strings))

print("Original List:")
print(strings)

print("List of Lists:")
print(result)
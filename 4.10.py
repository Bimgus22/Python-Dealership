items = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

print("The first three items in the list are:")
print(items[:3])

print("Three items from the middle of the list are:")
middle = len(items) // 2
print(items[middle - 1: middle + 2])

print("The last three items in the list are:")
print(items[-3:])

# Create a new list containing only the even numbers from an existing list.

value = [2,3,4,5,6,5,6,8,94,46,54,42,24,12]

StoredValue = [] #list for storage
for i in value:
    if i % 2 == 0:
        StoredValue.append(i)
print(StoredValue)
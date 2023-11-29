# Write a Python program to find the union of two lists.

ValueList1 = [1, 2, 3, 4]
ValueList2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# Convert the lists to sets and find their union
union_result = set(ValueList1) | set(ValueList2)

# Convert the result back to a list
union_list = list(union_result)

print(union_list)

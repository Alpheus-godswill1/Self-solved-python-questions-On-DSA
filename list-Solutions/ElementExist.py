# Write a Python program to check if an element exists in a list.

TestList = [1,8,9,8,9]


foundItem = 8
for i in TestList:
    if foundItem  == i:
        print('Item Exist in this Index!')
    else:
        print('Item not found')

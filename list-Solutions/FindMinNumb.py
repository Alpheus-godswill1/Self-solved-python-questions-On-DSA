# Write a Python program to find the minimum element in a list.
value = [1,2,2,0,33]
minNum = value[0]
for i in value:
    if i < minNum:
        minNum = i
print(minNum)
# Write a Python program to find the maximum element in a list.
value = [1,2,2,33,33]
max = value[0]
for i in value:
    if max < i:
        max = i
print(max)
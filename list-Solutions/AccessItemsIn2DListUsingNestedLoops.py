# Write a Python program to access elements in a 2D list using nested loops.

value = [1,2,[2,3,4],[4,6,8,"hello world"]]

for x in value:
    for y in value:
        print(y,x)
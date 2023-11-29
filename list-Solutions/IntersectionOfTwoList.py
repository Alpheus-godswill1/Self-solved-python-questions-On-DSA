# Write a Python program to find the intersection of two lists.

TestValue = [2, 3, 4, 5, 55, 4, 6, 555]
Junky = [2, 3, 4, 66, 7, 99, 100]

ListIntersection = []

for i in TestValue:
    if i in Junky:
        ListIntersection.append(i)

print(ListIntersection)

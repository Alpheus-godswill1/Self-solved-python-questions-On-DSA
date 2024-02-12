# Write a Python program to access elements in a 2D list using nested loops.
# Access elements in a 2D list using nested loops:python

# Sample 2D list
matrix = [
    [1, 2,3,23,17],
    [4, 5,6,12,23],
    [7, 8, 19,9,12,23,67]
]

# Access elements using nested loops
rows = len(matrix)
cols = len(matrix[1])
# print(rows)
# print(cols)
for i in range(rows):
    print(i)
    for j in range(cols):
        print(matrix[i][j], end=' ')
    print()
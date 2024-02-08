# Write a Python program to access elements in a 2D list using nested loops.
# Access elements in a 2D list using nested loops:python

# Sample 2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access elements using nested loops
rows = len(matrix)
cols = len(matrix[0])

for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=' ')
    print()
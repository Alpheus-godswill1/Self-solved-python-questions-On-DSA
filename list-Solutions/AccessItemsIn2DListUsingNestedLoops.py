# Write a Python program to access elements in a 2D list using nested loops.
# Access elements in a 2D list using nested loops:python

# Sample 2D list
matrix = [
    [1, 2,3,23,17],
    [4, 5,6,12,23],
    [7, 8, 19,9,12,23,67],
    [1,2,3,4,5,6,7]
]

# Access elements using nested loops
rows = len(matrix)
cols = max(len(row) for row in matrix)
for i in range(rows):
    for j in range(cols):
        if j < len(matrix[i]):
            print(matrix[i][j], end=' ')
        else:
            print(' ', end=' ')
    print()
    


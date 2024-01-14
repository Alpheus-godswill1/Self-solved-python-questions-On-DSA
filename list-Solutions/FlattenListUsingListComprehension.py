# Use list comprehension to flatten a nested list (2D list) into a single list.

a = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15],[16, 17, 18, 19]]

b = [b for i in a for b in i ]
print(b)
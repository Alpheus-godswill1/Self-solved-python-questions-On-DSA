#  Create a list of squares for even numbers and cubes for odd numbers from 1 to 10 using list comprehension.

a = [i**2 if i % 2 == 0 else i**3 for i in range(11)]
print(a)
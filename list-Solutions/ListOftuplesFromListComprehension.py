# Create a list of tuples from two lists using list comprehension.

a = [1,2,3,4,5,6,7,8,9]
b = [1,2,3,4,5,6,7,8,9]

c = [ (i,j) for i,j in zip(a,b) ]
print(c)
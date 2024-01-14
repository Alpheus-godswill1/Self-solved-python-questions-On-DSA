# Create a list of even numbers from an existing list using list comprehension.
number = [1,2,3,4,5,6,7,8,9,10,11,12,13]
b = []
a = [ b.append(i) if i % 2== 0 else '' for i in number]
print(b)    
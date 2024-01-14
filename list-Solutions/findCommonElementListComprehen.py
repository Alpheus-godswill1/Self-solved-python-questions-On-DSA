# Find common elements between two lists using list comprehension.

a = [1,1,4,2,3,5,6,7,8,9,10]

b = [4,6,8,0,10,2,99,400,20]
CommonElementList = []
c = [CommonElementList.append(i) if i in b else '' for i in a ]
CommonElementList.sort()
print(CommonElementList)

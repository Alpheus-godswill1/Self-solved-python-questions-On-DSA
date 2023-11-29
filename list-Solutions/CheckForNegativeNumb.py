# Check if a list contains any negative numbers.

Value = [2,-3,4,-8,-6,-6,-35,9]
NegativeNumb = []
for  i in Value:
    if i < 0:
        NegativeNumb.append(i)
print(NegativeNumb)

# Find the index of the minimum element in a list.

Value = [1,-1,2,3,4,5]

index = 0
MinNumb = Value[index]

for i in Value:
    if MinNumb > i:
        MinNumb = i
        index += 1
print(index, MinNumb)

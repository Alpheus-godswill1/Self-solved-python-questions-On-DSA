# Find the index of the maximum element in a list.
Value = [1,2,3,4,95]

index = 0
MaxNumb = Value[index]

for i in Value:
    if MaxNumb < i:
        MaxNumb = i
        index += 1
print(index, MaxNumb)
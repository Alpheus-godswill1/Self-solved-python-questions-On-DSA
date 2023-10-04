# Write a Python program that finds the maximum of three numbers and stores it in a variable.

Value = [2,3,4]

print(max(Value))
maximumNumb = 0

for i in Value:
    if i > maximumNumb:
        maximumNumb = i
print(maximumNumb)
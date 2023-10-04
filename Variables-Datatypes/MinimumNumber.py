# Write a Python program that finds the Minimum of three numbers and stores it in a variable.

Value = [-2,3,4,-5,-6,-9,30,-78,-100,-9,-2,-111111]
print(min(Value))

Minimum = 0
for i in Value:
    if Minimum > i:
        Minimum = i
print(Minimum)




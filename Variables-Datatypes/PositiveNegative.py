#  Write a Python program that checks if a given number is positive, negative, or zero and stores the result in a variable.

Value = int(input("Input a number so it is checked if it's positive, Negative or Zero: "))

if Value > 0:
    print('Positive')
if Value < 0:
    print('Negative')
if Value == 0:
    print('Zero')
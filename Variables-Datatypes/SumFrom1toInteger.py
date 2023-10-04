#  Create a Python program that calculates the sum of all integers from 1 to a given number and stores it in a variable.

n = int(input('Enter any number of your choice: '))
Result = 0

for i in range(1, n+1):
    Result += i
print(Result)
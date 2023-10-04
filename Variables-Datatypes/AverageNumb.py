#  Write a Python program that calculates the average of three numbers using variables.

ValueA= float(input('input any number of your choice: '))
ValueB = float(input('input any number of your choice: '))
ValueC = float(input('input any number of your choice: '))

Result = (ValueA+ValueB+ValueC) / 3
print(Result)

#  Way to do it though 

numbers = [float(input("Input any number of your choice: ")) for i in range(0,3)]
Result = sum(numbers)/len(numbers)
print(Result)
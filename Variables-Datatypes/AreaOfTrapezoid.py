#  Write a Python program that calculates the area of a trapezoid using variables for the bases and height.
#  Formula for Area of Trapezoid, I don't know, but let's say it is == ½ (a + b) h
baseA = float(input("Please input a value for the base of the trapezoid: "))
baseB = float(input("Please input a value for the base of the trapezoid: "))
height =  float(input("Please input a value for the height of the trapezoid: "))


Result = float(1/2*(baseA  +  baseB) * height)
print(Result)
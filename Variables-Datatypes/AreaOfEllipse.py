#  Write a Python program that calculates the area of an ellipse using variables for major and minor axes.

import math 
"""
A = π × a × b

Where:

A is the area of the ellipse.
π (pi) is approximately 3.14159.
"a" is the length of the semi-major axis, which is the longer radius.
"b" is the length of the semi-minor axis, which is the shorter radius.

"""
LengthA = float(input("Write the length of the semi-major axis, this is the longer radius: "))
LengthB = float(input("Write the length of the semi-minor axis, this is the shorter radius: "))
Area = math.pi * LengthA * LengthB 
print(Area)
#  Write a Python program that calculates the area of a regular polygon using variables for side length and number of sides.
import math
"""
A = (n × s²) / (4 × tan(π/n))

Where:

A is the area of the regular polygon.
n is the number of sides in the polygon.
s is the length of each side.
π is the mathematical constant Pi (approximately 3.14159).
tan is the tangent function.

"""
numOfSides = float(input("Write the number of sides of the polygon: "))
lengthOfSides = float(input("Write the length of sides of the polygon: "))
Area = (numOfSides * (lengthOfSides **2)) / (4 * (math.tan(math.pi/numOfSides)))
print(Area)
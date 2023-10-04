# Create a Python program that calculates the area of a sector of a circle using variables for radius and angle.

import math
"""
A = (θ/360) × πr²

Where:

A is the area of the sector.
θ (theta) is the central angle of the sector in degrees.
π (pi) is approximately 3.14159.
r is the radius of the circle.

"""
theta = float(input("Input the value of your angle and this will be calculated in degrees: "))
radiusOfSector = float(input("Input the value of your radius and this will be calculated: "))
AreaOfSectorOfCircle = (theta/360) * math.pi * (radiusOfSector ** 2)
print(AreaOfSectorOfCircle)






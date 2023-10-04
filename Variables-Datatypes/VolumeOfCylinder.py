# Create a Python program that calculates the volume of a cylinder using variables for radius and height.
# Let's say that the volume of a cylinder = ⫪r²h

# Import math library

import math


Radius =  float(input("Please enter any radius of your choice: " ))
Height = float(input("Please enter any height of your choice: " ))


Result = math.pi * (Radius ** 2) * (Height)
print(Result)
# Write a Python program that converts Celsius to Fahrenheit using a variable for temperature in Celsius.
#  Celsius -> Fahrenheit Formula conversion  => °F = (°C × 9/5) + 32

Celsius = float(input("Write your celsius value: "))
Fahrenheit = ((Celsius * (9/5)) + 32)
print(f"Your fahrenheit value for {Celsius} celsius = {Fahrenheit}")


#  Write a Python program that converts a given temperature in Fahrenheit to Celsius and stores it in a variable.
#  Fahrenheit -> Celsius Formula conversion => °C = (°F - 32) × 5/9

Fahrenheit = float(input("Write your Fahrenheit value: "))
Celsius = ((Fahrenheit - 32) * (5/9))
print(f"Your celsius value for {Fahrenheit} fahrenheit = {Celsius}")
# Implement a function that reverses a string

def ReversedString(reversed_String):
    return ''.join(sorted(reversed_String, reverse = True))
reversed_String = "Hello"
print(ReversedString(reversed_String))



#  Most accurate method
def ReversedString(input_string):
    return input_string[::-1]

reversed_string = "Hello"
print(ReversedString(reversed_string))

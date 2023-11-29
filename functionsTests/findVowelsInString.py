# Create a function that counts the number of vowels in a given string.


Vowels = ['a','e','i','o','u']
Count = 0

def CountVowelInString(Value):
    StringInList = sorted(Value,reverse=False)
    for item in StringInList:
        if item in Vowels:
            global Count
            Count += 1
    return Count

Value = "Programming"

print(CountVowelInString(Value))
#  Create a Python program that checks if a given character is a vowel or a consonant and stores the result in a variable.

Vowels = ['a','e','i','o','u']
Value = input('Please write a character or letter of your choice: ')

if Value in Vowels:
    print(f'The letter ------{Value}------- is a vowel. ')
else:
    print(f'The character --------{Value}-------- is a consonant or symbol. ')
    
    
    

#  OR

Vowels = ['a', 'e', 'i', 'o', 'u']
Value = input('Please write a character or letter of your choice: ')

result = 'vowel' if Value in Vowels else 'consonant or symbol'
print(f'The letter "{Value}" is a {result}.')

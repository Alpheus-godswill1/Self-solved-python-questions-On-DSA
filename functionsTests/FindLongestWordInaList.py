# Implement a function that finds the longest word in a list of words.
Value = ['Hello World! ','Alpheus Godswillmplement ','AlphaNumerica ','hownt to know?fa function that finds the longest word in a list of words.']

def LongestItemFind(index = 0):
    Word = Value[index]
    for item in Value:    
        if len(item) > len(Word):
            Word = item
            index += 1
    print(f'||||{index}||||, ||||{len(Word)}||||, ||||{Word}||||')
LongestItemFind()
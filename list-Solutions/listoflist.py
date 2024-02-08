# Create a list of lists from a 2D list where each sublist contains elements of a different column.
import random

test = [[1,2,3,4], 
        [5,6,7,8],
        [9,10,11]]


ListOfList = [[row[i] for row in test] for i in range(0, len(test))]

print(ListOfList)
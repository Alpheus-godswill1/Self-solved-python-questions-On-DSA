
def multiplyListItems(items):
    if not items:
        return 1
    else:
        return items[0] * multiplyListItems(items[1:])

items = [1,2,3,4,5]
print(multiplyListItems(items))





# Create a function that finds the maximum element in a list.

def findMaxValueInList(Value) :
    if not Value:
        return
    MaxNumber = Value[0]
    for i in Value:
        if i > MaxNumber:
            MaxNumber = i
    return(MaxNumber)



Value = []
print(findMaxValueInList(Value))
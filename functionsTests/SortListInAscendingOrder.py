# Create a function that sorts a list of integers in ascending order.

def sortListInAscendingOrder(Value):
    Value.sort()
    return Value

Value = [4,3,2,5,6,7,10,9,1]
print(sortListInAscendingOrder(Value))
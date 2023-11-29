# Remove all occurrences of a specific element from a list.

Value = [2,2,2,2,2,2,3,3,3,3,5,6,7,8,9,10,3,3,2,2,2,11,12,13,14,15]


for ValueBeingRemoved in Value:
    if  ValueBeingRemoved == 2:
        Value.remove(ValueBeingRemoved)
        continue
print(Value)





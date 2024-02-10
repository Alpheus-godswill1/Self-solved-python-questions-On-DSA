number = [17,17,17,2,17,17,17,17]
min_value = 0

frequency = {}

for i in set(number):
    frequency[i] = 0
    for c in number:
        if c == i:
            frequency[c] += 1
            
min_value =  min([frequency[i] for i in frequency])
Actual_value = [ number for i, number in enumerate(frequency) if frequency[number] == min_value]

print(Actual_value)


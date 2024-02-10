numbers = [1,2,2,1,1,2,2,1,1,2,2,2,2,2,2,89,383]

frequency = {}

max_freq = 0
for i in set(numbers):
    frequency[i] = 0
    for z in numbers:
        if z == i: # z == main number in  list # i is the frequency key
            frequency[i] += 1
max_freq = max([frequency[i] for i in frequency ])
print(max_freq)
print(frequency)
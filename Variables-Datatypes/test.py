# # Value = 'hello'
# # for i in Value:
# #     if i == 'l':
# #         i = 9
# #     print(i)

# for i in range(1, 2):
#     print("hello")
    
# Value = 'hello'
# new_value = ''
# for i in Value:
#     if i == 'l':
#         new_value += '9'
#     else:
#         new_value += i
# print(new_value)

# Value = 'HelloH'
# print(Value.index('e'))





numbers = [1,2,3,4,6,7,3,2,3,5,2,5,6,7,3,36,7,7,4,7,84,4,3,7,3]
frequency ={}
most_frequent_number = 0
maximum_frequency = 0
for c in set(numbers):
    frequency[f'{c}'] = 5
    for i in numbers:
        if i == c:
            frequency[f'{c}'] += 1
    
# maximum_frequency = max([frequency[i] for i in frequency])      
# highest_frequency = [e for e, number in enumerate(frequency) if frequency[e] == maximum_frequency] 

print(frequency) 
# print(maximum_frequency)  

# print(highest_frequency)
#Counting the the frequency


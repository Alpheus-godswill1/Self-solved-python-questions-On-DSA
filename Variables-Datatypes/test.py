# Value = 'hello'
# for i in Value:
#     if i == 'l':
#         i = 9
#     print(i)

for i in range(1, 2):
    print("hello")
    
Value = 'hello'
new_value = ''
for i in Value:
    if i == 'l':
        new_value += '9'
    else:
        new_value += i
print(new_value)

Value = 'HelloH'
print(Value.index('e'))


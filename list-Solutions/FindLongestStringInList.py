# Find the longest string in a list of strings.

value = ['Hello woeld',
         'How are you',
         'am fine',
         'going is going',
         'we pulling up',
         'try get sense',
         'we move',
         'We eventually going to build tech with gritdurhieuhruiehryheorghe',
         'Am a blessing do you understand that',
         'We are trying to make things right',
         'How about you and the family',
         'FindLongestString','']

ItemsLength = value[0]

for i in value:
    if len(ItemsLength) < len(i):
        ItemsLength = i
print(ItemsLength)
# How do you prompt the user for multiple pieces of information in a single input statement?

Result = input('Enter value of your and separate them with spaces: ')
Name, age, weekDay = Result.split()
print("Name: " + Name)
print("Age: " + age)
print('WeekDay : ' + weekDay)
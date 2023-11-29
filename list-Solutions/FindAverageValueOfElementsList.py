# Find the average value of elements in a list.
n = int(input('This number determines a lot so be careful: '))
value = [float(input("Input as many numbers of your choice until the call stops: ")) for i in range(0,n)]

Result = sum(value)/len(value)
print(Result)

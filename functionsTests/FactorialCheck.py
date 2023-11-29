# Write a Python function that calculates the factorial of a given integer.


def factorial(n):
    if n == 1:
        return n
    else:
        return(n,'*',factorial(n - 1))
    
n = int(input("Enter any number of your choice to find it's factorial: "))
print("Now the factorial of",n,"is = ", factorial(n))



def factorial(n):
    if n == 1:
        return n
    else:
        return(n * factorial(n - 1))
    
num = int(input("Enter any number of your choice to find it's factorial: "))
print("Now the factorial of",num,"is = ", factorial(num))


# testSplit = 'An apple a day keeps the doctor away'.lower()
# subString = 'Apple'.lower()
# testlist = testSplit.split()
# for subString in testlist:
#     print('True')
#     break
# print(testlist)
# Create a function that checks whether a given number is prime or not.
def is_prime(number):
    if number < 2:
        return False
    
    for i in range(2, number):
        if number % i == 0:
            return False
        return True
print(is_prime(2))
for i in range(2, ):
    if is_prime(i):
        print(i, end=' ')
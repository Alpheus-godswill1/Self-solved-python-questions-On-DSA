def find_difference(a, b):
    result = 1
    result2 = 1
    for element in a:
        result *= element
    for element in b:
        result2 *= element

    return abs(result2 - result if result > result2 else result - result2)


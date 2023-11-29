# Check if two lists have any common elements.

Value1 = [1, 2, 3, 4, 5]
Value2 = [1, 2, 8, 4, 5]


for i in Value1:
    if i in Value2:
        print("Yes they have common elements")
    else:
        print("No they don't have common elements")
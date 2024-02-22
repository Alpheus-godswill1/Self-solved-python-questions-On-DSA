# Write a Python program to transpose a 2D list (convert rows to columns and vice versa).

Original = [[1,2,3,4,5], 
            [4,5,6,8,4], 
            [7,8,9,7], 
            [10,11,12,3]]

Trans = [[row[i] for row in Original] for i in range(0, len(Original))]

SecondTrans = [[row[i] for row in Trans] for i in range(len(Trans))]

testcase = []
for i in range(0, len(Original)):
    for row in Original:
        testcase.append(row[i])
print(testcase)
        

print(SecondTrans)
print(' ')

print(Trans)

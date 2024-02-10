testCase = [[1,2,3,5],
            [6,7,8,9],
            [10,11,12,13],
            [14,15,16,17],
            [18,19,20,21]]

Trans = [tuple(row[i] for row in testCase) for i in range(len(testCase[1]))]

Transpose = list(zip(*testCase))


print(Trans)
print(Transpose)
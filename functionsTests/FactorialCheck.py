testSplit = 'An apple a day keeps the doctor away'.lower()
subString = 'Apple'.lower()
testlist = testSplit.split()
for subString in testlist:
    print('True')
    break
print(testlist)
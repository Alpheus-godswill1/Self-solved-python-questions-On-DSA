# Create a list of words that start with a specific letter from a given list of words.

words = ['arise','ascend','chosen','Generation','royal','Attain','Advice','Lift','Willing','admit','abruptly','advanced']
c = []
b = [ c.append(i) if i.lower().startswith('a') else '' for i in words]
print(c)


def findPairsSumToK(inputArr, k):
    needed = set() 
    result = [] 
    for index, each in enumerate(inputArr): 
        if k-each not in needed: 
            needed.add(k-each)
        elif each in needed: 
            result.append((each, k-each))
    return result

print findPairsSumToK([1, 2, 4, 1, 2 ], 5)
print findPairsSumToK([1, 2, 4, 1, 2 ], 3)


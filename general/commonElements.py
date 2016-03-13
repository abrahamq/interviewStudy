#Find the common elements of 2 unsorted int arrays

def findCommonElem(first, second): 
    firstSet = set(first)
    secondSet = set(second)
    return firstSet.intersection(secondSet) 

print findCommonElem([1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 5, 8])



#Find the common elements of 2 sorted int arrays
def findCommonElemSorted(first, second): 
    arrays = [first, second] 
    longArr = []
    shortArr = [] 
    if len(arrays[0]) > len(arrays[1]):
        longArr = arrays[0] 
        shortArr = arrays[1] 
    else: 
        longArr = arrays[1] 
        shortArr = arrays[0] 

    shortCounter =0 
    index = 0 
    commonElements = []
    #if short < current long, then update short, stay at same place in long 
    #if short == current long, then found match, update both 
    #if short > current long, then update long, stay at same place in short 
    while (index < len(longArr)-1 ): 
        if (shortArr[shortCounter] < longArr[index]): 
            if (shortCounter < len(shortArr)-1):
                shortCounter += 1
            else: # make sure that at the end we keep going through long 
                index +=1 
        elif (shortArr[shortCounter] == longArr[index]): 
            commonElements.append(shortArr[shortCounter])
            if (shortCounter < len(shortArr)-1):
                shortCounter += 1
            index += 1 
        elif (shortArr[shortCounter] > longArr[index]): 
            index += 1 
    return commonElements


print findCommonElemSorted([1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 5, 8])

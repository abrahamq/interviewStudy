#Find the only element in an array that only occurs once.

def findElementOnlyOnce(array ): 
    # go through array,
    #O(n) time, O(n) extra space 
    result = set() 
    for each in array: 
        if each in result: 
            result.remove(each)
        else: 
            result.add(each) 
    return list(result)[0]

print findElementOnlyOnce([1,1, 2, 3,3]) #2 
print findElementOnlyOnce([1,1, 2, 9, 2, 3,3]) #9 


def findElementOnlyOnceBetterSpace(array): 
    #O(n) time, O(1) extra space 
    counter = 0 
    for each in array: 
        counter = counter ^ each 
    return counter 

print findElementOnlyOnceBetterSpace([1,1, 2, 9, 2, 3,3]) #9 



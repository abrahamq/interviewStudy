
def binarySearch(array, key): 
    middle = len(array)/2 
    if (array[middle] > key):
        return binarySearch(array[0:middle], key)
    elif(array[middle] == key):
        return middle 
    else: 
        return middle + binarySearch(array[middle:-1], key) 


print binarySearch([1,2,3,4,5,6], 5) 

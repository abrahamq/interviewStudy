#Given 2 integer arrays, determine of the 2nd array is a rotated version of the 1st array.
#Ex. Original Array A={1,2,3,5,6,7,8} Rotated Array B={5,6,7,8,1,2,3}


def isRotated(original, rotated): 
    #find where the rotation begins 
    before = 0 
    first = []
    second = [] 
    for index, each in enumerate(rotated): 
        if each < before: #found the break 
            first = rotated[index:len(rotated)]
            second = rotated[0: index] 
        before = each  

    first.extend(second) 
    print first
    for index, each in enumerate(original): 
        if original[index] != first[index]: 
            return False 
    return len(first) == len(original) 

print isRotated([1,2,3,5,6,7,8], [5,6,7,8,1,2,3])

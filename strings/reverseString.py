#Reverse a String iteratively and recursively

def reverseIt(string): 
    newString = "" 
    backCounter = len(string)-1
    for index, each in enumerate(string):
        newString += string[backCounter] 
        backCounter -= 1 
    return newString

print reverseIt("abcd")

def reverseRecursive(string):
    if len(string) == 0: 
        return "" 
    return string[-1] + reverseRecursive(string[0:len(string)-1] ) 

print reverseRecursive("abcd") 



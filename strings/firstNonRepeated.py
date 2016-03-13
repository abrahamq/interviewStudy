#Find the first non-repeated character in a String

def firstNonRepeat(string):
    before = string[0] 
    cutString = string[0:-1] 
    for index, each in enumerate(cutString): 
        if each == before: 
            continue
        else: 
            if index+1 > len(cutString)+1 or each != cutString[index+1]:
                return each  
            before = each 

print firstNonRepeat("aabbccdeeff") 



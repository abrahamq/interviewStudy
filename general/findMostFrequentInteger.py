#o(n) time, O(n) space 
def mostFrequent(inputArr): 
    frequency = dict(); 
    for each in inputArr: 
        if each not in frequency:
            frequency[each] = 1
        else: 
            frequency[each] = frequency[each]+1 
    top = 0 
    for each in inputArr: 
        if  frequency[each] > top: 
            top = each

    return top 


sample = [1, 2, 3, 4, 5, 5, 5]

print mostFrequent(sample)

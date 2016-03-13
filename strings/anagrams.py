def anagram(original, test): 
    originalSet = set(original)
    for each in test: 
        if test not in originalSet:
            return False 
    return len(original) == len(test) 

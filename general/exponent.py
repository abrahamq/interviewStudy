
def exponent(num, power):
    if power == 0: 
        return 1 
    return num*exponent(num, power-1)

print exponent(2, 3) 


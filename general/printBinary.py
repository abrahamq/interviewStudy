#Write a function that prints out the binary form of an int
import math 

def printBinary(n): 
    string = ""
    for i in range(31, 0,-1):
        temp = n >> i 
        string += str(temp%2)
    print string
    return 


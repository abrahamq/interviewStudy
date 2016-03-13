mem = dict()
def fib(n):
    if n in mem: 
        return mem[n]
    if (n == 1): 
        return 1
    if (n == 0): 
        return 0
    mem[n] = fib(n-1) + fib(n-2)
    return mem[n]

print fib(5)

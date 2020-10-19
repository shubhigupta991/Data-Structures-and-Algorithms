def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))

cache = {}
def fibDP(n):
    if n in cache:
        return cache[n]
    elif n < 2:
        cache[n] = n
        return n
    else:
        cache[n] = fibDP(n-1) + fibDP(n-2)
        return cache[n]

print(fib(10))

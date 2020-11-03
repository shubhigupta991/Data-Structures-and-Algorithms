def add80(n):
    print('Long Time')
    return n + 80

print('Add80')
print(add80(10))
print(add80(10))
print(add80(5))

print('MemoizedAdd80')
cache = {}
def memoizedadd80(n):
    if n in cache:
        return cache[n]
    else:
        print('Long Time')
        cache[n] = n + 80
        return cache[n]

print(memoizedadd80(10))
print(memoizedadd80(10))
print(memoizedadd80(5))
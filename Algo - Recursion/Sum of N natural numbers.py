def sum(num):
    if num == 1:
        return num
    return num + sum(num-1)


print(sum(10))
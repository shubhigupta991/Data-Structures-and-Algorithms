def reverseString(string):
    if len(string) == 0:
        return
    lastChar = string[-1]
    print(lastChar,end='')
    return reverseString(string[0:len(string)-1])

reverseString('Hello')
def reverse1(string):
    myList = []
    for i in range(len(string)-1,-1,-1):
        myList.append(string[i])

    revString = ''.join(myList)
    return revString

def reverse2(string):
    return string[::-1]

print(reverse1('Hello this is shubhangi!!'))
print(reverse2('Hello this is shubhangi!!'))



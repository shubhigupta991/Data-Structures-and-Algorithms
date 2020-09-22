def reverse(string):
    myList = []
    for i in range(len(string)):
        myList.append(string[i])
    reverse = ''.join(myList[::-1])
    return reverse
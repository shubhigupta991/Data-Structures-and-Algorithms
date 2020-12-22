def FirstRecurringElement(mylist):          # Array implementation
    for i in range(len(mylist)):            # O(n^2)
        for j in range(i+1,len(mylist)):
            if mylist[i] == mylist[j]:
                return mylist[i]
    return 0

def FirstRecurringElement2(mylist):         # Hash Table implementation
    mydict = {}                             # O(n)
    for element in mylist:
        if element in mydict:
            return element
        else:
            mydict[element] = mylist.index(element)
    return 0

mylist = [2,1,1,2,3,4,5]
x = FirstRecurringElement2(mylist)
print(x)


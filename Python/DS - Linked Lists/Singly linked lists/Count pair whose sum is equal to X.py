def countPair(h1, h2, n1, n2, x):
    '''
    h1:  head of linkedList 1
    h2:  head of linkedList 2
    n1:  len of  linkedList 1
    n2:   len of linkedList 1
    X:   given sum
    '''

    ptr = h1
    ptr2 = h2
    count = 0
    while ptr:
        my_list.append(x - ptr.data)
        ptr = ptr.next

    while ptr2:
        if ptr2.data in my_list:
            count += 1
        ptr2 = ptr2.next

    return count
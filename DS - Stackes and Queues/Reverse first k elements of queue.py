def reverseK(queue,k,n):
    list2 = queue[:k]
    list2.reverse()
    for i in range(len(list2)):
        queue[i] = list2[i]
    return queue
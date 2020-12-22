def addOne(head):
    i = 0
    sum1 = 0
    ptr = head
    while ptr:
        i += 1
        sum1 = sum1*10 + ptr.data
        ptr = ptr.next
    sum2 = sum1 + 1
    ptr = head
    i = i-1
    while i != -1:
        divisor = pow(10,i)
        data = sum2//divisor
        if data != ptr.data:
            ptr.data = data
        ptr = ptr.next
        sum2 = int(sum2%divisor)
        i -= 1
    return head
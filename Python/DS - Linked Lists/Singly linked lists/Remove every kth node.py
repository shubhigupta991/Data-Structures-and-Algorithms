def deleteK(head, k):
    temp = head
    i = 1
    if k == 1:
        head = None

    else:
        while temp.next:
            if i == k - 1:
                temp.next = temp.next.next
                i = 1
                temp = temp.next
                if temp == None:
                    break
                continue
            temp = temp.next
            i += 1

    return head
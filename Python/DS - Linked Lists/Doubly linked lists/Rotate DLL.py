def update(llist, p):
    for i in range(p):
        firstnode = llist.head
        secondnode = llist.head.next
        firstnode.next = None
        secondnode.prev = None
        llist.head = secondnode
        temp = llist.head
        while temp.next:
            temp = temp.next
        temp.next = firstnode
        firstnode.prev = temp
    return llist
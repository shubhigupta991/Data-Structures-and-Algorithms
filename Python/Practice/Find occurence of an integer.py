def count(head, search_for):
    count = 0
    ptr = head
    while ptr != None:
        if ptr.data == search_for:
            count += 1
        ptr = ptr.next
    return count
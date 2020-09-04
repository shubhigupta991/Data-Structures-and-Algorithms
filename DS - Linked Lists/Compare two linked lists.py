def compare(head1, head2):
    ptr1 = head1
    ptr2 = head2
    while ptr1 or ptr2:
        if ptr1 == None:
            return -1
        elif ptr2 == None:
            return 1
        elif ord(ptr1.data) > ord(ptr2.data):
            return 1
        elif ord(ptr1.data) < ord(ptr2.data):
            return -1
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return 0
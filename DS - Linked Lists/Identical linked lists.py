def areIdentical(head1, head2):
    ptr1 = head1
    ptr2 = head2
    while ptr1 or ptr2:
        if ptr1 == None or ptr2 == None:
            return False
        elif ptr1.data != ptr2.data:
            return False
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return True
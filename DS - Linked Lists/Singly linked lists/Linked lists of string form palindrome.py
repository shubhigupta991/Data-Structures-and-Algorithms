def compute(head):
    my_list = []
    ptr = head
    while ptr:
        my_list.append(ptr.data)
        ptr = ptr.next
    my_list2 = my_list[::-1]
    return my_list == my_list2
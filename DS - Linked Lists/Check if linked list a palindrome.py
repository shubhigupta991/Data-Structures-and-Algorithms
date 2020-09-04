def isPalindrome(head):
    temp = head
    my_list = []
    while temp != None:
        my_list.append(temp.data)
        temp = temp.next
    number = my_list[:]
    reverse = my_list[::-1]
    return number == reverse
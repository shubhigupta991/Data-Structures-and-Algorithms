def deleteNode(curr_node):
    next_node = curr_node.next
    curr_node.data = next_node.data
    curr_node.next = next_node.next

def DFSInorder(root):
    stack = []
    temp = root
    array = []
    while True:
        if temp != None:
            stack.append(temp)
            temp = temp.left
        elif stack:
            temp = stack.pop()
            array.append(temp.data)
            temp = temp.right
        else:
            break

    return array

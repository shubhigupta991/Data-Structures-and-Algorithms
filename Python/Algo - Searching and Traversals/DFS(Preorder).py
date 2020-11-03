def DFSPreorder(root):
    stack = []
    temp = root
    array = []
    while temp != None:
        array.append(temp.data)
        if temp.right:
            stack.append(temp.right)
        if temp.left:
            temp = root.left
        else:
            if stack == []:
                temp = None
            else:
                temp = stack.pop()
    return array

def DFSPreorder(root):
    stack = []
    temp = root
    array = []
    while temp != None:
        array.append(temp.data)
        if root.right:
            stack.append(root.right)
        if root.left:
            temp = root.left
        else:
            temp = stack.pop()

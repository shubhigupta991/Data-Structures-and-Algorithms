def DFSPostorder(root):
    stack = []
    temp = root
    array = []

    def peek(stack):
        if len(stack) > 0:
            return stack[-1]
        return None

    while True:
        while temp:
            if temp.right != None:
                stack.append(temp.right)
            stack.append(temp)
            temp = temp.left

        temp = stack.pop()

        if temp.right != None and peek(stack) == temp.right:
            stack.pop()
            stack.append(temp)
            temp = temp.right
        else:
            array.append(temp.data)
            temp = None
        if len(stack) <= 0:
            break
    return array

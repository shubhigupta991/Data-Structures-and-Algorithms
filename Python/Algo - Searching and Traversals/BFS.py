''' This function represent implementation of BFS '''

def BFS(root):
    currentNode = root
    queue = []
    array = []
    queue.append(currentNode)

    while len(queue):
        currentNode = queue.pop(0)
        array.append(currentNode.data)
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
    return array